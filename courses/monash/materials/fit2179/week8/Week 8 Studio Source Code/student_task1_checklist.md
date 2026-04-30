# Task 1 — Symbol Map Checklist

Objective: Change the symbol map encodings so `color = mag`, `size = dmin`, add `shape = locationSource`, and verify the visualization.

Steps:

1. Open `js/symbol_map.vg.json` in the `2_symbol_map` folder.
2. Set the mark to `"point"`:

```json
"mark": { "type": "point", "tooltip": { "content": "data" } }
```

3. Update encodings:

```json
"color": { "field": "mag", "type": "quantitative" },
"size":  { "field": "dmin", "type": "quantitative" },
"shape": { "field": "locationSource", "type": "nominal" }
```

4. If you get a warning about shapes or have more categories than shapes, add an explicit shape scale:

```json
"shape": {
  "field": "locationSource",
  "type": "nominal",
  "scale": { "domain": ["us", "ak"], "range": ["circle", "cross"] }
}
```

5. Open `index.html` for `2_symbol_map` and check:
- Colors reflect `mag` values.
- Sizes reflect `dmin` values.
- Shapes differ by `locationSource` (or follow the explicit mapping).
- No Vega/Vega-Lite schema warnings in the browser console.

Deliverable: Save one screenshot showing the map and a hovered tooltip with `mag`, `dmin`, and `locationSource` values.
