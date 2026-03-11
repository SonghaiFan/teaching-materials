#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path


BULLETS = ("•", "▪", "§", "-", "–", "—", "*")


def run_command(args: list[str]) -> str:
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return result.stdout


def pdf_page_count(pdf_path: Path) -> int:
    info = run_command(["pdfinfo", str(pdf_path)])
    match = re.search(r"^Pages:\s+(\d+)$", info, flags=re.MULTILINE)
    if not match:
        raise RuntimeError(f"Could not read page count for {pdf_path}")
    return int(match.group(1))


def extract_pages(pdf_path: Path) -> list[str]:
    text = run_command(["pdftotext", str(pdf_path), "-"])
    pages = [page for page in text.split("\f") if page.strip()]
    return [page.replace("\x0c", "").strip() for page in pages]


def looks_like_heading(line: str) -> bool:
    if not line or len(line) > 90:
        return False
    if line.startswith(BULLETS):
        return False
    if re.search(r"\s{2,}", line):
        return False
    if line[0].islower():
        return False
    if line.endswith(":"):
        return True
    alpha = [ch for ch in line if ch.isalpha()]
    if not alpha:
        return False
    upper_ratio = sum(1 for ch in alpha if ch.isupper()) / len(alpha)
    if upper_ratio > 0.9:
        return True
    return len(line.split()) <= 5 and not line.endswith((".", ";", ",")) and upper_ratio > 0.2


def normalize_line(line: str) -> tuple[str, str]:
    stripped = line.strip()
    if not stripped:
        return ("blank", "")

    for bullet in BULLETS:
        if stripped.startswith(bullet):
            content = stripped[len(bullet) :].strip()
            return ("bullet", content)

    if re.match(r"^[A-Za-z]\.\s+", stripped):
        return ("list", stripped)

    if re.match(r"^\d+\.\s+", stripped):
        return ("list", stripped)

    if looks_like_heading(stripped):
        return ("heading", stripped)

    return ("text", stripped)


def should_join(previous_kind: str, previous_text: str, current_text: str) -> bool:
    if previous_kind not in {"bullet", "text", "list"}:
        return False
    if not previous_text or not current_text:
        return False
    if current_text[0].islower():
        return True
    return previous_text.endswith(("(", "/", "-", "&"))


def page_to_markdown(page_number: int, page_text: str) -> str:
    cleaned: list[tuple[str, str]] = []

    for raw_line in page_text.splitlines():
        kind, value = normalize_line(raw_line)
        if kind == "blank":
            if cleaned and cleaned[-1][0] != "blank":
                cleaned.append((kind, value))
            continue

        if cleaned and cleaned[-1][0] != "blank":
            previous_kind, previous_value = cleaned[-1]
            if should_join(previous_kind, previous_value, value):
                cleaned[-1] = (previous_kind, f"{previous_value} {value}")
                continue

        cleaned.append((kind, value))

    body_lines: list[str] = []
    for kind, value in cleaned:
        if kind == "blank":
            if body_lines and body_lines[-1] != "":
                body_lines.append("")
        elif kind == "heading":
            body_lines.append(f"### {value}")
        elif kind == "bullet":
            body_lines.append(f"- {value}")
        else:
            body_lines.append(value)

    body = "\n".join(body_lines).strip()
    return f"## Page {page_number}\n\n{body}\n"


def convert_pdf(pdf_path: Path, output_path: Path | None) -> Path:
    output_path = output_path or pdf_path.with_suffix(".md")
    page_count = pdf_page_count(pdf_path)
    pages = extract_pages(pdf_path)

    header = [
        f"# {pdf_path.stem}",
        "",
        f"> Source: `{pdf_path.name}`",
        f"> Pages: {page_count}",
        f"> Conversion: extracted embedded PDF text with `pdftotext`",
        "",
        "---",
        "",
    ]

    content = "\n---\n\n".join(
        page_to_markdown(index, page) for index, page in enumerate(pages, start=1)
    )
    output_path.write_text("\n".join(header) + content, encoding="utf-8")
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert PDF text to Markdown.")
    parser.add_argument("pdfs", nargs="+", help="PDF files to convert")
    args = parser.parse_args()

    for pdf in args.pdfs:
        pdf_path = Path(pdf).resolve()
        output_path = convert_pdf(pdf_path, None)
        print(output_path)


if __name__ == "__main__":
    main()
