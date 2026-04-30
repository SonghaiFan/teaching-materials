---
theme: default
title: Data Visualisation Studio 8
layout: cover
info: |
  ## FIT2179 Week 8
  DV2 sketch feedback and maps with Vega-Lite
highlighter: shiki
drawings:
  persist: false
transition: slide-left
---

# FIT2179 Data Visualisation Week 8

DV2 sketch feedback and maps with Vega-Lite

Songhai Fan · Monash University

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Session plan</p>

# Today's agenda

| Time | Focus |
|---|---|
| First hour | `DV2` sketch presentation and feedback |
| Second hour | Create maps with `Vega-Lite` |

> Today is project-driven. We use the first half to improve your DV2 direction, then use the second half to build map confidence.

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Studio goals</p>

# By the end of today

1. You have received feedback on your `DV2` sketch.
2. Your domain is clearly different from `DV1`.
3. You have a realistic map idea for the project.
4. You understand the basic structure of Vega-Lite maps.
5. You know what data to find or clean next.

---
layout: section
---

# DV2 Sketch Feedback

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">3-minute share</p>

# What to present

- your domain, audience, and main question
- how the story flows through the page
- where the map appears in the sketch
- what datasets you plan to use
- one thing you want feedback on

<div class="mt-5 border-l-2 border-slate-400 pl-4 text-sm text-slate-600">
Keep it short. The goal is not to defend a finished design, but to improve an early one.
</div>

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Feedback lens</p>

# What we are checking

- is the domain clearly different from your `DV1`?
- does the project include a meaningful map idiom?
- is the topic understandable for a general audience?
- can the story fit on one scrolling web page?
- are the planned datasets public and realistic?

---
layout: fact
---

# DV2 must include a map

No map means the visualisation cannot fully satisfy the assignment requirements.

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Use feedback now</p>

# Before moving to maps

Write down:

- one change to the topic or scope
- one change to the sketch layout
- one possible map idiom
- one data task for this week

---
layout: section
---

# Maps With Vega-Lite

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">When to use a map</p>

# Maps are for geographic questions

Use a map when location is part of the insight:

- where something happens
- how places compare
- how a pattern changes across regions
- how location connects to another variable

> Do not add a map only because it looks impressive. Make it earn its place in the story.

---
layout: two-cols
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Spatial data</p>

# Two common data shapes

- point data: `latitude` and `longitude`
- region data: country, state, suburb, postcode, or other boundaries

::right::

# Two common map idioms

- proportional symbol map
- choropleth map

<div class="mt-5 border border-slate-300 bg-white/60 p-4 text-sm">
The idiom depends on the data. Points and regions are not interchangeable.
</div>

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Spatial formats</p>

# Files you will see today

- `CSV`: tabular data, often with fields such as `latitude`, `longitude`, or `Country`
- `GeoJSON`: geographic shapes in JSON format
- `TopoJSON`: a smaller topology-based format often used for map boundaries

<div class="mt-5 border-l-2 border-slate-400 pl-4 text-sm text-slate-600">
For larger map files, tools such as `mapshaper` can simplify and convert spatial data.
</div>

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Projection</p>

# Maps need a projection

```json
"projection": {
  "type": "equalEarth"
}
```

- a projection turns the globe into a flat view
- `equalEarth` is a good general-purpose projection for world maps
- different map tasks may need different projections

---
layout: section
---

# Proportional Symbol Map

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Pattern</p>

# Symbol map structure

1. Draw the base map with `geoshape`.
2. Add a second layer of point marks.
3. Use `longitude` and `latitude` to position the points.
4. Use `size`, `color`, and `tooltip` to encode extra attributes.

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Key idea</p>

# Layer a basemap and points

```json
{
  "projection": {"type": "equalEarth"},
  "layer": [
    {
      "data": {
        "url": "js/ne_110m_admin_0_countries.topojson",
        "format": {
          "type": "topojson",
          "feature": "ne_110m_admin_0_countries"
        }
      },
      "mark": {"type": "geoshape", "fill": "lightgray"}
    },
    {
      "data": {"url": "data/earthquake.csv"},
      "mark": {"type": "circle", "tooltip": {"content": "data"}},
      "encoding": {
        "longitude": {"field": "longitude", "type": "quantitative"},
        "latitude": {"field": "latitude", "type": "quantitative"},
        "size": {"field": "mag", "type": "quantitative"},
        "color": {"field": "depth", "type": "quantitative"}
      }
    }
  ]
}
```

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Activity</p>

# Open the symbol map example

Source folder:

```txt
materials/fit2179/week8/Week 8 Studio Source Code/2_symbol_map
```

Try:

- open `index.html`
- inspect `js/symbol_map.vg.json`
- find the `longitude` and `latitude` encodings
- change the `size` or `color` field and refresh

---
layout: section
---

# Choropleth Map

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Pattern</p>

# Choropleth map structure

1. Start with boundary shapes, such as countries or states.
2. Join table data to the boundary data.
3. Colour each region by a quantitative value.
4. Add tooltips to make values readable.

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Key idea</p>

# Join data with `lookup`

```json
"transform": [
  {
    "lookup": "properties.NAME",
    "from": {
      "data": {"url": "data/covid_10_10_2020.csv"},
      "key": "Country",
      "fields": ["Active"]
    }
  },
  {
    "calculate": "datum.Active + 0.1",
    "as": "Active Cases"
  }
]
```

- `lookup` matches the map's country name to the CSV country name
- `fields` selects the values to bring into the map
- `calculate` creates a new field for encoding

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Colour regions</p>

# Encode the joined value

```json
"mark": {"type": "geoshape"},
"encoding": {
  "color": {
    "field": "Active Cases",
    "type": "quantitative",
    "scale": {"type": "log"}
  },
  "tooltip": [
    {"field": "properties.NAME", "type": "nominal", "title": "Country"},
    {"field": "Active", "type": "quantitative"}
  ]
}
```

> Check your join carefully. A choropleth can look valid even when many regions have missing data.

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Activity</p>

# Open the choropleth example

Source folder:

```txt
materials/fit2179/week8/Week 8 Studio Source Code/3_choropleth_map
```

Try:

- open `index.html`
- inspect `js/choropleth_map.vg.json`
- identify the boundary file and CSV file
- find the join key on both sides
- inspect what happens when a country name does not match

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">If time</p>

# Map refinements

Explore these files after the basic examples work:

- `mapWithGraticules.html`
- `emptyCountries.html`
- `choroplethMapWithOcean.html`
- `choroplethMapWithCountryName.html`

Use refinements only when they support the story and improve readability.

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">DV2 planning</p>

# Choose the right map for your project

| If your data is... | Consider... |
|---|---|
| exact locations | proportional symbol map |
| regions with rates or counts | choropleth map |
| movement between places | flow map or connected points |
| many small local areas | simplify boundaries and reduce detail |

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Before you leave</p>

# Week 8 checklist

- revise your sketch based on feedback
- confirm the map idiom for your DV2 story
- find public data from at least two sources
- test one Vega-Lite map example locally
- bring data questions to consultation or Ed early

