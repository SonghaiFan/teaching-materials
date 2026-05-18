#!/usr/bin/env python3
"""FIT5196 Assessment 2 Task 1 cleansing solution for Group024.

The script follows the 2026 food-delivery rules:
- structured order rules for date, meal period, branch prefix, menu, and price;
- road-network shortest-path distances from branch nodes to customer nodes;
- branch-specific linear delivery-fee models using weekend, meal time code, and distance;
- read-back validation for all exported CSV files.
"""

from __future__ import annotations

import ast
import heapq
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Callable

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

try:
    import networkx as nx
except ImportError:  # pragma: no cover - fallback kept for portable notebooks
    nx = None


ROOT = Path(__file__).resolve().parent

DIRTY_INPUT = ROOT / "Group024_dirty_data.csv"
MISSING_INPUT = ROOT / "Group024_missing_data.csv"
OUTLIER_INPUT = ROOT / "Group024_outlier_data.csv"
BRANCHES_INPUT = ROOT / "branches.csv"
NODES_INPUT = ROOT / "nodes.csv"
EDGES_INPUT = ROOT / "edges.csv"

DIRTY_OUTPUT = ROOT / "Group024_dirty_data_solution.csv"
MISSING_OUTPUT = ROOT / "Group024_missing_data_solution.csv"
OUTLIER_OUTPUT = ROOT / "Group024_outlier_data_solution.csv"

BRANCH_PREFIX = {
    "ORDA": "BK",
    "ORDK": "BK",
    "ORDX": "BK",
    "ORDC": "NS",
    "ORDI": "NS",
    "ORDZ": "NS",
    "ORDB": "TP",
    "ORDJ": "TP",
    "ORDY": "TP",
}

BRANCH_NODES = {
    "NS": 2455254505,
    "TP": 1390575046,
    "BK": 1889485053,
}

MEAL_PRICES = {
    "Breakfast": {
        "Cereal": 21.00,
        "Coffee": 7.50,
        "Eggs": 22.00,
        "Pancake": 24.25,
    },
    "Lunch": {
        "Burger": 31.00,
        "Chicken": 32.00,
        "Fries": 12.00,
        "Salad": 17.20,
        "Steak": 45.00,
    },
    "Dinner": {
        "Fish&Chips": 35.00,
        "Pasta": 27.50,
        "Salmon": 41.00,
        "Shrimp": 54.00,
    },
}

TIME_CODE = {
    "Breakfast": 0,
    "Lunch": 1,
    "Dinner": 2,
}

PROTECTED_DIRTY_COLUMNS = ["order_id", "time", "delivery_fee"]


@dataclass
class FeeModelReport:
    branch_code: str
    rows: int
    r2: float
    intercept: float
    coefficients: dict[str, float]
    residual_mean: float
    residual_std: float


@dataclass
class Task1Results:
    dirty_repairs: dict[str, int]
    missing_repairs: dict[str, int]
    missing_model_reports: list[FeeModelReport]
    outlier_removed: dict[str, int]
    outlier_model_reports: list[FeeModelReport]
    validation: dict[str, dict[str, object]]


def read_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def branch_from_order_id(order_id: str) -> str:
    prefix = str(order_id)[:4]
    if prefix not in BRANCH_PREFIX:
        raise ValueError(f"Unknown order prefix {prefix!r} in order_id {order_id!r}")
    return BRANCH_PREFIX[prefix]


def meal_from_time(value: str) -> str:
    hour, minute, second = [int(part) for part in str(value).split(":")]
    seconds = hour * 3600 + minute * 60 + second
    if 8 * 3600 <= seconds <= 12 * 3600:
        return "Breakfast"
    if 12 * 3600 + 1 <= seconds <= 16 * 3600:
        return "Lunch"
    if 16 * 3600 + 1 <= seconds <= 20 * 3600:
        return "Dinner"
    raise ValueError(f"Time {value!r} is outside the assignment meal windows")


def normalize_date(value: object) -> str | None:
    text = str(value)
    formats = (
        "%Y-%m-%d",
        "%d-%m-%Y",
        "%Y/%m/%d",
        "%d/%m/%Y",
        "%Y-%d-%m",
        "%Y/%d/%m",
    )
    for fmt in formats:
        try:
            return datetime.strptime(text, fmt).strftime("%Y-%m-%d")
        except ValueError:
            pass
    return None


def parse_items(value: object) -> list[tuple[str, int]]:
    parsed = ast.literal_eval(str(value))
    return [(str(item), int(quantity)) for item, quantity in parsed]


def order_total(items: list[tuple[str, int]], meal_type: str) -> float:
    prices = MEAL_PRICES[meal_type]
    return round(sum(prices[item] * quantity for item, quantity in items), 2)


def valid_menu_items(items: list[tuple[str, int]], meal_type: str) -> bool:
    prices = MEAL_PRICES[meal_type]
    return all(item in prices for item, _ in items)


def format_items(items: list[tuple[str, int]]) -> str:
    return repr([(item, int(quantity)) for item, quantity in items])


def correct_wrong_item_name(
    items: list[tuple[str, int]], meal_type: str, target_price: float
) -> list[tuple[str, int]]:
    """Change exactly one item name while preserving all quantities."""
    prices = MEAL_PRICES[meal_type]
    candidates: list[list[tuple[str, int]]] = []
    for pos, (item, quantity) in enumerate(items):
        if item in prices:
            continue
        fixed_part = sum(
            prices[name] * qty
            for idx, (name, qty) in enumerate(items)
            if idx != pos and name in prices
        )
        for candidate_name, candidate_price in prices.items():
            candidate_total = fixed_part + candidate_price * quantity
            if abs(candidate_total - float(target_price)) <= 1e-6:
                candidate_items = items.copy()
                candidate_items[pos] = (candidate_name, quantity)
                candidates.append(candidate_items)
    if len(candidates) != 1:
        raise ValueError(
            f"Expected one item-name correction for {items!r}, found {len(candidates)}"
        )
    return candidates[0]


class RoadNetwork:
    def __init__(self, nodes_path: Path, edges_path: Path) -> None:
        self.nodes = read_csv(nodes_path)
        self.edges = read_csv(edges_path)
        self.coord_to_node = {
            (round(float(row.lat), 7), round(float(row.lon), 7)): int(row.node)
            for row in self.nodes.itertuples(index=False)
        }
        self.node_to_coord = {
            int(row.node): (float(row.lat), float(row.lon))
            for row in self.nodes.itertuples(index=False)
        }
        self.shortest_paths = self._compute_branch_shortest_paths()

    def _compute_branch_shortest_paths(self) -> dict[str, dict[int, float]]:
        if nx is not None:
            graph = nx.Graph()
            for u, v, distance in zip(
                self.edges["u"], self.edges["v"], self.edges["distance(m)"]
            ):
                graph.add_edge(int(u), int(v), weight=float(distance))
            return {
                branch: nx.single_source_dijkstra_path_length(
                    graph, node, weight="weight"
                )
                for branch, node in BRANCH_NODES.items()
            }

        adjacency: dict[int, list[tuple[int, float]]] = {}
        for u, v, distance in zip(
            self.edges["u"], self.edges["v"], self.edges["distance(m)"]
        ):
            u_int, v_int, weight = int(u), int(v), float(distance)
            adjacency.setdefault(u_int, []).append((v_int, weight))
            adjacency.setdefault(v_int, []).append((u_int, weight))
        return {
            branch: self._dijkstra(adjacency, node)
            for branch, node in BRANCH_NODES.items()
        }

    @staticmethod
    def _dijkstra(
        adjacency: dict[int, list[tuple[int, float]]], source: int
    ) -> dict[int, float]:
        distances: dict[int, float] = {source: 0.0}
        heap: list[tuple[float, int]] = [(0.0, source)]
        while heap:
            current_distance, node = heapq.heappop(heap)
            if current_distance > distances[node]:
                continue
            for neighbour, weight in adjacency.get(node, []):
                candidate = current_distance + weight
                if candidate < distances.get(neighbour, float("inf")):
                    distances[neighbour] = candidate
                    heapq.heappush(heap, (candidate, neighbour))
        return distances

    def find_customer_node(self, lat: float, lon: float) -> tuple[int, float, float]:
        """Return the graph node and normalized coordinates for exact/fix candidates."""
        candidates = (
            (lat, lon),
            (-lat, lon),
            (lon, lat),
            (lon, -lat),
            (-lon, lat),
            (lat, -lon),
            (-lat, -lon),
        )
        for candidate_lat, candidate_lon in candidates:
            key = (round(float(candidate_lat), 7), round(float(candidate_lon), 7))
            if key in self.coord_to_node:
                node = self.coord_to_node[key]
                clean_lat, clean_lon = self.node_to_coord[node]
                return node, clean_lat, clean_lon
        raise ValueError(f"No graph node matched customer coordinate {(lat, lon)!r}")

    def distance_km(self, branch_code: str, lat: float, lon: float) -> float:
        node, _, _ = self.find_customer_node(float(lat), float(lon))
        metres = self.shortest_paths[branch_code][node]
        return round(metres / 1000.0, 3)


def add_fee_features(df: pd.DataFrame) -> pd.DataFrame:
    featured = df.copy()
    featured["date_dt"] = pd.to_datetime(featured["date"], format="%Y-%m-%d")
    featured["weekend"] = featured["date_dt"].dt.dayofweek.isin([5, 6]).astype(int)
    featured["time_code"] = featured["time"].map(meal_from_time).map(TIME_CODE)
    return featured


def adjusted_fee(df: pd.DataFrame) -> pd.Series:
    return df["delivery_fee"].astype(float).where(
        df["customerHasloyalty?"].eq(0), df["delivery_fee"].astype(float) * 2.0
    )


def fit_fee_models(
    df: pd.DataFrame,
    train_mask: pd.Series | None = None,
) -> tuple[dict[str, LinearRegression], list[FeeModelReport]]:
    featured = add_fee_features(df)
    if train_mask is None:
        train_mask = featured["delivery_fee"].notna()
    models: dict[str, LinearRegression] = {}
    reports: list[FeeModelReport] = []
    for branch_code, group in featured.loc[train_mask].groupby("branch_code"):
        x = group[["weekend", "time_code", "distance_to_customer_KM"]].to_numpy(float)
        y = adjusted_fee(group).to_numpy(float)
        model = LinearRegression().fit(x, y)
        predictions = model.predict(x)
        residuals = y - predictions
        models[branch_code] = model
        reports.append(
            FeeModelReport(
                branch_code=branch_code,
                rows=len(group),
                r2=float(model.score(x, y)),
                intercept=float(model.intercept_),
                coefficients={
                    "weekend": float(model.coef_[0]),
                    "time_code": float(model.coef_[1]),
                    "distance_to_customer_KM": float(model.coef_[2]),
                },
                residual_mean=float(np.mean(residuals)),
                residual_std=float(np.std(residuals, ddof=0)),
            )
        )
    return models, reports


def predict_fee(row: pd.Series, model: LinearRegression) -> float:
    meal_type = meal_from_time(row["time"])
    date_value = pd.to_datetime(row["date"], format="%Y-%m-%d")
    x = np.array(
        [
            [
                int(date_value.dayofweek in [5, 6]),
                TIME_CODE[meal_type],
                float(row["distance_to_customer_KM"]),
            ]
        ],
        dtype=float,
    )
    predicted = float(model.predict(x)[0])
    if int(row["customerHasloyalty?"]) == 1:
        predicted /= 2.0
    return round(predicted, 6)


def clean_dirty_data(df: pd.DataFrame, network: RoadNetwork) -> tuple[pd.DataFrame, dict[str, int]]:
    cleaned = df.copy()
    repairs = {
        "date": 0,
        "order_type": 0,
        "branch_code": 0,
        "order_items": 0,
        "order_price": 0,
        "customer_coordinates": 0,
        "distance_to_customer_KM": 0,
        "unchanged": 0,
    }

    for idx, row in cleaned.iterrows():
        expected_date = normalize_date(row["date"])
        if expected_date is None:
            raise ValueError(f"Could not parse date {row['date']!r} at row {idx}")
        if row["date"] != expected_date:
            cleaned.at[idx, "date"] = expected_date
            repairs["date"] += 1
            continue

        expected_type = meal_from_time(row["time"])
        if row["order_type"] != expected_type:
            cleaned.at[idx, "order_type"] = expected_type
            repairs["order_type"] += 1
            continue

        expected_branch = branch_from_order_id(row["order_id"])
        if row["branch_code"] != expected_branch:
            cleaned.at[idx, "branch_code"] = expected_branch
            repairs["branch_code"] += 1
            continue

        items = parse_items(row["order_items"])
        if not valid_menu_items(items, expected_type):
            fixed_items = correct_wrong_item_name(
                items, expected_type, float(row["order_price"])
            )
            cleaned.at[idx, "order_items"] = format_items(fixed_items)
            repairs["order_items"] += 1
            continue

        expected_price = order_total(items, expected_type)
        if abs(float(row["order_price"]) - expected_price) > 1e-6:
            cleaned.at[idx, "order_price"] = expected_price
            repairs["order_price"] += 1
            continue

        _, clean_lat, clean_lon = network.find_customer_node(
            float(row["customer_lat"]), float(row["customer_lon"])
        )
        if (
            abs(float(row["customer_lat"]) - clean_lat) > 1e-9
            or abs(float(row["customer_lon"]) - clean_lon) > 1e-9
        ):
            cleaned.at[idx, "customer_lat"] = clean_lat
            cleaned.at[idx, "customer_lon"] = clean_lon
            repairs["customer_coordinates"] += 1
            continue

        expected_distance = network.distance_km(
            expected_branch, float(row["customer_lat"]), float(row["customer_lon"])
        )
        if abs(float(row["distance_to_customer_KM"]) - expected_distance) > 1e-6:
            cleaned.at[idx, "distance_to_customer_KM"] = expected_distance
            repairs["distance_to_customer_KM"] += 1
            continue

        repairs["unchanged"] += 1

    return cleaned, repairs


def impute_missing_data(
    df: pd.DataFrame, network: RoadNetwork
) -> tuple[pd.DataFrame, dict[str, int], list[FeeModelReport]]:
    cleaned = df.copy()
    repairs = {
        "branch_code": int(cleaned["branch_code"].isna().sum()),
        "distance_to_customer_KM": int(cleaned["distance_to_customer_KM"].isna().sum()),
        "delivery_fee": int(cleaned["delivery_fee"].isna().sum()),
    }

    missing_branch = cleaned["branch_code"].isna()
    cleaned.loc[missing_branch, "branch_code"] = cleaned.loc[missing_branch, "order_id"].map(
        branch_from_order_id
    )

    missing_distance = cleaned["distance_to_customer_KM"].isna()
    for idx, row in cleaned.loc[missing_distance].iterrows():
        cleaned.at[idx, "distance_to_customer_KM"] = network.distance_km(
            row["branch_code"], float(row["customer_lat"]), float(row["customer_lon"])
        )

    models, reports = fit_fee_models(cleaned, cleaned["delivery_fee"].notna())
    missing_fee = cleaned["delivery_fee"].isna()
    for idx, row in cleaned.loc[missing_fee].iterrows():
        cleaned.at[idx, "delivery_fee"] = predict_fee(row, models[row["branch_code"]])

    return cleaned, repairs, reports


def detect_delivery_fee_outliers(
    df: pd.DataFrame, max_iterations: int = 8
) -> tuple[set[int], list[FeeModelReport], dict[str, int]]:
    featured = add_fee_features(df)
    featured["adjusted_fee"] = adjusted_fee(featured)
    outlier_indices: set[int] = set()
    per_branch_counts: dict[str, int] = {}
    reports: list[FeeModelReport] = []

    for branch_code, group in featured.groupby("branch_code", sort=True):
        x_all = group[["weekend", "time_code", "distance_to_customer_KM"]].to_numpy(float)
        y_all = group["adjusted_fee"].to_numpy(float)
        keep = np.ones(len(group), dtype=bool)
        model = LinearRegression()

        for _ in range(max_iterations):
            model.fit(x_all[keep], y_all[keep])
            residuals_all = y_all - model.predict(x_all)
            residuals_keep = residuals_all[keep]
            q1, q3 = np.percentile(residuals_keep, [25, 75])
            iqr = q3 - q1
            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr
            new_keep = (residuals_all >= lower) & (residuals_all <= upper)
            if np.array_equal(new_keep, keep):
                break
            keep = new_keep

        model.fit(x_all[keep], y_all[keep])
        residuals = y_all[keep] - model.predict(x_all[keep])
        reports.append(
            FeeModelReport(
                branch_code=branch_code,
                rows=int(keep.sum()),
                r2=float(model.score(x_all[keep], y_all[keep])),
                intercept=float(model.intercept_),
                coefficients={
                    "weekend": float(model.coef_[0]),
                    "time_code": float(model.coef_[1]),
                    "distance_to_customer_KM": float(model.coef_[2]),
                },
                residual_mean=float(np.mean(residuals)),
                residual_std=float(np.std(residuals, ddof=0)),
            )
        )

        branch_outliers = group.index[~keep].tolist()
        outlier_indices.update(int(idx) for idx in branch_outliers)
        per_branch_counts[branch_code] = len(branch_outliers)

    return outlier_indices, reports, per_branch_counts


def remove_outliers(df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, int], list[FeeModelReport]]:
    outlier_indices, reports, per_branch_counts = detect_delivery_fee_outliers(df)
    cleaned = df.drop(index=sorted(outlier_indices)).copy()
    return cleaned, per_branch_counts, reports


def assert_columns_and_shape(
    original: pd.DataFrame, result: pd.DataFrame, name: str, same_rows: bool
) -> None:
    if list(original.columns) != list(result.columns):
        raise AssertionError(f"{name}: output columns do not match input columns")
    if same_rows and len(original) != len(result):
        raise AssertionError(f"{name}: row count changed unexpectedly")


def validate_structural_rules(df: pd.DataFrame, network: RoadNetwork, name: str) -> dict[str, object]:
    invalid_rows: list[int] = []
    for idx, row in df.iterrows():
        expected_date = normalize_date(row["date"])
        if row["date"] != expected_date:
            invalid_rows.append(idx)
            continue
        expected_type = meal_from_time(row["time"])
        expected_branch = branch_from_order_id(row["order_id"])
        items = parse_items(row["order_items"])
        expected_price = order_total(items, expected_type)
        expected_distance = network.distance_km(
            expected_branch, float(row["customer_lat"]), float(row["customer_lon"])
        )
        if (
            row["order_type"] != expected_type
            or row["branch_code"] != expected_branch
            or not valid_menu_items(items, expected_type)
            or abs(float(row["order_price"]) - expected_price) > 1e-6
            or abs(float(row["distance_to_customer_KM"]) - expected_distance) > 1e-6
        ):
            invalid_rows.append(idx)
    if invalid_rows:
        raise AssertionError(f"{name}: structural rules failed at rows {invalid_rows[:10]}")
    return {
        "rows": len(df),
        "missing_cells": int(df.isna().sum().sum()),
        "valid_branch_codes": sorted(df["branch_code"].unique().tolist()),
        "valid_order_types": sorted(df["order_type"].unique().tolist()),
    }


def validate_dirty_protection(original: pd.DataFrame, cleaned: pd.DataFrame) -> None:
    for column in PROTECTED_DIRTY_COLUMNS:
        if not original[column].equals(cleaned[column]):
            raise AssertionError(f"Dirty protected column {column!r} was modified")
    for idx in original.index:
        before_items = parse_items(original.at[idx, "order_items"])
        after_items = parse_items(cleaned.at[idx, "order_items"])
        before_quantities = [quantity for _, quantity in before_items]
        after_quantities = [quantity for _, quantity in after_items]
        if before_quantities != after_quantities:
            raise AssertionError(f"Dirty item quantities changed at row {idx}")


def validate_outputs(
    dirty_original: pd.DataFrame,
    missing_original: pd.DataFrame,
    outlier_original: pd.DataFrame,
    network: RoadNetwork,
) -> dict[str, dict[str, object]]:
    dirty = read_csv(DIRTY_OUTPUT)
    missing = read_csv(MISSING_OUTPUT)
    outlier = read_csv(OUTLIER_OUTPUT)

    assert_columns_and_shape(dirty_original, dirty, "dirty", same_rows=True)
    assert_columns_and_shape(missing_original, missing, "missing", same_rows=True)
    assert_columns_and_shape(outlier_original, outlier, "outlier", same_rows=False)
    validate_dirty_protection(dirty_original, dirty)

    dirty_report = validate_structural_rules(dirty, network, "dirty")
    missing_report = validate_structural_rules(missing, network, "missing")
    outlier_report = validate_structural_rules(outlier, network, "outlier")

    if missing.isna().sum().sum() != 0:
        raise AssertionError("missing output still contains missing values")
    if len(outlier) >= len(outlier_original):
        raise AssertionError("outlier output did not remove any rows")

    return {
        "dirty": dirty_report,
        "missing": missing_report,
        "outlier": {
            **outlier_report,
            "rows_removed": len(outlier_original) - len(outlier),
        },
    }


def write_solution(df: pd.DataFrame, path: Path) -> None:
    df.to_csv(path, index=False)


def run_all(verbose: bool = True) -> Task1Results:
    dirty_original = read_csv(DIRTY_INPUT)
    missing_original = read_csv(MISSING_INPUT)
    outlier_original = read_csv(OUTLIER_INPUT)
    _ = read_csv(BRANCHES_INPUT)
    network = RoadNetwork(NODES_INPUT, EDGES_INPUT)

    dirty_solution, dirty_repairs = clean_dirty_data(dirty_original, network)
    missing_solution, missing_repairs, missing_reports = impute_missing_data(
        missing_original, network
    )
    outlier_solution, outlier_removed, outlier_reports = remove_outliers(outlier_original)

    write_solution(dirty_solution, DIRTY_OUTPUT)
    write_solution(missing_solution, MISSING_OUTPUT)
    write_solution(outlier_solution, OUTLIER_OUTPUT)

    validation = validate_outputs(
        dirty_original, missing_original, outlier_original, network
    )

    results = Task1Results(
        dirty_repairs=dirty_repairs,
        missing_repairs=missing_repairs,
        missing_model_reports=missing_reports,
        outlier_removed=outlier_removed,
        outlier_model_reports=outlier_reports,
        validation=validation,
    )
    if verbose:
        print_results(results)
    return results


def print_model_reports(title: str, reports: list[FeeModelReport]) -> None:
    print(title)
    for report in sorted(reports, key=lambda item: item.branch_code):
        print(
            f"  {report.branch_code}: n={report.rows}, R2={report.r2:.4f}, "
            f"residual_mean={report.residual_mean:.6f}, residual_std={report.residual_std:.6f}, "
            f"coef={report.coefficients}"
        )


def print_results(results: Task1Results) -> None:
    print("Dirty-data repairs:", results.dirty_repairs)
    print("Missing-data imputations:", results.missing_repairs)
    print_model_reports("Missing delivery-fee model diagnostics:", results.missing_model_reports)
    print("Outlier rows removed by branch:", results.outlier_removed)
    print_model_reports("Outlier retained-row model diagnostics:", results.outlier_model_reports)
    print("Read-back validation:", results.validation)


if __name__ == "__main__":
    run_all(verbose=True)
