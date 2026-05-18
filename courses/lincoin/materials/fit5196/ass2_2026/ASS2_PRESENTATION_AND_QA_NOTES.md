# ASS2 Presentation, Reflection, and QA Notes

Owner: Agent 3 QA/docs integration.

Scope: presentation/reflection support and final checks only. Do not edit notebooks, solution CSVs, or source data from this file.

## Presentation Storyline

Use a short end-to-end wrangling narrative rather than presenting the work as isolated code cells.

1. Problem framing: Group024 received three order datasets with different quality tasks: dirty values to correct, missing values to impute, and delivery-fee outliers to remove.
2. Reference integration: 2026 food-delivery rules require branch metadata plus a road-network graph from `nodes.csv` and `edges.csv`; old 2025 warehouse/Haversine assumptions are not valid.
3. Task 1 method: profile first, encode meal windows/menus/branch prefixes/graph distances as reusable structures, then apply rule-based and model-based fixes with validation after each export.
4. Task 2 method: profile `suburb_info.xlsx`, compare scaling and power transformations using skewness, scale, correlation, and linearity evidence, then recommend transformations for later linear modelling.
5. Quality assurance: final outputs are checked structurally, semantically, and logically before submission, with special attention to exact headers and parsable CSVs.

## FIT5196 Weeks 1-11 Reflection Links

- Weeks 1-2: The notebooks should show the complete wrangling pipeline: discovery, EDA, rule design, cleaning/transformation, validation, documentation, and export QA.
- Week 3: Date, time, order ID, branch code, and `order_items` formats should be validated as structured text before correction.
- Weeks 4-5: Profiling should justify fixes using shapes, missingness, category summaries, distributions, correlations, and visible examples of anomalies.
- Week 6: The solution should use suitable data structures: dictionaries for menus, branch prefixes, and meal windows; a weighted graph or Dijkstra fallback for road distance.
- Weeks 7-8: Issues should be classified before action: accuracy errors in dirty data, completeness problems in missing data, consistency checks across derived fields, and delivery-fee outliers.
- Week 9: Task 2 should compare transformations with evidence, not preference: scale, skewness, target correlation, and linearity diagnostics.
- Week 10: Task 1 demonstrates data integration by enriching order rows with branch metadata and road-network reference data.
- Week 11: Final validation should combine structure, domain logic, and read-back checks on exported deliverables.

Suggested reflection sentence for notebooks or presentation:

> This step follows the FIT5196 cleansing workflow: audit the issue, choose a rule-based or model-based fix, then verify that no new inconsistency is introduced.

## Final Deliverable Checklist

- `Group024_dirty_data_solution.csv`
- `Group024_missing_data_solution.csv`
- `Group024_outlier_data_solution.csv`
- `Group024_ass2_task1.ipynb`
- `Group024_ass2_task1.py`
- `Group024_ass2_task2.ipynb`
- `Group024_ass2_task4.pdf`
- `Group024_AI_Records.docx`, `.pdf`, or `.txt` if generative AI is declared
- Final zip: `Group024_ass2.zip`

## CSV QA Gates

Expected input columns for all three order datasets:

```text
order_id,date,time,order_type,branch_code,order_items,order_price,customer_lat,customer_lon,customerHasloyalty?,distance_to_customer_KM,delivery_fee
```

Minimum final checks:

- All three solution CSVs parse with `pandas.read_csv`.
- Output columns exactly match their corresponding input columns.
- Dirty and missing solution files preserve 500 rows.
- Outlier solution preserves columns and removes only full rows.
- Missing solution has no remaining null values.
- `branch_code` values are only `BK`, `NS`, and `TP`.
- `order_type` agrees with protected `time` using breakfast, lunch, and dinner windows.
- `order_price` agrees with parsed `order_items` and the relevant meal menu.
- `distance_to_customer_KM` agrees with graph shortest-path distance within rounding tolerance.
- Dirty-data protected fields are not changed where the assignment says they must remain protected: `order_id`, `time`, numeric item quantities in `order_items`, and `delivery_fee`.

## Runnable QA Skeleton

Run this after Agents 1 and 2 finish. It intentionally checks hard gates first.

```python
from pathlib import Path
import pandas as pd

base = Path(".")
inputs = {
    "dirty": base / "Group024_dirty_data.csv",
    "missing": base / "Group024_missing_data.csv",
    "outlier": base / "Group024_outlier_data.csv",
}
outputs = {
    "dirty": base / "Group024_dirty_data_solution.csv",
    "missing": base / "Group024_missing_data_solution.csv",
    "outlier": base / "Group024_outlier_data_solution.csv",
}

for key, path in outputs.items():
    assert path.exists(), f"Missing output: {path}"
    src = pd.read_csv(inputs[key])
    out = pd.read_csv(path)
    assert list(out.columns) == list(src.columns), f"{path}: columns changed"
    if key in {"dirty", "missing"}:
        assert len(out) == 500, f"{path}: expected 500 rows"
    if key == "outlier":
        assert len(out) <= 500, f"{path}: outlier output gained rows"
    assert set(out["branch_code"].dropna()).issubset({"BK", "NS", "TP"}), f"{path}: invalid branch code"

missing = pd.read_csv(outputs["missing"])
assert missing.isna().sum().sum() == 0, "Missing-data solution still contains null values"

for required in ["Group024_ass2_task1.ipynb", "Group024_ass2_task1.py", "Group024_ass2_task2.ipynb"]:
    assert (base / required).exists(), f"Missing deliverable: {required}"

print("Hard-gate CSV and file-existence checks passed.")
```

Additional semantic checks should be implemented in the Task 1 notebook/script because they need the same parsed menus, graph, and helper functions used by the solver.

## Task 2 QA Notes

- Confirm the notebook reads `suburb_info.xlsx` successfully. If local pandas fails with `ImportError: openpyxl`, install or activate an environment with `openpyxl` before executing the notebook.
- Confirm the required fields are present: `number_of_houses`, `number_of_units`, `population`, `aus_born_perc`, `median_income`, and `median_house_price`.
- Confirm the final section contains a recommendation table with one recommendation per feature and optional target transformation advice.
- Confirm notebook outputs are visible before export/submission.

## Submission Risk Notes

- Exact CSV headers are a marking gate; do not reorder or rename columns.
- Do not copy 2025 Task 1 business rules into 2026 work. The 2026 task uses food-delivery meals, branch-specific delivery-fee models, loyalty discount logic, and graph distance.
- Keep final prose in English for submission-facing notebooks/reports.
- Before zipping, reopen the final zip or list its contents to verify the exact expected filenames are present.
