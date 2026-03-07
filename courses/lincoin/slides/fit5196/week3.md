---
theme: default
title: FIT5196 - Week 3
layout: cover
info: |
  ## FIT5196 Week 3
  Regular Expressions
highlighter: shiki
drawings:
  persist: false
transition: slide-left
---

# FIT5196 Data Wrangling

## Week 3: Regular Expressions

---

# Agenda

1. What are Regular Expressions?
2. Basic Syntax and Patterns
3. Common Operators
4. Practical Applications
5. Python `re` Module

---
layout: section
---

# Introduction to Regex

---

# What are Regular Expressions?

> "Regular expressions are sequences of characters that define search patterns, mainly for use in pattern matching with strings."

<div class="mt-6 border-l-2 border-sky-700 pl-4 text-sm text-slate-600">
Regex is a powerful tool for:<br>
• Finding patterns in text<br>
• Validating data formats<br>
• Extracting information<br>
• Cleaning and transforming strings
</div>

---

# Why Use Regex in Data Wrangling?

<div class="grid grid-cols-2 gap-6">

<div class="border border-slate-300 bg-white/60 p-4">
  <h3 class="font-bold">Common Use Cases</h3>
  <ul class="text-sm mt-2">
    <li>Email validation</li>
    <li>Phone number extraction</li>
    <li>Date format parsing</li>
    <li>URL identification</li>
    <li>Log file analysis</li>
  </ul>
</div>

<div class="border border-slate-300 bg-white/60 p-4">
  <h3 class="font-bold">Data Cleaning</h3>
  <ul class="text-sm mt-2">
    <li>Remove special characters</li>
    <li>Standardize formats</li>
    <li>Extract substrings</li>
    <li>Find and replace</li>
    <li>Split text data</li>
  </ul>
</div>

</div>

---
layout: section
---

# Regex Syntax

---

# Basic Patterns

| Pattern | Matches | Example |
|---------|---------|---------|
| `.` | Any character | `a.c` → "abc", "aec" |
| `^` | Start of string | `^Hello` |
| `$` | End of string | `world$` |
| `\d` | Digit (0-9) | `\d{3}` → "123" |
| `\w` | Word character | `\w+` → "hello" |
| `\s` | Whitespace | `\s+` → "   " |
| `\b` | Word boundary | `\bword\b` |

---

# Quantifiers

| Symbol | Meaning | Example |
|--------|---------|---------|
| `*` | 0 or more | `a*` → "", "a", "aaa" |
| `+` | 1 or more | `a+` → "a", "aaa" |
| `?` | 0 or 1 | `colou?r` → "color", "colour" |
| `{n}` | Exactly n | `\d{4}` → "2024" |
| `{n,}` | n or more | `\d{2,}` |
| `{n,m}` | Between n and m | `\d{2,4}` |

---

# Character Classes

| Pattern | Matches |
|---------|---------|
| `[abc]` | a, b, or c |
| `[^abc]` | Not a, b, or c |
| `[a-z]` | Any lowercase letter |
| `[A-Z]` | Any uppercase letter |
| `[0-9]` | Any digit |
| `[a-zA-Z]` | Any letter |

---
layout: section
---

# Python `re` Module

---

# Key Functions

```python
import re

# Search for pattern
re.search(pattern, string)

# Find all matches
re.findall(pattern, string)

# Replace matches
re.sub(pattern, replacement, string)

# Split by pattern
re.split(pattern, string)

# Match at beginning
re.match(pattern, string)
```

---

# Practical Examples

```python
import re

# Extract emails
text = "Contact: john@email.com or jane@work.org"
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
# ['john@email.com', 'jane@work.org']

# Validate phone number
phone = "(03) 9902-0400"
pattern = r'\(\d{2}\)\s\d{4}-\d{4}'
match = re.match(pattern, phone)

# Clean text
dirty = "Price: $1,234.56!!!"
clean = re.sub(r'[^\d.]', '', dirty)
# '1234.56'
```

---
layout: statement
---

Mastering regex takes practice.

Start simple and build complexity gradually.

---
layout: end
---

# Next Week

## Exploratory Data Analysis (EDA)

- Understanding your data
- Statistical summaries
- Visualization techniques
