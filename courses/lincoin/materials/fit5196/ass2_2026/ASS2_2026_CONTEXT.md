# FIT5196 Ass2 2026 Context Guide

This folder is the working area for Group024 Assessment 2, Semester 1 2026.

## Working Roadmap

Use the FIT5196 data wrangling pipeline throughout the assignment:

`Discovery -> EDA/Profile -> Rule/Structure Design -> Cleaning/Transformation -> Validation -> Documentation -> Export QA`

Short Chinese memory aid: 先理解数据, 再设计规则, 最后清洗和验证. Do not jump straight into changing values.

## 2026 Deliverables

- `Group024_dirty_data_solution.csv`
- `Group024_missing_data_solution.csv`
- `Group024_outlier_data_solution.csv`
- `Group024_ass2_task1.ipynb`
- `Group024_ass2_task1.py`
- `Group024_ass2_task2.ipynb`
- `Group024_ass2_task4.pdf`
- `Group024_AI_Records.docx/.pdf/.txt` if generative AI is declared

Final zip name: `Group024_ass2.zip`.

## Marking Focus

- Task 1 Data Cleansing: 18/40
- Task 2 Data Reshaping: 6/40
- Task 3 Presentation: 14/40
- Task 4 AI Declaration: 2/40

CSV output structure is a hard gate. Files must be parsable and preserve the exact expected headers. A bad header can cause zero for the affected output file.

## Major Difference From Old Ass2

Old 2025 Ass2 was an online electronics-store task using warehouses, Haversine distance, seasons, sentiment, coupon discount, and `delivery_charges`.

2026 Ass2 is a food-delivery task using branches, road-network graph distance, meal periods, branch-specific delivery models, loyalty discount, and `delivery_fee`.

Use old Ass2 only as reference for:

- report structure
- EDA flow
- helper function style
- output/read-back QA
- Task 2 reshaping style

Do not copy old Task 1 business rules.

## Unit Learning Links To Reflect

- Weeks 1-2: show the whole wrangling process, not only final code.
- Week 3: validate structured text patterns such as dates and IDs.
- Weeks 4-5: profile the data before fixing it.
- Week 6: use suitable structures: dictionaries for rules and graphs for road distances.
- Weeks 7-8: classify quality issues before cleaning: accuracy, completeness, consistency, outliers.
- Week 9: compare transformations using scale, skewness, correlation, and linearity evidence.
- Week 10: integrate and enrich order data with branch and graph reference files.
- Week 11: validate outputs structurally, semantically, and logically.

Suggested notebook reflection sentence:

> This step follows the FIT5196 cleansing workflow: audit the issue, choose a rule-based or model-based fix, then verify that no new inconsistency is introduced.

