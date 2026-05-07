---
theme: default
title: Data Visualisation Studio 9
layout: cover
info: |
  ## FIT2179 Week 9
  Interactive Charts with Vega-Lite
highlighter: shiki
drawings:
  persist: false
transition: slide-left
---

# FIT2179 Data Visualisation Week 9

Interactive Charts with Vega-Lite

Songhai Fan · Monash University

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Session plan</p>

# Today's agenda

| Time | Focus |
|---|---|
| 0 – 10 min | `DV1` debrief and general feedback |
| 10 min – 1.5 hr | Interactive Charts with `Vega-Lite` |
| Remaining time | `Vega-Lite` help session and FAQs |

> Today is hands-on. We open with a quick debrief, build one chart step by step, then use remaining time to answer your questions.

---
layout: section
---

# DV1 Debrief

0 – 10 min

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">DV1 debrief · 0 – 10 min</p>

# General feedback

<VClicks>

- What did students do well overall?
- Common things that were missed or overlooked — share with the group.
- Any patterns in the submissions worth discussing?

</VClicks>

## Grade queries

If a student wants to discuss their individual mark, ask them to **send a query via email** rather than discussing it in the studio session.

---
layout: section
---

# Part 1 — Interactive Bubble Plot

Building step by step

---
layout: two-cols
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">1.0 Dataset</p>

# What we are visualising

Country-level COVID-19 statistics as of **10 Oct 2020** — one row per country.

| Field | Description |
|---|---|
| `Confirmed` | Total confirmed cases |
| `Deaths` | Total deaths |
| `Active` | Active cases |
| `Population` | Country population |
| `Continent` | Continent name |

::right::

## Four attributes → four visual channels

| Channel | Field |
|---|---|
| X position | `Confirmed` cases |
| Y position | `Deaths` |
| Colour | `Continent` |
| Size (area) | `Population` |

---
layout: statement
---

A bubble plot encodes **three or four variables** simultaneously — position (X, Y), size, and colour.

Most charts only encode two.

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">1.1 Minimal spec</p>

# Start: the basic bubble plot

<VegaLitePlayground
  title="Basic Bubble Plot"
  :height="300"
  :initialSpec="{
    '$schema': 'https://vega.github.io/schema/vega-lite/v5.json',
    'width': 200,
    'height': 260,
    'title': 'COVID-19 Cases per Country (13 Oct 2020)',
    'data': {
      'url': 'https://raw.githubusercontent.com/FIT3179/Vega-Lite/main/4_interactive_scatter_plot/data/COVID_19_10_Oct_2020.csv'
    },
    'mark': 'circle',
    'encoding': {
      'x': {
        'field': 'Confirmed',
        'type': 'quantitative',
        'title': 'Confirmed Cases'
      },
      'y': {
        'field': 'Deaths',
        'type': 'quantitative'
      },
      'color': {
        'field': 'Continent',
        'type': 'nominal'
      },
      'size': {
        'field': 'Population',
        'type': 'quantitative'
      }
    }
  }"
/>

---
layout: two-cols
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">1.2 Log scale axes</p>

# Problem: data clusters in one corner

The US, Brazil, and India dominate. Most countries are squashed at the bottom-left.

**Solution: log scale on both axes.**


```json
"transform": [
  { "filter": "datum.Active > 0" },
  { "filter": "datum.Deaths > 0" }
]
```


> Log scale does not work with zero or negative values.

::right::

```json {all|4-5|6-9|all}
"x": {
  "field": "Confirmed",
  "type": "quantitative",
  "title": "Confirmed Cases",
  "axis": { "tickCount": 7 },
  "scale": {
    "type": "log",
    "domain": [1, 10000000]
  }
},
"y": {
  "field": "Deaths",
  "type": "quantitative",
  "axis": { "tickCount": 6 },
  "scale": {
    "type": "log",
    "domain": [1, 1000000]
  }
}
```

---
layout: two-cols
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">1.3 Size scale</p>

# Classify population into buckets

Replace the continuous size scale with a **threshold scale**.

## Threshold scale
Five thresholds → six classes. Each maps to a fixed pixel² area.


## SI format `.1s`
- `1000000` → `1M` 
- `500000000` → `500M`

::right::

```json {all|3|4-8|9|all}
"size": {
  "field": "Population",
  "type": "quantitative",
  "scale": {
    "type": "threshold",
    "domain": [
      1000000, 10000000,
      50000000, 100000000, 500000000
    ],
    "range": [10, 50, 150, 200, 300, 400]
  },
  "legend": { "format": ".1s" }
}
```

---
layout: two-cols
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">1.4 Colour scale</p>

# Custom palette from ColorBrewer

Choose one colour per continent. Add **opacity** to reduce clutter when bubbles overlap.

> Pick palettes from **colorbrewer2.org**. Aim for colours that are distinct even for colour-blind viewers — use the "colorblind safe" filter.

::right::

```json {all|3-13}
"color": {
  "field": "Continent",
  "type": "nominal",
  "scale": {
    "domain": [
      "North America", "South America",
      "Europe", "Africa",
      "Asia", "Oceania"
    ],
    "range": [
      "#e41a1c", "#984ea3",
      "#ff7f00", "#a6cee3",
      "#377eb8", "#a65628"
    ]
  }
},
"opacity": { "value": 0.6 }
```

---
layout: two-cols
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">1.5 Tooltip</p>

# Show details on demand

Two steps: add a `calculate` transform, then list fields in `tooltip`.

## Calculate transform

```json
{
  "calculate":
    "datum.Confirmed / datum.Population * 10000",
  "as": "Cases per 10,000 Population"
}
```


::right::

```json {all|1|2-3|10-11}
"tooltip": [
  { "field": "Country",
    "type": "nominal" },
  { "field": "Confirmed",
    "type": "quantitative", "format": "," },
  { "field": "Active",
    "type": "quantitative", "format": "," },
  { "field": "Deaths",
    "type": "quantitative", "format": "," },
  { "field": "Cases per 10,000 Population",
    "type": "quantitative", "format": ".2f" }
]
```

---
layout: section
---

# 1.6 Filtering and Selections

Overview → filter → details on demand

---
layout: fact
---

# "Overview first, zoom and filter, then details-on-demand."

Ben Shneiderman

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Three filter types</p>

# What Vega-Lite v5 gives us

<div class="grid grid-cols-3 gap-6 mt-4">

<div>

### Legend selection
Click a legend item to highlight that category. Everything else fades.

`bind: "legend"`

</div>

<div>

### Dropdown
Pick one category from a list. Chart filters to show only that group.

`input: "select"`

</div>

<div>

### Slider
Drag to set a numeric threshold. Good for continuous values like population.

`input: "range"`

</div>

</div>

> Use a **dropdown** for categorical filters (continent, region). Use a **slider** for continuous numeric filters (population, GDP).

---
layout: two-cols
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">1.6.1 Legend selection</p>

# Click a continent to highlight it

Use `params` bound to the legend (Vega-Lite v5+):

> Selected continents stay bright at **0.8**. Unselected fade to **0.2**. Click again to deselect all.

::right::

```json {all|2-7|8|9-14|all}
"params": [{
  "name": "continent_highlight",
  "select": {
    "type": "point",
    "fields": ["Continent"]
  },
  "bind": "legend"
}],
"encoding": {
  "opacity": {
    "condition": {
      "param": "continent_highlight",
      "value": 0.8
    },
    "value": 0.2
  }
}
```

---
layout: two-cols
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">1.6.2 Dropdown filter</p>

# Filter by continent

Add a `select` input to `params`, then filter in `transform`:

> `null` is the "Show All" sentinel. Always use the **options** value (not labels) in the filter expression.

::right::

<div style="overflow-y: auto; max-height: 460px;">

```json {all|3-16|18-}
"params": [{
  "name": "Continent_selection",
  "bind": {
    "input": "select",
    "options": [
      null,
      "North America", "South America",
      "Europe", "Africa", "Asia", "Oceania"
    ],
    "labels": [
      "Show All",
      "North America", "South America",
      "Europe", "Africa", "Asia", "Oceania"
    ],
    "name": "Continent Selection: "
  }
}],
"transform": [{
  "filter":
    "Continent_selection == null ||
     datum.Continent == Continent_selection"
}]
```

</div>

---
layout: two-cols
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">1.6.3 Slider filter</p>

# Filter by population

Drag the slider to hide countries below a minimum population:

## Important

The filter expression references the **exact** param `name` — it is case-sensitive.

::right::

```json {all|2-9}
"params": [{
  "name": "Population_Above",
  "value": 0,
  "bind": {
    "input": "range",
    "min": 0,
    "max": 100000000,
    "step": 1000000,
    "name": "Minimum Population: "
  }
}],
"transform": [{
  "filter":
    "datum.Population > Population_Above"
}]
```

---
layout: two-cols
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">1.7 Text annotations</p>

# Label key countries with a text layer

Vega-Lite layers let you stack different mark types on shared axes.

Use an **opacity condition** to show labels only for named countries — not every data point.

> Setting `"value": 0` for unmatched rows makes labels invisible without removing any data.

::right::

<div style="overflow-y: auto; max-height: 460px;">
```json {all|20-29}
"layer": [
  {
    "mark": "circle",
    "encoding": { }
  },
  {
    "mark": {
      "type": "text",
      "align": "right",
      "baseline": "middle",
      "dx": -12,
      "fontSize": 11.5,
      "fontStyle": "italic"
    },
    "encoding": {
      "text": {
        "field": "Country", "type": "nominal"
      },
      "color": { "value": "black" },
      "opacity": {
        "condition": {
          "test": "datum['Country'] == 'China' ||
                   datum['Country'] == 'Singapore' ||
                   datum['Country'] == 'Australia' ||
                   datum['Country'] == 'United States'",
          "value": 1
        },
        "value": 0
      }
    }
  }
]
```
</div>

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Try it live</p>

# Interactive bubble plot — full spec

<VegaLitePlayground
  title="COVID-19 Bubble Plot"
  :height="300"
  :initialSpec="{
    '$schema': 'https://vega.github.io/schema/vega-lite/v5.json',
    'width': 200, 'height': 250,
    'title': 'COVID-19 Cases per Country (13 Oct 2020)',
    'data': {
      'url': 'https://raw.githubusercontent.com/FIT3179/Vega-Lite/main/4_interactive_scatter_plot/data/COVID_19_10_Oct_2020.csv'
    },
    'params': [
      {
        'name': 'Population_Above', 'value': 0,
        'bind': { 'input': 'range', 'min': 0, 'max': 100000000, 'step': 1000000, 'name': 'Min Population: ' }
      },
      {
        'name': 'Continent_selection',
        'bind': {
          'input': 'select',
          'options': [null, 'North America', 'South America', 'Europe', 'Africa', 'Asia', 'Oceania'],
          'labels': ['Show All', 'North America', 'South America', 'Europe', 'Africa', 'Asia', 'Oceania'],
          'name': 'Continent: '
        }
      }
    ],
    'transform': [
      { 'filter': 'datum.Active > 0' },
      { 'filter': 'datum.Deaths > 0' },
      { 'filter': 'datum.Population > Population_Above' },
      { 'filter': 'Continent_selection == null || datum.Continent == Continent_selection' },
      { 'calculate': 'datum.Confirmed/datum.Population * 10000', 'as': 'Cases per 10,000 Population' }
    ],
    'mark': 'circle',
    'encoding': {
      'x': { 'field': 'Confirmed', 'type': 'quantitative', 'title': 'Confirmed Cases', 'axis': { 'tickCount': 6 }, 'scale': { 'type': 'log', 'domain': [1, 10000000] } },
      'y': { 'field': 'Deaths', 'type': 'quantitative', 'axis': { 'tickCount': 5 }, 'scale': { 'type': 'log', 'domain': [1, 1000000] } },
      'color': { 'field': 'Continent', 'type': 'nominal', 'scale': { 'domain': ['North America','South America','Europe','Africa','Asia','Oceania'], 'range': ['#e41a1c','#984ea3','#ff7f00','#a6cee3','#377eb8','#a65628'] } },
      'size': { 'field': 'Population', 'type': 'quantitative', 'scale': { 'type': 'threshold', 'domain': [1000000,10000000,50000000,100000000,500000000], 'range': [10,50,150,200,300,400] }, 'legend': { 'format': '.1s' } },
      'opacity': { 'value': 0.7 },
      'tooltip': [
        { 'field': 'Country', 'type': 'nominal' },
        { 'field': 'Confirmed', 'type': 'quantitative', 'format': ',' },
        { 'field': 'Deaths', 'type': 'quantitative', 'format': ',' },
        { 'field': 'Cases per 10,000 Population', 'type': 'quantitative', 'format': '.2f' }
      ]
    }
  }"
/>

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Build checklist</p>

# Part 1 — what you should have now

<VClicks>

- ✅ **Basic bubble plot** — `mark: "circle"`, four encodings
- ✅ **Log axes** — `scale: { type: "log" }` + `transform` filters
- ✅ **Threshold size scale** — six population classes
- ✅ **Custom colour palette** — domain + range + opacity
- ✅ **Tooltip** — `calculate` for derived field + tooltip array
- ✅ **Legend selection** — `params` + `bind: "legend"` + opacity condition
- ✅ **Dropdown filter** — `bind: { input: "select" }` + transform filter
- ✅ **Slider filter** — `bind: { input: "range" }` + transform filter
- ✅ **Text annotations** — second layer, `mark: "text"`, opacity condition

</VClicks>

---
layout: section
---

# Part 2 — Multiple Charts on a Page

Building a simple dashboard with HTML and Pure.css

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">The goal</p>

# From single chart to dashboard

Vega-Lite renders one chart at a time. To show **multiple charts**, we use an HTML page as the container.

## Option 1 — HTML + CSS grid

Use **Pure.css** to lay out multiple `<div>` containers, each holding one Vega-Lite chart embedded via `vegaEmbed`.

## Option 2 — Vega-Lite concat

Vega-Lite can produce multi-view displays natively using `hconcat` or `vconcat`. We will cover this in Week 10.

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">HTML structure</p>

# Page skeleton

<div style="overflow-y: auto; max-height: 360px;">

```html {all|1-5|7-14|16-20|all}
<!-- 1. Load dependencies in <head> -->
<script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>
<link rel="stylesheet" href="https://unpkg.com/purecss@2.0.6/build/pure-min.css">

<!-- 2. Layout with Pure.css grid -->
<div class="pure-g">
  <div class="pure-u-1-2">
    <div id="chart1"></div>
  </div>
  <div class="pure-u-1-2">
    <div id="chart2"></div>
  </div>
</div>

<!-- 3. Embed each chart with vegaEmbed -->
<script>
  vegaEmbed('#chart1', 'line-chart-responsive.json')
  vegaEmbed('#chart2', 'normalised-stacked-bars-responsive.json')
</script>
```

</div>

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Layout patterns</p>

# Three Pure.css grid patterns

## Two columns

`.pure-u-1-2` on each child. Left column holds text or a title; right holds the chart.

## Three equal columns

`.pure-u-1-3` on each child. Good for three small charts side by side.

## Wide + narrow

`.pure-u-2-3` + `.pure-u-1-3`. A wide chart next to a narrow text or legend block.

> Same Pure.css fractions from Week 5 — just swap content blocks for `vegaEmbed` containers.

---
layout: two-cols
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Polish tips</p>

# Three things to add before you submit

<VClicks>

- **Responsive width** — let each chart fill its container
- **Hide the editor button** — cleaner for portfolio work
- **Attribution footer** — required for academic honesty

</VClicks>

## Responsive charts

Using `"width": "container"` means the chart resizes when the browser window changes. Pair with a percentage CSS width on the container div.

::right::

```html {all|2|5|7-9|all}
<!-- 1. Responsive width -->
{ "width": "container" }

<!-- 2. Hide editor button -->
vegaEmbed('#chart1', spec, { actions: false })

<!-- 3. Attribution footer -->
<p>Created by <a href="#">Your Name</a> ·
   Data: <a href="#">Source</a></p>
```

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Reference</p>

# Example and source code

## Live example

[fit3179.github.io/Vega-Lite/5_multiple_charts_html/](https://fit3179.github.io/Vega-Lite/5_multiple_charts_html/)

Shows two-column, three-column, and merged-column layouts on one page.

## Source code

[github.com/FIT3179/Vega-Lite → 5_multiple_charts_html](https://github.com/FIT3179/Vega-Lite/tree/main/5_multiple_charts_html)

Pay attention to `index.html`, the JSON spec files, and the `styles.css` overrides.

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Studio tasks</p>

# Your tasks for today

<VClicks>

- **Task 1 — Interactive bubble plot**
  Build the full COVID bubble plot step by step: log axes → size scale → colour → tooltip → legend selection → dropdown → slider → text annotations.

- **Task 2 — Dashboard page**
  Use the `5_multiple_charts_html` example as a starting point. Replace the Seattle weather charts with **two charts from your DV2 topic**. Apply `"width": "container"` and `actions: false`.

- **Stretch — Combine both filters**
  Have the dropdown and slider active simultaneously. Make sure both appear in the same `params` array.

</VClicks>

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Concepts summary</p>

# What we covered today

| Concept | Key property |
|---|---|
| Log scale | `"scale": { "type": "log" }` |
| Threshold size | `"scale": { "type": "threshold", "domain": [...] }` |
| Tooltip + derived field | `"transform": [{ "calculate": "...", "as": "..." }]` |
| Legend selection | `"params": [{ "bind": "legend" }]` |
| Dropdown filter | `"bind": { "input": "select", "options": [...] }` |
| Slider filter | `"bind": { "input": "range", "min": ..., "max": ... }` |
| Text annotation | Layer 2 with `"mark": "text"` + opacity condition |
| Multi-chart page | `vegaEmbed` + Pure.css grid |

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Before you leave</p>

# Week 9 checklist

<VClicks>

- The bubble plot spec runs without errors in the Vega Editor
- All three interaction types work — legend, dropdown, slider
- Text labels appear only on the selected countries
- At least two charts are embedded in your dashboard HTML
- `actions: false` hides the Vega Editor button
- The dashboard layout is readable on a standard laptop screen

</VClicks>

---
layout: section
---

# Vega-Lite Help Session

Remaining time — bring your DV2 questions

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Help session · remaining time</p>

# FAQs from previous years

<VClicks>

- **"My chart is blank / nothing renders"** — check the browser console for JSON syntax errors. A missing comma or bracket is the most common cause.

- **"The tooltip shows field names, not values"** — make sure `"type"` is specified for every tooltip field (`"nominal"`, `"quantitative"`, etc.).

- **"My log scale breaks with some data"** — filter out zeros and negatives in `transform` before applying the log scale.

- **"The dropdown shows the option value, not my label"** — `"labels"` and `"options"` must be the same length and in the same order. `null` in options maps to `"Show All"` in labels.

- **"My slider does nothing"** — make sure the filter expression references the exact `"name"` from the param (case-sensitive).

- **"Country labels overlap everywhere"** — use the opacity condition to show labels only for a small named subset, not every data point.

</VClicks>

---
layout: statement
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Help session · remaining time</p>

# Bring your DV2 questions


> Post questions on Ed early — other students likely have the same question.

---
layout: end
---

# See you next week
