# Agent Workplan

Use this plan to coordinate parallel Ass2 completion.

## Shared Rules

- Work in `materials/fit5196/ass2_2026`.
- Preserve user-provided input files.
- Do not reuse old 2025 Task 1 business rules.
- Final notebook/report prose should be English. Bilingual notes are allowed in helper markdown only.
- Keep notebooks readable: short markdown explanations, visible outputs, and no noisy dependency-install cells.

## Agent 1: Task 1 Core Solver

Owns:

- `Group024_ass2_task1.ipynb`
- `Group024_ass2_task1.py`
- `Group024_dirty_data_solution.csv`
- `Group024_missing_data_solution.csv`
- `Group024_outlier_data_solution.csv`

Must follow `TASK1_AGENT_GUIDE.md`.

## Agent 2: Task 2 Notebook

Owns:

- `Group024_ass2_task2.ipynb`

Must follow `TASK2_REUSE_GUIDE.md`.

## Agent 3: QA and Integration

Owns:

- guide markdown maintenance
- final QA scripts/checks
- presentation/reflection notes
- deliverable checklist

Suggested output file:

- `ASS2_PRESENTATION_AND_QA_NOTES.md`

## Final QA Checklist

- CSVs parse with `pandas.read_csv`.
- Output columns exactly match input columns.
- Dirty and missing outputs preserve 500 rows.
- Outlier output preserves columns and removes only selected rows.
- No missing values remain in `Group024_missing_data_solution.csv`.
- `branch_code` values are only `BK`, `NS`, `TP`.
- `order_type` matches protected `time`.
- Recomputed `order_price` matches `order_items`.
- Recomputed graph distance matches `distance_to_customer_KM` within rounding tolerance.
- Task 2 notebook includes a final recommendation table.
- Notebook outputs are visible.
- `.py` file exists for Task 1 plagiarism checking.

