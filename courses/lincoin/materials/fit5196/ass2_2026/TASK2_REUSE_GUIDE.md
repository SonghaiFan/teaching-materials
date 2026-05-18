# Task 2 Reuse Guide

Goal: create `Group024_ass2_task2.ipynb`.

Use old Task 2 only as a reference. The best reference is:

`../ass2/Group_032_ass2_task2_FS.ipynb`

The old and 2026 `suburb_info.xlsx` files contain the same data, so the analysis approach is reusable. Update the narrative for the 2026 rubric: Task 2 is now 6/40 and requires a clear final recommended transformation set.

## Required Columns

Features:

- `number_of_houses`
- `number_of_units`
- `population`
- `aus_born_perc`
- `median_income`

Target:

- `median_house_price`

## Notebook Roadmap

1. Discovery and loading
   - Load only `suburb_info.xlsx`.
   - Convert `%`, `$`, and comma-formatted values to numeric.
   - Confirm shape, columns, duplicates, and missingness.

2. EDA and profiling
   - Descriptive statistics.
   - Feature scale comparison.
   - Histograms and boxplots.
   - Skewness and outlier observations.
   - Pearson/Spearman correlations with the target.
   - Scatterplots with regression trend lines.

3. Transformation comparison
   - Scaling: StandardScaler, MinMaxScaler, RobustScaler.
   - Transformations: log/log1p, sqrt, Box-Cox, Yeo-Johnson.
   - Evaluate using scale, skewness reduction, correlation/linearity, and optional simple OLS diagnostics.

4. Recommendation
   - Provide one final recommendation per feature.
   - Optionally recommend a target transformation for later modelling.
   - Explain tradeoffs in plain English.

## Likely Recommendation Direction

- `number_of_houses`: Box-Cox or Yeo-Johnson, then scale.
- `number_of_units`: Box-Cox or Yeo-Johnson, then scale.
- `population`: sqrt, Box-Cox, or Yeo-Johnson, then scale.
- `aus_born_perc`: keep original shape; scale if needed for modelling.
- `median_income`: keep original or light power transform; scale for modelling.
- `median_house_price`: consider log, Box-Cox, or Yeo-Johnson if later modelling benefits from a less skewed target.

Avoid saying that a final predictive model is required. Simple OLS diagnostics can be used as evidence, but the task is data preparation for a later linear model.

