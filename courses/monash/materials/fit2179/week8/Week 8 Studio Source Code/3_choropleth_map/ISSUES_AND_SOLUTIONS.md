# Choropleth Map Issues & Solutions

## Issue 1: Blank Countries (Missing Data)

### What Could Cause This?

#### **1. Country Name Mismatch (Most Common Cause)**
The TopoJSON file (geographic boundaries) and the CSV data file use different country names:

**Example:** Congo appears blank on the map
- **TopoJSON might contain:** "Democratic Republic of the Congo" or "Congo"
- **CSV contains:** "Congo (Kinshasa)" 
- **Lookup fails** → No match → Country appears white/blank

When Vega-Lite performs a `lookup` transform with `properties.NAME`, it tries to match:
```
properties.NAME (from TopoJSON) == Country (from CSV)
```
If these don't match exactly, the lookup returns `null`, and no color is assigned.

#### **2. Missing Data**
Some countries might not have COVID-19 data recorded in the CSV file at all.

#### **3. No Data vs. Zero Cases**
- A blank country could mean "no data available"
- But we don't distinguish between "0 cases" and "no data" visually

---

### What Is the Best Way to Handle This?

#### **Solution 1: Fix the Country Name Mismatch (Recommended)**

**Step 1:** Identify which countries are blank
- Compare TopoJSON country names with CSV country names
- Create a mapping file for mismatches

**Step 2:** Create a name mapping/matching strategy
```json
{
  "lookup": "properties.NAME",
  "from": {
    "data": {"url": "...covid_10_10_2020.csv"},
    "key": "Country",
    "fields": ["Active"]
  }
}
```

**Step 3:** Use data transformation to standardize names
- Option A: Clean the CSV before loading
- Option B: Use a lookup table with name mappings
- Option C: Modify the data on-the-fly with `transform`

#### **Solution 2: Display Blank Countries Differently**

Distinguish between "no data" and "data available":

```json
"color": {
  "condition": {
    "test": "datum.Active == null",
    "value": "#d3d3d3"  // Light gray for no data
  },
  "field": "Active Cases",
  "type": "quantitative",
  "scale": {"type": "log"}
}
```

This shows:
- **Light gray** = No data available
- **Blue gradient** = Data available

#### **Solution 3: Add Stroke/Border to Highlight Missing Data**

```json
"stroke": {
  "condition": {
    "test": "datum.Active == null",
    "value": "red"  // Red border for no data
  },
  "value": "white"
}
```

#### **Solution 4: Use Tooltips to Explain**

```json
"tooltip": [
  {"field": "properties.NAME", "type": "nominal", "title": "Country"},
  {
    "condition": {"test": "datum.Active == null", "value": "No data available"},
    "field": "Active",
    "type": "quantitative"
  }
]
```

---

## Issue 2: Same Color for Neighboring Countries

### Why Is This a Problem?

1. **Loss of Visual Distinction**
   - Adjacent countries with similar values blend together
   - Impossible to distinguish one country from its neighbors
   - Reduces readability and analysis

2. **Choropleth Limitation**
   - Continuous color scales naturally produce similar colors for similar values
   - Countries grouped by value (e.g., 1000-2000 cases) get same hue
   - Geography + data values = colors don't align well with geography

3. **Example from Map:**
   - Multiple African countries with similar blue shades
   - West African region appears as a uniform color band
   - Can't see individual country boundaries clearly

---

### What Could Be Done to Fix This?

#### **Solution 1: Add Borders/Strokes (Quick Fix)**

Make borders darker or colored to separate regions:

```json
"mark": {"type": "geoshape", "stroke": "black", "strokeWidth": 2}
```

**Pros:**
- Simple to implement
- Works immediately
- Doesn't change data encoding

**Cons:**
- Borders can be distracting
- Small countries might be hidden by thick borders

#### **Solution 2: Use a Different Color Scale (Better)**

Switch from a single hue (blue) to a **diverging color scale**:

```json
"color": {
  "field": "Active Cases",
  "type": "quantitative",
  "scale": {"scheme": "redblue"}  // or "viridis", "plasma", "turbo"
}
```

**Better color schemes:**
- `viridis` - Perceptually uniform, colorblind-friendly
- `turbo` - More color variety
- `diverging` - Shows positive/negative values
- `spectral` - Warm to cool colors

#### **Solution 3: Reduce Color Scale Range (Binning)**

Instead of a continuous scale, use discrete bins:

```json
"color": {
  "field": "Active Cases",
  "type": "ordinal",
  "scale": {
    "scheme": "blues",
    "type": "ordinal"
  }
}
```

Or manually define bins:
```json
"color": {
  "field": "Active Cases",
  "type": "ordinal",
  "scale": {
    "domain": ["0-1000", "1000-5000", "5000-10000", "10000+"],
    "range": ["#f1eef6", "#bdc9e1", "#74a9cf", "#0570b0"]
  }
}
```

**Pros:**
- Clear visual separation between bins
- Easier to distinguish neighboring countries
- Reduces perceived "smoothness" that hides boundaries

**Cons:**
- Loses granularity of data
- Must choose appropriate bin sizes

#### **Solution 4: Use Contour/Interpolation Lines**

Add contour lines to show data gradients:

```json
"layer": [
  {
    "mark": "geoshape",
    // ... choropleth ...
  },
  {
    "mark": "line",
    // Add contour lines for continuous data
  }
]
```

#### **Solution 5: Small Multiples / Faceting**

Create separate maps for different regions:

```json
"facet": {"field": "Region", "type": "nominal"},
"spec": {
  // Individual choropleth for each region
}
```

#### **Solution 6: Add Outlines/Contours Underneath**

Create a base map with strong borders, then overlay choropleth:

```json
"layer": [
  {
    "data": {"url": "topojson"},
    "mark": {"type": "geoshape", "fill": "white", "stroke": "black", "strokeWidth": 1.5}
  },
  {
    "data": {"url": "csv"},
    "mark": {"type": "geoshape", "stroke": "none"},
    // Color encoding with data
  }
]
```

---

## Comparison of Solutions

| Solution | Effort | Effectiveness | Drawbacks |
|----------|--------|----------------|-----------|
| Add borders | ⭐ Easy | ⭐⭐ Moderate | Can be distracting |
| Better color scheme | ⭐⭐ Easy | ⭐⭐⭐ Good | Limited by data |
| Binned colors | ⭐⭐ Medium | ⭐⭐⭐⭐ Very good | Loses precision |
| Contour lines | ⭐⭐⭐ Hard | ⭐⭐⭐ Good | Complex to implement |
| Small multiples | ⭐⭐⭐ Hard | ⭐⭐⭐⭐ Excellent | Takes more space |
| Layered outlines | ⭐⭐ Medium | ⭐⭐⭐⭐ Excellent | Slightly more data |

---

## Recommended Implementation

### **For Blank Countries:**
1. **First:** Use conditional coloring to show "no data" in light gray
2. **Second:** Add tooltips explaining missing data
3. **Third:** Fix the data source if possible

### **For Same-Color Neighbors:**
1. **Quick fix:** Increase stroke width: `"strokeWidth": 1.5`
2. **Better fix:** Use viridis color scale: `"scheme": "viridis"`
3. **Best fix:** Combine binned colors with strong borders

---

## Example Implementation

Here's how to combine both solutions:

```json
{
  "mark": {"type": "geoshape", "stroke": "#333", "strokeWidth": 1.5},
  "encoding": {
    "color": {
      "condition": {
        "test": "datum.Active == null",
        "value": "#e0e0e0"
      },
      "field": "Active Cases",
      "type": "quantitative",
      "scale": {
        "type": "quantile",
        "scheme": "viridis"
      }
    },
    "tooltip": [
      {"field": "properties.NAME", "type": "nominal", "title": "Country"},
      {"field": "Active", "type": "quantitative", "title": "Active Cases"}
    ]
  }
}
```

This:
- ✅ Shows no-data countries in light gray
- ✅ Uses perceptually uniform "viridis" colors
- ✅ Adds dark borders to separate countries
- ✅ Uses quantile scaling for better distribution
