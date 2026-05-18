from __future__ import annotations

from pathlib import Path
from typing import Callable

import numpy as np
import pandas as pd


class Task1NotebookTools:
    """A thin classroom helper for Task 1 notebooks.

    This class intentionally does not contain attribute-specific cleaning
    logic. The notebook should compute masks, replacement values, model
    predictions, and validation checks. This helper only manages common
    notebook mechanics: loading data, one-anomaly tracking, reporting,
    before/after display, row removal, validation tables, and export.
    """

    OUTPUT_COLUMNS = [
        "order_id",
        "date",
        "time",
        "order_type",
        "branch_code",
        "order_items",
        "order_price",
        "customer_lat",
        "customer_lon",
        "customerHasloyalty?",
        "distance_to_customer_KM",
        "delivery_fee",
    ]

    def __init__(self, folder: str | Path, group_id: str = "024"):
        self.folder = Path(folder)
        self.group_id = group_id
        self.raw = {
            "dirty": pd.read_csv(self.folder / f"Group{group_id}_dirty_data.csv"),
            "missing": pd.read_csv(self.folder / f"Group{group_id}_missing_data.csv"),
            "outlier": pd.read_csv(self.folder / f"Group{group_id}_outlier_data.csv"),
        }
        self.branches = pd.read_csv(self.folder / "branches.csv")
        self.nodes = pd.read_csv(self.folder / "nodes.csv")
        self.edges = pd.read_csv(self.folder / "edges.csv")

        self.frames: dict[str, pd.DataFrame] = {}
        self.flags: dict[str, pd.Series] = {}
        self.log: list[dict] = []

    def overview(self) -> pd.DataFrame:
        rows = []
        for name, frame in self.raw.items():
            rows.append(
                {
                    "dataset": name,
                    "rows": len(frame),
                    "columns": frame.shape[1],
                    "missing_cells": int(frame.isna().sum().sum()),
                    "duplicated_order_id": int(frame["order_id"].duplicated().sum()),
                }
            )
        print("Loaded Task 1 files.")
        return pd.DataFrame(rows)

    def column_summary(self, dataset: str) -> pd.DataFrame:
        frame = self.raw[dataset]
        print(f"[{dataset}] rows={len(frame)}, columns={frame.shape[1]}")
        return (
            pd.DataFrame(
                {
                    "dtype": frame.dtypes.astype(str),
                    "missing": frame.isna().sum(),
                    "unique": frame.nunique(dropna=True),
                }
            )
            .reset_index(names="column")
        )

    def start(self, dataset: str) -> pd.DataFrame:
        self.frames[dataset] = self.raw[dataset].copy()
        self.flags[dataset] = pd.Series("", index=self.frames[dataset].index, dtype="object")
        if dataset == "dirty":
            print("[dirty:start] protected columns: order_id, time, delivery_fee, item quantities")
        elif dataset == "missing":
            print(f"[missing:start] missing_cells={int(self.frames[dataset].isna().sum().sum())}")
        elif dataset == "outlier":
            print("[outlier:start] target attribute: delivery_fee")
        return self.frames[dataset]

    def frame(self, dataset: str) -> pd.DataFrame:
        return self.frames[dataset]

    def fix_values(
        self,
        dataset: str,
        step: str,
        issue_mask: pd.Series,
        replacements: dict[str, object],
        sample_columns: list[str],
        remaining_check: Callable[[pd.DataFrame], pd.Series] | None = None,
        n: int = 8,
    ) -> pd.DataFrame:
        """Apply column replacements and print a consistent step report."""
        frame = self.frames[dataset]
        issue_mask = self._as_bool_mask(issue_mask, frame.index)

        if dataset == "dirty":
            apply_mask = issue_mask & self.flags[dataset].eq("")
            skipped = int((issue_mask & self.flags[dataset].ne("")).sum())
        else:
            apply_mask = issue_mask
            skipped = 0

        columns = ["order_id"] + [col for col in sample_columns if col != "order_id"]
        before = frame.loc[apply_mask, columns].copy()

        for column, value in replacements.items():
            self._assign(frame, apply_mask, column, value)

        if dataset == "dirty":
            self.flags[dataset].loc[apply_mask] = step

        after = frame.loc[apply_mask, columns].copy()
        remaining = self._remaining(frame, remaining_check)
        self._record(dataset, step, int(issue_mask.sum()), int(apply_mask.sum()), remaining, skipped)

        result = pd.concat(
            [before.add_suffix("_before"), after.add_suffix("_after")],
            axis=1,
        )
        return result.head(n)

    def remove_rows(
        self,
        dataset: str,
        step: str,
        issue_mask: pd.Series,
        sample_columns: list[str],
        n: int = 10,
    ) -> pd.DataFrame:
        frame = self.frames[dataset]
        issue_mask = self._as_bool_mask(issue_mask, frame.index)
        removed = frame.loc[issue_mask, ["order_id"] + sample_columns].copy()
        before_rows = len(frame)
        self.frames[dataset] = frame.loc[~issue_mask].copy()
        after_rows = len(self.frames[dataset])

        self._record(dataset, step, int(issue_mask.sum()), before_rows - after_rows, 0, 0)
        print(f"[{dataset}:{step}] rows_before={before_rows}, rows_after={after_rows}")
        return removed.head(n)

    def validate(self, dataset: str, checks: list[dict]) -> pd.DataFrame:
        result = pd.DataFrame(checks)
        print(f"[{dataset}:validate] passed={int(result['passed'].sum())}/{len(result)}")
        return result

    def step_log(self, dataset: str | None = None) -> pd.DataFrame:
        result = pd.DataFrame(self.log)
        if dataset is not None and len(result):
            result = result[result["dataset"].eq(dataset)]
        return result.reset_index(drop=True)

    def export_all(self):
        outputs = {
            f"Group{self.group_id}_dirty_data_solution.csv": self.frames["dirty"],
            f"Group{self.group_id}_missing_data_solution.csv": self.frames["missing"],
            f"Group{self.group_id}_outlier_data_solution.csv": self.frames["outlier"],
        }
        for filename, frame in outputs.items():
            frame[self.OUTPUT_COLUMNS].to_csv(self.folder / filename, index=False)
            print(f"[export] {filename}: rows={len(frame)}, columns={len(self.OUTPUT_COLUMNS)}")

    def read_back_outputs(self) -> pd.DataFrame:
        rows = []
        for dataset in ["dirty", "missing", "outlier"]:
            filename = f"Group{self.group_id}_{dataset}_data_solution.csv"
            frame = pd.read_csv(self.folder / filename)
            rows.append(
                {
                    "file": filename,
                    "rows": len(frame),
                    "columns": frame.shape[1],
                    "missing_cells": int(frame.isna().sum().sum()),
                    "same_columns": list(frame.columns) == self.OUTPUT_COLUMNS,
                }
            )
        print("[read-back] exported CSV files parsed successfully")
        return pd.DataFrame(rows)

    def compare_with_saved_outputs(self) -> pd.DataFrame:
        rows = []
        for dataset in ["dirty", "missing", "outlier"]:
            current = self.frames[dataset][self.OUTPUT_COLUMNS].reset_index(drop=True)
            saved = pd.read_csv(self.folder / f"Group{self.group_id}_{dataset}_data_solution.csv")
            rows.append(
                {
                    "dataset": dataset,
                    "same_shape": current.shape == saved.shape,
                    "same_columns": list(current.columns) == list(saved.columns),
                    "numeric_close": self._numeric_close(current, saved),
                }
            )
        print("[compare] current in-memory results checked against saved CSV files")
        return pd.DataFrame(rows)

    def _assign(self, frame: pd.DataFrame, mask: pd.Series, column: str, value: object):
        if callable(value):
            frame.loc[mask, column] = value(frame, mask)
        elif isinstance(value, pd.Series):
            frame.loc[mask, column] = value.loc[mask]
        elif isinstance(value, pd.DataFrame):
            frame.loc[mask, column] = value.loc[mask, column]
        else:
            frame.loc[mask, column] = value

    def _as_bool_mask(self, mask: pd.Series, index: pd.Index) -> pd.Series:
        result = pd.Series(mask, index=index)
        return result.fillna(False).astype(bool)

    def _remaining(
        self,
        frame: pd.DataFrame,
        remaining_check: Callable[[pd.DataFrame], pd.Series] | None,
    ) -> int:
        if remaining_check is None:
            return 0
        remaining_mask = self._as_bool_mask(remaining_check(frame), frame.index)
        return int(remaining_mask.sum())

    def _record(
        self,
        dataset: str,
        step: str,
        flagged: int,
        fixed: int,
        remaining: int,
        skipped: int,
    ):
        self.log.append(
            {
                "dataset": dataset,
                "step": step,
                "flagged": flagged,
                "fixed": fixed,
                "remaining": remaining,
                "skipped_by_tracker": skipped,
            }
        )
        print(
            f"[{dataset}:{step}] "
            f"flagged={flagged}, fixed={fixed}, remaining={remaining}, skipped_by_tracker={skipped}"
        )

    def _numeric_close(self, left: pd.DataFrame, right: pd.DataFrame) -> bool:
        if left.shape != right.shape or list(left.columns) != list(right.columns):
            return False
        for column in left.columns:
            if pd.api.types.is_numeric_dtype(left[column]) or pd.api.types.is_numeric_dtype(right[column]):
                if not np.allclose(left[column].to_numpy(), right[column].to_numpy(), equal_nan=True):
                    return False
            else:
                if not left[column].astype(str).equals(right[column].astype(str)):
                    return False
        return True
