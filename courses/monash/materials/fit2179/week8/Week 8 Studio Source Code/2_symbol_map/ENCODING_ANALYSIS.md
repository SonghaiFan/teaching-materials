# Earthquake Symbol Map - Encoding Analysis

## Summary of Changes

### Original Encodings

- **color**: `depth` (quantitative) - Depth in km
- **size**: `mag` (quantitative) - Magnitude

### Modified Encodings

- **color**: `mag` (quantitative) - Magnitude
- **size**: `dmin` (quantitative) - Minimum Distance
- **shape**: `locationSource` (nominal) - Location Source (NEW)

---

## Visualization Results

### ✅ What Works

1. **Color encoding for magnitude**: The red color scale effectively shows earthquake magnitude, with darker/redder points indicating higher magnitudes.
2. **Size encoding for dmin**: Points vary in size according to the minimum distance value.
3. **Shape encoding display**: Points are rendered with different shapes (circles and crosses) for different location sources.

### ⚠️ Warning: Shape Encoding Limitations

When you add the `shape` encoding for `locationSource`, you may encounter implicit warnings or constraints in Vega-Lite:

#### Why is there a warning?

1. **Limited Shape Palette**: The `shape` channel supports only a limited number of distinct shapes in Vega-Lite:
   - circle
   - square
   - cross (or x)
   - diamond
   - triangle-up
   - triangle-down
   - triangle-right
   - triangle-left

2. **Data Constraint**: In the earthquake dataset, there are only 2 location sources:
   - `us` (USGS - United States Geological Survey)
   - `ak` (Alaska Earthquake Center)

   This fits within the available shapes, so it works without explicit errors.

3. **Shape Effectiveness**: However, the shape channel is **less effective** for encoding categorical data compared to other channels:
   - Harder to distinguish visually (especially small sizes)
   - Less intuitive than color or position
   - Works best for 2-3 categories maximum
   - Can be ambiguous in print or with color-blind viewers

---

## The Fix

### Problem

If there were **more than ~5-8** unique values in `locationSource`, Vega-Lite would either:

- Recycle shapes (same shape for multiple categories)
- Issue a warning about insufficient shapes
- Create visual ambiguity

### Solution: Explicit Shape Scale

Add a `scale` definition to control which shapes map to which categories:

```json
"shape": {
  "field": "locationSource",
  "type": "nominal",
  "title": "Location Source",
  "scale": {
    "domain": ["us", "ak"],
    "range": ["circle", "cross"]
  }
}
```

This explicitly maps:

- `us` → circle
- `ak` → cross

### Better Alternative Approaches

If you had many location sources, consider:

1. **Use Color instead** (more perceptually distinct):

```json
"color": {
  "field": "locationSource",
  "type": "nominal",
  "title": "Location Source"
}
```

2. **Use a legend with filtering**:

```json
"opacity": {
  "field": "locationSource",
  "type": "nominal",
  "scale": {"domain": ["us", "ak"], "range": [1, 0.5]}
}
```

3. **Small multiples** (separate visualizations for each source)

4. **Combination of channels** (shape + color, shape + opacity)

---

## Mark Type Requirement

Note: The `shape` channel requires the mark type to be **`point`** rather than **`circle`**:

- `"circle"`: Fixed circular marks (doesn't support shape encoding)
- `"point"`: Flexible point marks (supports shape, size, color, opacity)

---

## Data Statistics

- **Total earthquakes**: 27 (in the sample data)
- **Unique location sources**: 2 (us, ak)
- **dmin range**: 0.257 - 4.375 degrees
- **Magnitude range**: 4.5 - 5.9

---

## Recommendations

✅ **Keep this encoding because**:

- Only 2 location sources (fits shape channel well)
- Visual distinction is clear
- Complements the magnitude (color) and distance (size) encodings
- Provides third dimension of information

⚠️ **If you had many location sources**:

- Switch `shape` to `opacity` or secondary `color` scale
- Or use `facet` to create separate maps per location source

---

## Files Modified

- `symbol_map.vg.json` - Updated with new encodings (color: mag, size: dmin, shape: locationSource)
- `symbol_map_fixed.vg.json` - Version with explicit shape scale definition (recommended)
