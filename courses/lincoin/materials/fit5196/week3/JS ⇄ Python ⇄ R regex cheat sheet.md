# JS ⇄ Python ⇄ R regex cheat sheet



## **Quick translation table**



| **Task**                   | **JavaScript**                         | **Python (**re**)**                      | **R (base)**                                 | **R (stringr)**                          |
| -------------------------- | -------------------------------------- | ---------------------------------------- | -------------------------------------------- | ---------------------------------------- |
| **Literal pattern**        | /[bdf]eer/                             | r"[bdf]eer"                              | "[bdf]eer"                                   | "[bdf]eer"                               |
| **Find all matches**       | "beer deer feer".match(/[bdf]eer/g)    | re.findall(r"[bdf]eer", text)            | regmatches(text, gregexpr("[bdf]eer", text)) | str_extract_all(text, "[bdf]eer")        |
| **Test if any match**      | /[bdf]eer/.test(text)                  | re.search(r"[bdf]eer", text) is not None | grepl("[bdf]eer", text)                      | str_detect(text, "[bdf]eer")             |
| **Get first match object** | text.match(/[bdf]eer/)                 | re.search(r"[bdf]eer", text)             | regexpr("[bdf]eer", text)                    | str_match(text, "[bdf]eer")              |
| **Replace all**            | text.replace(/[bdf]eer/g, "XXX")       | re.sub(r"[bdf]eer", "XXX", text)         | gsub("[bdf]eer", "XXX", text)                | str_replace_all(text, "[bdf]eer", "XXX") |
| **Capture groups**         | /(\w+)-(\d+)/ then .match() or .exec() | re.findall(r"(\w+)-(\d+)", text)         | regexec("(\\w+)-(\\d+)", text)               | str_match(text, "(\\w+)-(\\d+)")         |



## **Flags mapping**



| **Meaning**             | **JS flag**              | **Python flag**           | **R (base)**                        | **R (stringr)**              |
| ----------------------- | ------------------------ | ------------------------- | ----------------------------------- | ---------------------------- |
| **Global / find all**   | g                        | (use findall or finditer) | gregexpr                            | str_*_all()                  |
| **Case-insensitive**    | i                        | re.IGNORECASE             | ignore.case=TRUE                    | regex(..., ignore_case=TRUE) |
| **Multiline ^/$**       | m                        | re.MULTILINE              | perl=TRUE + anchors behave per PCRE | regex(..., multiline=TRUE)   |
| **Dot matches newline** | s                        | re.DOTALL                 | perl=TRUE with (?s) inline          | regex(..., dotall=TRUE)      |
| **Unicode-aware**       | u (default in modern JS) | re.UNICODE (default 3.x)  | PCRE via perl=TRUE                  | regex(... ) uses ICU         |



## **Notes**



- **JS uses /pattern/flags**; **Python/R use strings**. In Python prefer **raw strings** like r"\d+" so backslashes aren’t doubled.
- In **R base**, add perl=TRUE to get full PCRE behavior when needed, e.g. gregexpr("(?s)foo.*bar", text, perl=TRUE).
- For **find all**: JS needs the g flag; Python uses findall; R uses gregexpr (base) or *_all functions (stringr).

