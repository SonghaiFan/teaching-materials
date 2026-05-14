---
theme: default
title: Data Visualisation Studio 10
layout: cover
info: |
  ## FIT2179 Week 10
  Advanced interactions and multiple views in Vega-Lite
highlighter: shiki
drawings:
  persist: false
transition: slide-left
---
# FIT2179 Data Visualisation Week 10

Advanced interactions and multiple views in Vega-Lite

Songhai Fan · Monash University
---
layout: default
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Session plan</p>

# Today's agenda

| Time | Focus |
|---|---|
| 0 - 40 min | Advanced interactivity Part 1 |
| 40 - 80 min | Advanced interactivity Parts 2 and 3 |
| End | Exercise time, questions, and Test 2 reminder |

Today is mainly about reading Vega-Lite code patterns and then reusing them in your `DV2`.
---
layout: default
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Studio goals</p>

# By the end of today

- create multiple views in one Vega-Lite specification
- connect views with a brush selection
- use parameters for sliders and dropdowns
- build small multiples with `repeat`
- recognise which pattern is useful for your `DV2`
---
layout: section
---
# Part 1

Overview + detail
---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Demo first</p>

# Overview + detail demo

<VegaLitePlayground
  title="Brush the lower chart to zoom the upper chart"
  :height="300"
  :initialSpec="{
    '$schema': 'https://vega.github.io/schema/vega-lite/v5.json',
    data: {
      url: 'https://raw.githubusercontent.com/vega/vega-datasets/next/data/sp500.csv',
    },
    vconcat: [
      {
        width: 460,
        height: 220,
        mark: 'area',
        encoding: {
          x: {
            field: 'date',
            type: 'temporal',
            scale: { domain: { param: 'brush' } },
            axis: { title: '' },
          },
          y: { field: 'price', type: 'quantitative' },
        },
      },
      {
        width: 460,
        height: 60,
        mark: 'line',
        params: [
          {
            name: 'brush',
            select: { type: 'interval', encodings: ['x'] },
          },
        ],
        encoding: {
          x: { field: 'date', type: 'temporal' },
          y: {
            field: 'price',
            type: 'quantitative',
            axis: { tickCount: 3, grid: false },
          },
        },
      },
    ],
  }"
/>

---
layout: two-cols
zoom: 0.78
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Explain the code</p>

# `vconcat`

- Line `6`: `vconcat` places the two views vertically.
- Lines `8-9`: the first chart is the detailed view.
- Lines `17-18`: the second chart is the shorter overview.
- Line `12`: the top chart hides its x-axis title because the overview already provides time context.
- Try replacing `vconcat` with `hconcat` or `concat`.

::right::

<div style="overflow-y: auto; max-height: 580px;">

```json {6|8-9|12|17-18|all} {lines:true,startLine:1}
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {
    "url": "https://raw.githubusercontent.com/vega/vega-datasets/next/data/sp500.csv"
  },
  "vconcat": [
    {
      "width": 480,
      "height": 240,
      "mark": "area",
      "encoding": {
        "x": {"field": "date", "type": "temporal", "axis": {"title": ""}},
        "y": {"field": "price", "type": "quantitative"}
      }
    },
    {
      "width": 480,
      "height": 60,
      "mark": "area",
      "encoding": {
        "x": {"field": "date", "type": "temporal"},
        "y": {"field": "price", "type": "quantitative"}
      }
    }
  ]
}
```

</div>

---
layout: two-cols
zoom: 0.78
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Explain the code</p>

# Brush selection

- Line `15`: the detailed chart responds to the brush.
- Lines `25-27`: the overview chart defines a brushing selection.
- `interval` means users drag a continuous range.
- `encodings: ["x"]` restricts the brush to the x-axis.
- The selected range becomes the top chart's x-scale domain.

::right::

<div style="overflow-y: auto; max-height: 500px;">

```json {all} {lines:true,startLine:12}
"x": {
  "field": "date",
  "type": "temporal",
  "scale": {"domain": {"param": "brush"}},
  "axis": {"title": ""}
}
```

```json {all} {lines:true,startLine:25}
"params": [
  {"name": "brush", "select": {"type": "interval", "encodings": ["x"]}}
]
```

</div>

---
layout: default
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Exercise 1</p>

# Build overview + detail

Starting from the earthquake stacked area chart:

- put the stacked area chart in the first view
- add a short line chart as the second view
- define a brush on the line chart
- use the brush to filter or zoom the main chart

Make each view work separately first. Then connect them.
---
layout: default
zoom: 0.78
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Solution preview</p>

# Overview + detail solution preview

<VegaLitePlayground
  title="Earthquake overview + detail solution preview"
  :height="400"
  :initialSpec="{
    '$schema': 'https://vega.github.io/schema/vega-lite/v5.json',
    data: {
      url: 'https://raw.githubusercontent.com/FIT3179/Vega-Lite/main/6_advanced_examples/data/earthquake_lite.csv',
    },
    vconcat: [
      {
        width: 360,
        height: 170,
        transform: [
          {
            bin: { step: 0.5, extent: [5, 7] },
            field: 'mag',
            as: 'magnitude',
          },
        ],
        mark: 'area',
        encoding: {
          x: {
            field: 'time',
            type: 'temporal',
            timeUnit: 'yearmonth',
            scale: { domain: { param: 'brush' } },
            axis: { title: '' },
          },
          y: { aggregate: 'count', title: 'Count of Earthquakes' },
          color: {
            field: 'magnitude',
            scale: { range: ['#fdbe85', '#fd8d3c', '#e6550d', '#bd0026', '#7f0000'] },
            title: 'Magnitude',
          },
        },
      },
      {
        width: 360,
        height: 48,
        mark: 'line',
        title: 'Brush here to select a time period',
        params: [
          {
            name: 'brush',
            select: { type: 'interval', encodings: ['x'] },
          },
        ],
        encoding: {
          x: {
            field: 'time',
            type: 'temporal',
            timeUnit: 'yearmonth',
            axis: { title: '', format: '%Y' },
          },
          y: {
            aggregate: 'count',
            axis: { tickCount: 3, grid: false },
            title: 'Count',
          },
        },
      },
    ],
  }"
/>

---
layout: section
---
# Part 2

Coordinated views
---
layout: default
zoom: 0.78
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Demo first</p>

# Coordinated earthquake views demo

<VegaLitePlayground
  title="Coordinated earthquake views demo"
  :height="420"
  :initialSpec="{
    '$schema': 'https://vega.github.io/schema/vega-lite/v5.json',
    data: {
      url: 'https://raw.githubusercontent.com/FIT3179/Vega-Lite/main/6_advanced_examples/data/earthquake_lite.csv',
    },
    vconcat: [
      {
        width: 400,
        height: 230,
        projection: { type: 'equalEarth', rotate: [-150, 0, 0] },
        layer: [
          {
            data: {
              url: 'https://raw.githubusercontent.com/FIT3179/Vega-Lite/main/2_symbol_map/js/ne_110m_admin_0_countries.topojson',
              format: { type: 'topojson', feature: 'ne_110m_admin_0_countries' },
            },
            mark: { type: 'geoshape', fill: 'lightgray', stroke: 'white' },
          },
          {
            transform: [{ filter: { param: 'time_brush' } }],
            mark: { type: 'circle', opacity: 0.45, size: 18 },
            encoding: {
              longitude: { field: 'longitude', type: 'quantitative' },
              latitude: { field: 'latitude', type: 'quantitative' },
              color: {
                field: 'mag',
                type: 'quantitative',
                title: 'Magnitude',
                scale: {
                  type: 'threshold',
                  domain: [5.5, 6, 6.5, 7],
                  range: ['#fdbe85', '#fd8d3c', '#e6550d', '#bd0026', '#7f0000'],
                },
              },
              tooltip: [
                { field: 'time', type: 'temporal' },
                { field: 'mag', type: 'quantitative' },
                { field: 'place', type: 'nominal' },
              ],
            },
          },
        ],
      },
      {
        width: 480,
        height: 60,
        mark: 'line',
        title: 'Brush here to select a time period',
        params: [
          {
            name: 'time_brush',
            select: { type: 'interval', encodings: ['x'] },
          },
        ],
        encoding: {
          x: {
            field: 'time',
            timeUnit: 'yearmonth',
            axis: { title: '', format: '%Y' },
          },
          y: {
            aggregate: 'count',
            axis: { tickCount: 3, grid: false },
            title: 'Count',
          },
        },
      },
      {
        width: 480,
        height: 110,
        transform: [
          {
            bin: { step: 0.5, extent: [5, 7] },
            field: 'mag',
            as: 'magnitude',
          },
        ],
        mark: 'area',
        encoding: {
          x: {
            field: 'time',
            timeUnit: 'yearmonth',
            scale: { domain: { param: 'time_brush' } },
            axis: { title: '', tickCount: 5, grid: false },
          },
          y: { aggregate: 'count', title: 'Count' },
          color: {
            field: 'magnitude',
            scale: { range: ['#fdbe85', '#fd8d3c', '#e6550d', '#bd0026', '#7f0000'] },
            legend: null,
          },
        },
      },
    ],
    config: { title: { fontSize: 13 } },
  }"
/>

---
layout: two-cols
zoom: 0.78
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Explain the code</p>

# Three linked views

- `vconcat` combines three vertically stacked views.
- The first view is the map.
- The second view is the line chart that defines `time_brush`.
- The third view is the stacked area chart.
- The same named parameter can control multiple views.

::right::

<div style="overflow-y: auto; max-height: 500px;">

```json {1|3-8|10-15|17-22|all} {lines:true}
"vconcat": [
  {
    "width": 400,
    "height": 230,
    "projection": {"type": "equalEarth", "rotate": [-150, 0, 0]},
    "layer": [...]
  },
  {
    "width": 480,
    "height": 60,
    "mark": "line",
    "params": [...]
  },
  {
    "width": 480,
    "height": 110,
    "mark": "area",
    "encoding": {...}
  }
]
```

</div>

---
layout: two-cols
zoom: 0.78
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Explain the code</p>

# Map filter and colour scale

- The map only shows earthquakes inside `time_brush`.
- Longitude and latitude place circles on the map.
- Colour encodes magnitude.
- A threshold scale creates magnitude classes.
- The colour bins match the stacked area chart later.

::right::

<div style="overflow-y: auto; max-height: 460px;">

```json {1|3-4|5-13|9-12|all} {lines:true}
"transform": [{"filter": {"param": "time_brush"}}],
"encoding": {
  "longitude": {"field": "longitude", "type": "quantitative"},
  "latitude": {"field": "latitude", "type": "quantitative"},
  "color": {
    "field": "mag",
    "type": "quantitative",
    "title": "Magnitude",
    "scale": {
      "type": "threshold",
      "domain": [5.5, 6, 6.5, 7],
      "range": ["#fdbe85", "#fd8d3c", "#e6550d", "#bd0026", "#7f0000"]
    }
  }
}
```

</div>

---
layout: two-cols
zoom: 0.78
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Explain the code</p>

# Filter vs zoom

- The line chart creates the `time_brush` parameter.
- The map filters rows to the selected time period.
- The area chart keeps all rows but zooms the x-axis.
- Use `filter` when the marks should disappear.
- Use `scale.domain` when the view should zoom into the selected range.

::right::

<div style="overflow-y: auto; max-height: 430px;">

```json {1-6|all} {lines:true}
"params": [
  {
    "name": "time_brush",
    "select": {"type": "interval", "encodings": ["x"]}
  }
]
```

```json {all} {lines:true}
"transform": [{"filter": {"param": "time_brush"}}]
```

```json {all} {lines:true}
"x": {
  "field": "time",
  "timeUnit": "yearmonth",
  "scale": {"domain": {"param": "time_brush"}}
}
```

</div>

---
layout: default
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Exercise 2</p>

# Coordinated view practice

## Practice 1: layout

- change the layout to match Figure 6 from the studio handout
- place the map and stacked area chart side by side
- keep the filtering line chart underneath

## Practice 2: greatest earthquake mark

- change the size and shape of the mark for the greatest earthquake
- example: use a `point` mark with a custom star-shaped SVG path
- hint: check the `shape` property for Vega-Lite point marks

---
layout: default
zoom: 0.78
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Solution preview</p>

# Coordinated view solution preview

<VegaLitePlayground
  title="Brush the line chart to filter the map and zoom the area chart"
  :height="420"
  :initialSpec="{
    '$schema': 'https://vega.github.io/schema/vega-lite/v5.json',
    data: {
      url: 'https://raw.githubusercontent.com/FIT3179/Vega-Lite/main/6_advanced_examples/data/earthquake_lite.csv',
    },
    vconcat: [
      {
        hconcat: [
          {
            width: 340,
            height: 230,
            title: 'Earthquakes above a magnitude of 5',
            projection: { type: 'equalEarth', rotate: [-150, 0, 0] },
            layer: [
              {
                data: {
                  url: 'https://raw.githubusercontent.com/FIT3179/Vega-Lite/main/2_symbol_map/js/ne_110m_admin_0_countries.topojson',
                  format: { type: 'topojson', feature: 'ne_110m_admin_0_countries' },
                },
                mark: { type: 'geoshape', fill: 'lightgray', stroke: 'white' },
              },
              {
                transform: [{ filter: { param: 'time_brush' } }],
                mark: { type: 'circle', opacity: 0.35, size: 12 },
                encoding: {
                  longitude: { field: 'longitude', type: 'quantitative' },
                  latitude: { field: 'latitude', type: 'quantitative' },
                  color: {
                    field: 'mag',
                    type: 'quantitative',
                    title: 'Magnitude',
                    scale: {
                      type: 'threshold',
                      domain: [5.5, 6, 6.5, 7],
                      range: ['#fdbe85', '#fd8d3c', '#e6550d', '#bd0026', '#7f0000'],
                    },
                  },
                  tooltip: [
                    { field: 'time', type: 'temporal' },
                    { field: 'mag', type: 'quantitative' },
                    { field: 'place', type: 'nominal' },
                  ],
                },
              },
              {
                transform: [
                  { filter: { param: 'time_brush' } },
                  {
                    window: [{ op: 'rank', as: 'ranking' }],
                    sort: [{ field: 'mag', order: 'descending' }],
                  },
                  { filter: 'datum.ranking == 1' },
                ],
                mark: {
                  type: 'point',
                  shape: 'M0,-1 L0.224,-0.309 L0.951,-0.309 L0.363,0.118 L0.588,0.809 L0,0.382 L-0.588,0.809 L-0.363,0.118 L-0.951,-0.309 L-0.224,-0.309 Z',
                  filled: true,
                  size: 220,
                  color: '#111827',
                  stroke: 'white',
                  strokeWidth: 1.5,
                },
                encoding: {
                  longitude: { field: 'longitude', type: 'quantitative' },
                  latitude: { field: 'latitude', type: 'quantitative' },
                  tooltip: [
                    { field: 'place', type: 'nominal', title: 'Greatest earthquake' },
                    { field: 'mag', type: 'quantitative', title: 'Magnitude' },
                    { field: 'time', type: 'temporal' },
                  ],
                },
              },
            ],
          },
          {
            width: 250,
            height: 230,
            transform: [
              {
                bin: { step: 0.5, extent: [5, 7] },
                field: 'mag',
                as: 'magnitude',
              },
            ],
            mark: 'area',
            encoding: {
              x: {
                field: 'time',
                type: 'temporal',
                timeUnit: 'yearmonth',
                scale: { domain: { param: 'time_brush', encoding: 'x' } },
                axis: { title: '', tickCount: 5, grid: false },
              },
              y: { aggregate: 'count', type: 'quantitative', title: 'Count of Earthquakes' },
              color: {
                field: 'magnitude',
                type: 'ordinal',
                scale: { range: ['#fdbe85', '#fd8d3c', '#e6550d', '#bd0026', '#7f0000'] },
                legend: null,
              },
            },
          },
        ],
      },
      {
        width: 720,
        height: 60,
        mark: 'line',
        title: 'Brush here to select a time period',
        params: [
          {
            name: 'time_brush',
            select: { type: 'interval', encodings: ['x'] },
          },
        ],
        encoding: {
          x: {
            field: 'time',
            type: 'temporal',
            timeUnit: 'yearmonth',
            axis: { title: '', format: '%Y' },
          },
          y: {
            aggregate: 'count',
            type: 'quantitative',
            axis: { tickCount: 3, grid: false },
            title: 'Count',
          },
        },
      },
    ],
    config: { title: { fontSize: 13 } },
  }"
/>

---
layout: section
---
# Part 3

Parameters for maps
---
layout: default
zoom: 0.78
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Demo first</p>

# Choropleth with controls demo

<VegaLitePlayground
  title="Use the controls to change year, zoom, and centre"
  :height="420"
  :initialSpec="{
    '$schema': 'https://vega.github.io/schema/vega-lite/v5.json',
    title: 'Median house price per suburb (2010-2020)',
    width: 480,
    height: 320,
    params: [
      {
        name: 'Year_selection',
        value: 2018,
        bind: { input: 'range', min: 2010, max: 2020, step: 1, name: 'Year: ' },
      },
      {
        name: 'zoom_level',
        value: 30000,
        bind: { input: 'range', min: 3500, max: 60000, step: 100, name: 'Zoom: ' },
      },
      {
        name: 'center_to',
        value: [145, -37.95],
        bind: {
          input: 'select',
          options: [[145, -37.95], [144.3, -38.1], [144.9, -36.7], [147.1, -38.1]],
          labels: ['Melbourne CBD', 'Geelong', 'Bendigo', 'Sale'],
          name: 'Map Centre: ',
        },
      },
    ],
    projection: {
      type: 'equirectangular',
      center: { expr: 'center_to' },
      scale: { expr: 'zoom_level' },
    },
    layer: [
      {
        data: {
          url: 'https://raw.githubusercontent.com/FIT3179/Vega-Lite/main/6_advanced_examples/data/VIC_LOCALITY_POLYGON_SHP.json',
          format: { type: 'topojson', feature: 'VIC_LOCALITY_POLYGON_SHP' },
        },
        mark: { type: 'geoshape', fill: '#ddd', stroke: 'white', strokeWidth: 1 },
      },
      {
        data: {
          url: 'https://raw.githubusercontent.com/FIT3179/Vega-Lite/main/6_advanced_examples/data/house_price_by_suburb_long_format.csv',
        },
        transform: [
          {
            lookup: 'locality',
            from: {
              data: {
                url: 'https://raw.githubusercontent.com/FIT3179/Vega-Lite/main/6_advanced_examples/data/VIC_LOCALITY_POLYGON_SHP.json',
                format: { type: 'topojson', feature: 'VIC_LOCALITY_POLYGON_SHP' },
              },
              key: 'properties.NAME',
            },
            as: 'geo',
          },
          { filter: 'datum.year == Year_selection' },
        ],
        mark: { type: 'geoshape', stroke: '#fff', strokeWidth: 0.5 },
        encoding: {
          shape: { field: 'geo', type: 'geojson' },
          color: {
            field: 'price',
            type: 'quantitative',
            title: 'Price',
            scale: { domain: [400000, 1800000], scheme: 'reds' },
            legend: { format: '.2s' },
          },
          tooltip: [
            { field: 'locality', type: 'nominal', title: 'Suburb' },
            { field: 'price', type: 'quantitative', title: 'Median Price', format: ',' },
            { field: 'year', type: 'quantitative', title: 'Year' },
          ],
        },
      },
    ],
  }"
/>

---
layout: two-cols
zoom: 0.78
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Explain the code</p>

# Year and zoom sliders

- Lines `7-17`: `Year_selection` is a range slider.
- Lines `18-28`: `zoom_level` is another range slider.
- These are UI controls bound to parameters, not selections from chart marks.
- Other parts of the spec read the live parameter values.

::right::

<div style="overflow-y: auto; max-height: 600px;">

```json {7-17|18-28|all} {lines:true,startLine:6}
"params": [
  {
    "name": "Year_selection",
    "value": 2018,
    "bind": {
      "input": "range",
      "min": 2010,
      "max": 2020,
      "step": 1,
      "name": "Year: "
    }
  },
  {
    "name": "zoom_level",
    "value": 30000,
    "bind": {
      "input": "range",
      "min": 3500,
      "max": 60000,
      "step": 100,
      "name": "Zoom: "
    }
  }
]
```

</div>

---
layout: two-cols
zoom: 0.78
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Explain the code</p>

# Map centre dropdown

- Lines `29-43`: `center_to` is a dropdown with named locations.
- Line `31`: the default centre is Melbourne CBD.
- Lines `34-39`: each option is a longitude-latitude pair.
- Line `40`: labels make the dropdown readable.
- This is a workaround because Vega-Lite does not provide direct drag-to-pan map controls.

::right::

<div style="overflow-y: auto; max-height: 600px;">

```json {29-43|31|34-39|40|all} {lines:true,startLine:29}
{
  "name": "center_to",
  "value": [145, -37.95],
  "bind": {
    "input": "select",
    "options": [
      [145, -37.95],
      [144.3, -38.1],
      [144.9, -36.7],
      [147.1, -38.1]
    ],
    "labels": ["Melbourne CBD", "Geelong", "Bendigo", "Sale"],
    "name": "Map Centre: "
  }
}
```

</div>

---
layout: two-cols
zoom: 0.78
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Explain the code</p>

# Projection and base layer

- Lines `45-49`: the projection reads `center_to` and `zoom_level`.
- Lines `47-48`: `expr` means the value comes from a parameter expression.
- Lines `51-69`: the first layer draws the grey suburb polygons.
- This base layer gives the choropleth a visible background.
- We will turn this into a missing-data tooltip in the practice.

::right::

<div style="overflow-y: auto; max-height: 600px;">

```json {all}{lines:true,startLine:45}
"projection": {
  "type": "equirectangular",
  "center": {"expr": "center_to"},
  "scale": {"expr": "zoom_level"}
}
```

```json {all}{lines:true,startLine:62}
"mark": {
  "type": "geoshape",
  "fill": "#ddd",
  "stroke": "white",
  "strokeWidth": 1
}
```

</div>

---
layout: two-cols
zoom: 0.78
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Explain the code</p>

# Lookup, filter, and encoding

- Lines `76-87`: join each CSV row to its suburb geometry.
- Line `89`: keep only rows from the selected year.
- This is the key data join: CSV values first, matching geometry second.
- The filter happens after the lookup so the selected year still has geometry.

```json {76-87|89} {lines:true,startLine:76}
"lookup": "locality",
"from": {
  "data": {
    "url": "VIC_LOCALITY_POLYGON_SHP.json",
    "format": {
      "type": "topojson",
      "feature": "VIC_LOCALITY_POLYGON_SHP"
    }
  },
  "key": "properties.NAME"
},
"as": "geo"
},
{"filter": "datum.year == Year_selection"}
```

::right::


Thus the original data：
```json
{
  "locality": "MURNUNGING",
  "year": 2018,
  "price": 500000
}
```

After `lookup`：

```json
{
  "locality": "MURNUNGING",
  "year": 2018,
  "price": 500000,
  "geo": {
    "type": "Polygon",
    "properties": {
      "NAME": "MURNUNGING"
    },
    "coordinates": [...]
  }
}
```

---
layout: default
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Practice</p>

# Try `facet`

Convert the house-price small multiple from `repeat` to `facet`:

- use the long-format CSV
- facet the map by `year`
- use `columns: 2`
- remove the manual year-label layer
- compare what you gain and lose compared with `repeat`
---
layout: default
zoom: 0.78
---

<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Solution preview</p>

# Small multiples with `facet` solution preview

<VegaLitePlayground
  title="Solution preview: faceted long-format data"
  :height="450"
  :initialSpec="{
    '$schema': 'https://vega.github.io/schema/vega-lite/v5.json',
    title: 'Median house price per suburb',
    data: {
      url: 'https://raw.githubusercontent.com/FIT3179/Vega-Lite/main/6_advanced_examples/data/house_price_by_suburb_long_format.csv',
    },
    transform: [
      {
        lookup: 'locality',
        from: {
          data: {
            url: 'https://raw.githubusercontent.com/FIT3179/Vega-Lite/main/6_advanced_examples/data/VIC_LOCALITY_POLYGON_SHP.json',
            format: { type: 'topojson', feature: 'VIC_LOCALITY_POLYGON_SHP' },
          },
          key: 'properties.NAME',
        },
        as: 'geo',
      },
    ],
    facet: {
      field: 'year',
      type: 'ordinal',
      header: { title: null, labelAngle: 0 },
    },
    columns: 2,
    spec: {
      projection: {
        type: 'equirectangular',
        center: [144.4, -37.6],
        scale: 21000,
      },
      width: 200,
      height: 118,
      mark: { type: 'geoshape', stroke: '#fff', strokeWidth: 0.5 },
      encoding: {
        shape: { field: 'geo', type: 'geojson' },
        color: {
          field: 'price',
          type: 'quantitative',
          title: 'Median price',
          scale: { domain: [400000, 1800000], scheme: 'reds' },
          legend: { format: '.2s' },
        },
        tooltip: [
          { field: 'locality', type: 'nominal', title: 'Suburb' },
          { field: 'price', type: 'quantitative', title: 'Median Price', format: ',' },
          { field: 'year', type: 'ordinal', title: 'Year' },
        ],
      },
    },
  }"
/>

---
layout: default
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Pattern comparison</p>

# `repeat` or `facet`?

| Pattern | Good fit |
|---|---|
| `repeat` | repeated fields in wide-format data |
| `repeat` | layered small multiples, like base map + data map + text label |
| `facet` | one long-format table with a panel category, such as `year` |
| `facet` | simpler small multiples with automatic panel labels |
---
layout: default
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Choosing a pattern</p>

# Use the pattern that matches the task

| Pattern | Use when |
|---|---|
| `vconcat` + brush | one view controls detail in another view |
| coordinated views | multiple charts should respond to one selection |
| bound parameters | users need sliders or dropdown controls |
| `repeat` | you want the same chart repeated for several fields |
| `facet` | you want one chart per category in long-format data |
---
layout: default
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Reminder</p>

# Before next week

- Test 2 is during the `Week 11` workshop.
- Keep building `DV2` charts, map, layout, and interactions.
- Make static charts work before adding interactions.
- Bring one specific code question to consultation or Ed.
