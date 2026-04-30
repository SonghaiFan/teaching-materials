# Task 2 — Choropleth Issues & Fixes Checklist

Objective: Diagnose blank countries and improve neighbour distinguishability on the choropleth map.

Steps:

1. Open `js/choropleth_map.vg.json` and `data/covid_10_10_2020.csv` in the `3_choropleth_map` folder.
2. Inspect the `lookup` transform: it matches `properties.NAME` (TopoJSON) to CSV `Country`.
   - Create a short list of mismatches (e.g., `Congo (Kinshasa)` vs `Democratic Republic of the Congo`).
3. Short-term visual fix: add conditional color for missing data:

```json
"color": {
  "condition": { "test": "datum.Active == null", "value": "#d3d3d3" },
  "field": "Active Cases",
  "type": "quantitative"
}
```

4. Improve neighbour distinction (choose one or combine):
- Add borders: `"mark": { "type": "geoshape", "stroke": "#333", "strokeWidth": 1.2 }`.
- Use a perceptually-uniform scheme: `"scale": { "scheme": "viridis" }`.
- Bin the data into categories and encode color as nominal (recommended for clarity).

5. Validate in `analysis.html` or `index.html` in the `3_choropleth_map` folder:
- Previously blank countries appear gray with tooltip saying "No data".
- Neighbouring countries are visually separable.

Deliverable: One-paragraph report listing mismatched country names found, which fix you applied, and a screenshot of the improved map.
