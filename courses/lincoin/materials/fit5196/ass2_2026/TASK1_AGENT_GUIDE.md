# Task 1 Agent Guide

Goal: create `Group024_ass2_task1.ipynb`, `Group024_ass2_task1.py`, and the three Task 1 solution CSV files.

## Files

Inputs:

- `Group024_dirty_data.csv`
- `Group024_missing_data.csv`
- `Group024_outlier_data.csv`
- `branches.csv`
- `nodes.csv`
- `edges.csv`

Outputs:

- `Group024_dirty_data_solution.csv`
- `Group024_missing_data_solution.csv`
- `Group024_outlier_data_solution.csv`

All output CSVs must preserve the same column names as their respective inputs. Dirty and missing outputs should preserve row count and order. Outlier output removes rows only.

## 2026 Business Rules

Meal windows:

- Breakfast: `08:00:00` to `12:00:00`
- Lunch: `12:00:01` to `16:00:00`
- Dinner: `16:00:01` to `20:00:00`

Branch mapping from order ID prefix:

- `ORDA`, `ORDK`, `ORDX` -> `BK`
- `ORDC`, `ORDI`, `ORDZ` -> `NS`
- `ORDB`, `ORDJ`, `ORDY` -> `TP`

Menus and unit prices:

- Breakfast: `Cereal=21.00`, `Coffee=7.50`, `Eggs=22.00`, `Pancake=24.25`
- Lunch: `Burger=31.00`, `Chicken=32.00`, `Fries=12.00`, `Salad=17.20`, `Steak=45.00`
- Dinner: `Fish&Chips=35.00`, `Pasta=27.50`, `Salmon=41.00`, `Shrimp=54.00`

Branch graph nodes:

- `NS`: `2455254505`
- `TP`: `1390575046`
- `BK`: `1889485053`

Dirty-data protected columns:

- `order_id`
- `time`
- numeric item quantities inside `order_items`
- `delivery_fee`

Do not alter protected columns in the dirty-data solution.

## Algorithm Roadmap

1. Discovery and EDA
   - Load all files.
   - Preserve original column order.
   - Parse `order_items` with `ast.literal_eval`.
   - Summarize shapes, missingness, category values, and obvious anomalies.

2. Rule and structure design
   - Build dictionaries for branch prefixes, meal windows, menu items, and item prices.
   - Build an undirected weighted graph from `edges.csv`, using `distance(m)` as the weight.
   - Use `networkx` if available; otherwise use a `heapq` Dijkstra fallback.

3. Dirty data cleaning
   - Each dirty row has at most one anomaly. Fix with a priority guard so one detected problem does not trigger multiple edits.
   - Fix candidate families:
     - normalize dates to `YYYY-MM-DD`;
     - derive `order_type` from protected `time`;
     - infer uppercase `branch_code` from `order_id`;
     - correct the single wrong item in `order_items` by matching menu and exact `order_price`;
     - recompute `order_price` from valid items and prices;
     - fix `customer_lat/customer_lon` by matching `nodes.csv` candidates, including sign flip and lat/lon swap candidates;
     - recompute `distance_to_customer_KM` with Dijkstra and round to 3 decimals.
   - Never modify `delivery_fee` in dirty data.

4. Missing data imputation
   - Fill `branch_code` from order ID prefix.
   - Fill `distance_to_customer_KM` from graph distance after branch is known.
   - Fill `delivery_fee` from a branch-specific linear model.

5. Delivery fee model
   - Fit one model per branch.
   - Features: weekend flag, time code, graph distance in km.
   - Time code: Breakfast 0, Lunch 1, Dinner 2.
   - Undo loyalty discount before fitting by doubling observed fees for loyal customers.
   - Reapply loyalty discount after prediction by halving predicted fee for loyal customers.
   - Report R2 and residual diagnostics.

6. Outlier removal
   - Detect outliers only with respect to `delivery_fee`.
   - Recommended: branch-specific model residuals after undoing loyalty, then IQR or MAD threshold per branch.
   - Remove whole rows; do not cap or overwrite values.

7. Validation and export
   - Read back every CSV with pandas.
   - Assert exact columns.
   - Assert no missing values remain in the missing-data solution.
   - Assert valid branch codes and meal types.
   - Include concise markdown explaining why each method reflects FIT5196 data quality, cleansing, integration, and validation concepts.

