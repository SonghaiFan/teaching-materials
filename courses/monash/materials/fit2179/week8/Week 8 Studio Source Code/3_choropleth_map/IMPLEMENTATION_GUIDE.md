# Choropleth Map: Practical Implementation Guide

## Quick Reference: The Two Main Problems & Solutions

### Problem 1: Blank Countries (White/No Color)

**Root Cause:** Country name mismatch in the lookup transform

```
TopoJSON: "Congo"
CSV: "Congo (Kinshasa)"
Result: ❌ No match → datum.Active = null → White color
```

**Simplest Fix - Add Conditional Color:**
```json
"color": {
  "condition": {
    "test": "datum.Active == null",
    "value": "#d3d3d3"  // Light gray = no data
  },
  "field": "Active Cases",
  "type": "quantitative"
}
```

**Complete Solution - Fix the Data:**
Create a mapping file or data transformation to match country names:
- Option A: Clean CSV before loading
- Option B: Add a lookup table
- Option C: Use Vega transform to standardize names

---

### Problem 2: Same-Color Neighbors (Indistinguishable Countries)

**Root Cause:** Continuous color scales produce too many similar shades

**Best Solution - Binned/Discretized Colors:**

```json
{
  "transform": [
    // ... existing transforms ...
    {
      "calculate": "datum.Active == null ? 'No Data' : datum.Active < 1000 ? '0-1K' : datum.Active < 5000 ? '1K-5K' : '5K+'",
      "as": "CasesBin"
    }
  ],
  "encoding": {
    "color": {
      "field": "CasesBin",
      "type": "nominal",  // ← KEY: use nominal, not quantitative
      "scale": {
        "domain": ["No Data", "0-1K", "1K-5K", "5K+"],
        "range": ["#e0e0e0", "#f1eef6", "#bdc9e1", "#08519c"]
      }
    }
  }
}
```

**Key Difference:**
- `type: "quantitative"` → Continuous gradient (many similar shades)
- `type: "nominal"` → Discrete categories (distinct colors)

---

## Step-by-Step Implementation

### Step 1: Add Better Borders (5 minutes)
Helps distinguish countries even with same colors:
```json
"mark": {"type": "geoshape", "stroke": "#333", "strokeWidth": 1.5}
```

### Step 2: Highlight Missing Data (5 minutes)
Show users which countries have no data:
```json
"condition": {
  "test": "datum.Active == null",
  "value": "#d3d3d3"
}
```

### Step 3: Create Bins (15 minutes)
Add a calculate transform to your spec:
```json
{
  "calculate": "datum.Active == null ? 'No Data' : datum.Active < 1000 ? '0-1K' : datum.Active < 5000 ? '1K-5K' : datum.Active < 20000 ? '5K-20K' : '20K+'",
  "as": "CasesBin"
}
```

### Step 4: Update Color Encoding (5 minutes)
Change from `quantitative` to `nominal`:
```json
"color": {
  "field": "CasesBin",        // ← Use new binned field
  "type": "nominal",           // ← Change from quantitative
  "scale": {
    "domain": ["No Data", "0-1K", "1K-5K", "5K-20K", "20K+"],
    "range": ["#efefef", "#f7fbff", "#c6dbef", "#6baed6", "#08519c"]
  }
}
```

**Total Implementation Time: ~30 minutes**

---

## Common Questions & Answers

### Q: Will binning lose information?
**A:** Yes, slightly. A country with 4,999 cases looks same as one with 1,000 cases (both in "1K-5K"). But this is acceptable because:
- Viewers can't distinguish 50+ colors anyway
- The patterns are still clear (outbreak regions stand out)
- This is standard practice in choropleth design

### Q: How do I choose bin sizes?
**A:** Use data-driven bins:
```
- Look at your data distribution
- Use quantiles (equal number of countries per bin)
- Or use meaningful ranges (e.g., powers of 10, thresholds)

Option 1 (Data-driven):
0-500, 500-2000, 2000-10000, 10000-50000, 50000+

Option 2 (Meaningful):
No Outbreak, Low, Medium, High, Critical
```

### Q: Why is viridis better than my blue scale?
**A:**
- **Blue scale:** Similar shades, hard to distinguish (colorblind-unfriendly)
- **Viridis:** Perceptually uniform, designed for colorblind viewers
- **Trade-off:** Viridis uses more "rainbow" but is more distinguishable

Try: `"scheme": "viridis"` or `"scheme": "turbo"`

### Q: Should I fix country name mismatches?
**A:** **Yes, definitely** - this is the right way. But short-term:
1. Use gray for no-data to show the problem
2. Add tooltip explaining missing data
3. Fix the data source when possible

---

## Visual Debugging

### Check if your data loaded correctly:
```json
"tooltip": [
  {"field": "properties.NAME", "type": "nominal", "title": "Country"},
  {"field": "Active", "type": "quantitative", "title": "Active Cases"},
  {"calculate": "datum.Active == null ? 'NO DATA' : 'HAS DATA'", "title": "Status"}
]
```

Hover over countries to see which ones have/don't have data.

---

## Files You Now Have

1. **ISSUES_AND_SOLUTIONS.md** - Detailed explanation of both issues
2. **choropleth_improved_borders.vg.json** - Solution 1: Better borders + no-data highlighting
3. **choropleth_viridis.vg.json** - Solution 2: Better color scheme
4. **choropleth_binned.vg.json** - Solution 3: Binned colors (RECOMMENDED)
5. **analysis.html** - Interactive comparison of all solutions

---

## Teaching Discussion Points

Use these points when discussing with tutors and peers:

### About Blank Countries:
- "Data quality is critical - we need to verify all country names match"
- "Gray color is better than white because white looks like 'no answer' vs 'unknown'"
- "Always check the data first before blaming the visualization"

### About Same-Color Neighbors:
- "Continuous scales are nice but not always practical for maps"
- "Our eyes can distinguish ~5-7 distinct colors, not 50+ shades"
- "Binning trades precision for clarity - sometimes that's the right choice"
- "Map design is about trade-offs: accuracy vs clarity vs simplicity"

### Design Decisions:
- "Why did we choose these bin sizes?" (Discuss data distribution)
- "How many categories is too many?" (Cognitive load)
- "Is it better to be precise or clear?" (Iterative design)

---

## Next Steps

1. **Try all three solutions** - See which one your team prefers
2. **Fix the data** - Create a country name mapping file
3. **User test** - Show real users and get feedback
4. **Refine** - Based on feedback, adjust bin sizes, colors, labels

---

## Key Takeaway

The choice between continuous and binned colors is **not about right vs wrong** - it's about:
- **Purpose**: What story are you telling?
- **Audience**: What's their background?
- **Data**: What patterns matter?
- **Constraints**: Print? Web? Interactive?

A good choropleth adapts to these factors!
