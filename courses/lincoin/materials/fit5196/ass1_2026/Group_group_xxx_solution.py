from __future__ import annotations

from pathlib import Path
import json
import re
from xml.etree import ElementTree as ET

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


pd.set_option("display.max_columns", 100)
pd.set_option("display.width", 160)
pd.set_option("display.max_colwidth", 120)


BASE_DIR = Path.cwd()
JSON_PATH = BASE_DIR / "GroupXXX.json"
XML_PATH = BASE_DIR / "GroupXXX.xml"
OUTPUT_CSV = BASE_DIR / "GroupXXX_dataset.csv"
SAMPLE_OUTPUT_PATH = BASE_DIR / "sample_output.csv"

TARGET_COLUMNS = [
    "Post_ID",
    "User_ID",
    "Secret",
    "Server",
    "Title",
    "Is_Public",
    "Is_Friend",
    "Is_Family",
    "Farm",
    "City",
    "Country",
    "Post_Date",
    "Taken_Date",
    "Tags",
    "Latitude",
    "Longitude",
    "Description",
    "Min_Taken_Date",
]

RENAME_MAP = {
    "PostID": "Post_ID",
    "UserID": "User_ID",
    "secret": "Secret",
    "server": "Server",
    "title": "Title",
    "ispublic": "Is_Public",
    "isfriend": "Is_Friend",
    "isfamily": "Is_Family",
    "farm": "Farm",
    "City": "City",
    "Country": "Country",
    "Post_date": "Post_Date",
    "Post date": "Post_Date",
    "Taken_date": "Taken_Date",
    "Taken date": "Taken_Date",
    "tags": "Tags",
    "latitude": "Latitude",
    "longitude": "Longitude",
    "description": "Description",
    "min_taken_date": "Min_Taken_Date",
}

TEXT_LOWER_COLUMNS = ["Title", "City", "Country", "Tags", "Description"]
NUMERIC_COLUMNS = [
    "Post_ID",
    "Server",
    "Is_Public",
    "Is_Friend",
    "Is_Family",
    "Farm",
    "Latitude",
    "Longitude",
]


def parse_json_records(json_path: Path) -> pd.DataFrame:
    records = json.loads(json_path.read_text(encoding="utf-8"))
    if not isinstance(records, list):
        raise ValueError("JSON root must be a list")
    return pd.DataFrame(records)


def parse_xml_records(xml_path: Path) -> pd.DataFrame:
    tree = ET.parse(xml_path)
    root = tree.getroot()
    rows: list[dict[str, str | None]] = []

    for record in root.findall(".//Record"):
        row = {}
        for child in record:
            row[child.tag] = child.text
        rows.append(row)

    return pd.DataFrame(rows)


def strip_tags_and_emoji(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"[\U00010000-\U0010ffff]", " ", text)
    return text


def keep_latin_content_only(text: str) -> str:
    pattern = r"[^\u0000-\u024F\u1E00-\u1EFF0-9\s\.,;:!\?\-_'\"/\\@#&\(\)\[\]\{\}\+\*=<>%\|~`]+"
    return re.sub(pattern, " ", text)


def normalise_text_value(value) -> str:
    if pd.isna(value):
        return "NaN"

    text = str(value)
    text = strip_tags_and_emoji(text)
    text = keep_latin_content_only(text)
    text = re.sub(r"\s+", " ", text).strip()

    return text if text else "NaN"


def standardise_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns=RENAME_MAP).copy()

    for col in TARGET_COLUMNS:
        if col not in df.columns:
            df[col] = pd.NA

    df = df[TARGET_COLUMNS]

    for col in TEXT_LOWER_COLUMNS:
        df[col] = df[col].map(normalise_text_value)
        df[col] = df[col].where(df[col].eq("NaN"), df[col].str.lower())

    for col in df.columns:
        if col not in TEXT_LOWER_COLUMNS and df[col].dtype == object:
            df[col] = df[col].map(normalise_text_value)

    for col in NUMERIC_COLUMNS:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    for col in ["Post_Date", "Taken_Date", "Min_Taken_Date"]:
        df[col] = df[col].map(lambda x: "NaN" if pd.isna(x) else str(x).strip())
        df[col] = df[col].replace({"": "NaN", "None": "NaN", "nan": "NaN"})

    df = df.replace({pd.NA: np.nan})
    df = df.drop_duplicates().reset_index(drop=True)
    df = df.fillna("NaN")
    return df


def build_merged_dataset() -> pd.DataFrame:
    sample_columns = pd.read_csv(SAMPLE_OUTPUT_PATH, nrows=0).columns.tolist()
    assert sample_columns == TARGET_COLUMNS, "sample_output.csv columns do not match TARGET_COLUMNS"

    json_df_raw = parse_json_records(JSON_PATH)
    xml_df_raw = parse_xml_records(XML_PATH)

    print("JSON shape:", json_df_raw.shape)
    print("XML shape:", xml_df_raw.shape)

    json_df = standardise_dataframe(json_df_raw)
    xml_df = standardise_dataframe(xml_df_raw)

    print("JSON standardised shape:", json_df.shape)
    print("XML standardised shape:", xml_df.shape)

    merged_df = pd.concat([json_df, xml_df], ignore_index=True)
    rows_before = len(merged_df)
    merged_df = merged_df.drop_duplicates().reset_index(drop=True)
    rows_after = len(merged_df)

    print("Rows before deduplication:", rows_before)
    print("Rows after deduplication:", rows_after)
    print("Duplicates removed:", rows_before - rows_after)

    assert merged_df.columns.tolist() == TARGET_COLUMNS, "Final columns do not match required output structure"

    merged_df.to_csv(OUTPUT_CSV, index=False)
    print(f"Saved merged dataset to: {OUTPUT_CSV}")
    return merged_df


def prepare_eda_dataset(merged_df: pd.DataFrame) -> pd.DataFrame:
    eda_df = merged_df.replace("NaN", pd.NA).copy()

    for col in ["Post_Date", "Taken_Date", "Min_Taken_Date"]:
        eda_df[col] = pd.to_datetime(eda_df[col], errors="coerce")

    for col in NUMERIC_COLUMNS:
        eda_df[col] = pd.to_numeric(eda_df[col], errors="coerce")

    eda_df["Description_Length"] = eda_df["Description"].fillna("").str.len()
    eda_df["Tag_Count"] = (
        eda_df["Tags"].fillna("").str.split(",").map(lambda items: len([item for item in items if item.strip()]))
    )
    eda_df["Post_Year"] = eda_df["Post_Date"].dt.year
    eda_df["Post_Month"] = eda_df["Post_Date"].dt.to_period("M").astype("string")

    return eda_df


def dataset_overview(eda_df: pd.DataFrame) -> pd.DataFrame:
    overview = pd.DataFrame(
        {
            "dtype": eda_df.dtypes.astype(str),
            "missing_count": eda_df.isna().sum(),
            "missing_ratio": (eda_df.isna().mean() * 100).round(2),
            "n_unique": eda_df.nunique(dropna=True),
        }
    ).sort_values(by="missing_ratio", ascending=False)
    return overview


def finish_plot(fig) -> None:
    fig.tight_layout()
    plt.close(fig)


def run_eda_plots(eda_df: pd.DataFrame) -> None:
    missing_ratio = (eda_df.isna().mean() * 100).sort_values(ascending=False)
    fig = plt.figure(figsize=(10, 5))
    missing_ratio.plot(kind="bar", color="steelblue")
    plt.title("Missing Value Ratio by Attribute")
    plt.ylabel("Missing Ratio (%)")
    plt.xlabel("Attribute")
    plt.xticks(rotation=60, ha="right")
    finish_plot(fig)

    top_countries = eda_df["Country"].dropna().value_counts().head(10)
    top_cities = eda_df["City"].dropna().value_counts().head(10)
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    top_countries.sort_values().plot(kind="barh", ax=axes[0], color="teal")
    axes[0].set_title("Top 10 Countries")
    axes[0].set_xlabel("Record Count")
    top_cities.sort_values().plot(kind="barh", ax=axes[1], color="darkorange")
    axes[1].set_title("Top 10 Cities")
    axes[1].set_xlabel("Record Count")
    finish_plot(fig)

    post_year_counts = eda_df["Post_Year"].dropna().astype(int).value_counts().sort_index()
    fig = plt.figure(figsize=(10, 4))
    post_year_counts.plot(kind="line", marker="o", color="purple")
    plt.title("Number of Posts by Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Posts")
    plt.grid(alpha=0.3)
    finish_plot(fig)

    tag_series = eda_df["Tags"].dropna().str.split(",").explode().str.strip()
    tag_series = tag_series[tag_series.ne("")]
    top_tags = tag_series.value_counts().head(15)
    fig = plt.figure(figsize=(10, 5))
    top_tags.sort_values().plot(kind="barh", color="forestgreen")
    plt.title("Top 15 Tags")
    plt.xlabel("Frequency")
    finish_plot(fig)

    country_year_df = eda_df.dropna(subset=["Country", "Post_Year"]).copy()
    top5_countries = country_year_df["Country"].value_counts().head(5).index.tolist()
    country_year_df = country_year_df[country_year_df["Country"].isin(top5_countries)]
    country_year_counts = country_year_df.groupby(["Post_Year", "Country"]).size().unstack(fill_value=0).sort_index()
    fig = plt.figure(figsize=(11, 5))
    for country in country_year_counts.columns:
        plt.plot(country_year_counts.index, country_year_counts[country], marker="o", label=country)
    plt.title("Post Trend Over Time for Top 5 Countries")
    plt.xlabel("Year")
    plt.ylabel("Number of Posts")
    plt.legend()
    plt.grid(alpha=0.3)
    finish_plot(fig)

    geo_df = eda_df.dropna(subset=["Latitude", "Longitude"]).copy()
    fig = plt.figure(figsize=(10, 5))
    plt.scatter(geo_df["Longitude"], geo_df["Latitude"], alpha=0.35, s=10, color="crimson")
    plt.title("Geographical Distribution of Photo Records")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(alpha=0.2)
    finish_plot(fig)

    numeric_cols = [
        "Post_ID",
        "Server",
        "Is_Public",
        "Is_Friend",
        "Is_Family",
        "Farm",
        "Latitude",
        "Longitude",
        "Description_Length",
        "Tag_Count",
    ]
    corr_input = eda_df[numeric_cols].copy()
    corr_input = corr_input.loc[:, corr_input.nunique(dropna=True) > 1]
    corr = corr_input.corr(numeric_only=True)
    fig, ax = plt.subplots(figsize=(9, 7))
    im = ax.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
    ax.set_xticks(range(len(corr.columns)))
    ax.set_xticklabels(corr.columns, rotation=45, ha="right")
    ax.set_yticks(range(len(corr.index)))
    ax.set_yticklabels(corr.index)
    ax.set_title("Correlation Heatmap for Numeric Features")
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    finish_plot(fig)

    plot_df = eda_df.dropna(subset=["Description_Length", "Tag_Count"]).copy()
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    axes[0].scatter(plot_df["Tag_Count"], plot_df["Description_Length"], alpha=0.35, s=12, color="navy")
    axes[0].set_title("Tag Count vs Description Length")
    axes[0].set_xlabel("Tag Count")
    axes[0].set_ylabel("Description Length")

    privacy_summary = eda_df[["Is_Public", "Is_Friend", "Is_Family"]].apply(pd.Series.value_counts).fillna(0).astype(int)
    privacy_summary.plot(kind="bar", ax=axes[1], color=["#1f77b4", "#ff7f0e", "#2ca02c"])
    axes[1].set_title("Distribution of Privacy Flags")
    axes[1].set_xlabel("Flag Value")
    axes[1].set_ylabel("Count")
    finish_plot(fig)


def main() -> None:
    print("Working directory:", BASE_DIR)
    print("JSON file:", JSON_PATH.name)
    print("XML file:", XML_PATH.name)
    print("Output CSV:", OUTPUT_CSV.name)

    assert JSON_PATH.exists(), f"Missing file: {JSON_PATH}"
    assert XML_PATH.exists(), f"Missing file: {XML_PATH}"
    assert SAMPLE_OUTPUT_PATH.exists(), f"Missing file: {SAMPLE_OUTPUT_PATH}"

    merged_df = build_merged_dataset()
    eda_df = prepare_eda_dataset(merged_df)
    overview = dataset_overview(eda_df)

    print("\nDataset overview:")
    print(overview.head(10).to_string())

    print("\nTop countries:")
    print(eda_df["Country"].dropna().value_counts().head(10).to_string())

    print("\nTop cities:")
    print(eda_df["City"].dropna().value_counts().head(10).to_string())

    run_eda_plots(eda_df)


if __name__ == "__main__":
    main()
