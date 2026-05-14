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
zoom: 0.78
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Demo first</p>

# Overview + detail demo

<VegaLitePlayground
  title="Brush the lower chart to zoom the upper chart"
  :height="400"
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
zoom: 0.88
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Explain the code</p>

# `vconcat`

- Line `6`: `vconcat` places the two views vertically.
- Lines `8-9`: the first chart is the detailed view.
- Lines `17-18`: the second chart is the shorter overview.
- Line `12`: the top chart hides its x-axis title because the overview already provides time context.
- Try replacing `vconcat` with `hconcat` or `concat`.

::right::

<div style="overflow-y: auto; max-height: 500px;">

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
zoom: 0.88
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

```json {15|all} {lines:true,startLine:12}
"x": {
  "field": "date",
  "type": "temporal",
  "scale": {"domain": {"param": "brush"}},
  "axis": {"title": ""}
}
```

```json {25-27|26|all} {lines:true,startLine:25}
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
  title="Brush the lower chart to zoom the upper chart"
  :height="300"
  :initialSpec="{
    '$schema': 'https://vega.github.io/schema/vega-lite/v5.json',
    data: {
      url: 'https://raw.githubusercontent.com/vega/vega-datasets/next/data/sp500.csv',
    },
    vconcat: [
      {
        width: 480,
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
        width: 480,
        height: 60,
        mark: 'area',
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
layout: section
---
# Part 2

Coordinated views
---
layout: default
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Demo first</p>

# Coordinated earthquake views demo

<VegaLitePlayground
  title="Brush the line chart to filter the map and zoom the area chart"
  :height="320"
  :initialSpec="{
    '$schema': 'https://vega.github.io/schema/vega-lite/v5.json',
    data: {
      url: 'https://raw.githubusercontent.com/FIT3179/Vega-Lite/main/6_advanced_examples/data/earthquake_lite.csv',
    },
    vconcat: [
      {
        width: 480,
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
zoom: 0.86
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Explain the code</p>

# Three linked views

- Lines `6-141`: `vconcat` combines three vertically stacked views.
- Lines `7-89`: the map view.
- Lines `90-113`: the line chart view that defines `time_brush`.
- Lines `114-140`: the stacked area chart view.
- The same named parameter can control multiple views.

::right::

<div style="overflow-y: auto; max-height: 500px;">

```json {6|7-12|13-18|19-25|all} {lines:true,startLine:6}
"vconcat": [
  {
    "width": "container",
    "height": 400,
    "projection": {"type": "equalEarth", "rotate": [-150, 0, 0]},
    "layer": [...]
  },
  {
    "width": "container",
    "height": 60,
    "mark": "line",
    "params": [...]
  },
  {
    "width": "container",
    "mark": "area",
    "encoding": {...}
  }
]
```

</div>
---
layout: two-cols
zoom: 0.86
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Explain the code</p>

# Map filter and colour scale

- Line `38`: the map only shows earthquakes inside `time_brush`.
- Lines `40-41`: longitude and latitude place circles on the map.
- Lines `42-45`: colour encodes magnitude.
- Lines `46-50`: a threshold scale creates magnitude classes.
- The colour bins match the stacked area chart later.

::right::

<div style="overflow-y: auto; max-height: 460px;">

```json {38|40-41|42-50|all} {lines:true,startLine:38}
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
zoom: 0.86
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Explain the code</p>

# Filter vs zoom

- Lines `95-100`: the line chart creates the `time_brush` parameter.
- Line `38`: the map filters rows to the selected time period.
- Line `128`: the area chart keeps all rows but zooms the x-axis.
- Use `filter` when the marks should disappear.
- Use `scale.domain` when the view should zoom into the selected range.

::right::

<div style="overflow-y: auto; max-height: 430px;">

```json {95-100|all} {lines:true,startLine:95}
"params": [
  {
    "name": "time_brush",
    "select": {"type": "interval", "encodings": ["x"]}
  }
]
```

```json {38|all} {lines:true,startLine:38}
"transform": [{"filter": {"param": "time_brush"}}]
```

```json {128|all} {lines:true,startLine:125}
"x": {
  "field": "time",
  "timeUnit": "yearmonth",
  "scale": {"domain": {"param": "time_brush"}}
}
```

</div>
---
layout: two-cols
zoom: 0.86
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Explain the code</p>

# Annotation transform

- Lines `63-64`: rank earthquakes by magnitude, largest first.
- Line `66`: keep only the highest ranked row.
- Lines `67-70`: create text for the annotation.
- Lines `71-74`: split the text into two lines.
- This pattern is useful when annotation depends on the current selection.

::right::

<div style="overflow-y: auto; max-height: 460px;">

```json {63-64|66|67-70|71-74|all} {lines:true,startLine:61}
"transform": [
  {
    "window": [{"op": "rank", "as": "ranking"}],
    "sort": [{"field": "mag", "order": "descending"}]
  },
  {"filter": "datum.ranking == 1"},
  {
    "calculate": "'The worst earthquake of; the selected period: ' + datum['mag']",
    "as": "text_annotation_raw"
  },
  {
    "calculate": "split(datum.text_annotation_raw, ';')",
    "as": "text_annotation"
  }
]
```

</div>
---
layout: default
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Exercise 2</p>

# Coordinated view practice

## Practice 1: greatest earthquake mark

- change the size and shape of the mark for the greatest earthquake
- example: use a `point` mark with `shape: "star"`
- hint: check the `shape` property for Vega-Lite point marks

## Practice 2: layout

- change the layout to match Figure 6 from the studio handout
- place the map and stacked area chart side by side
- keep the filtering line chart underneath
---
layout: default
zoom: 0.73
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Solution preview</p>

# Coordinated view solution preview

<VegaLitePlayground
  title="Brush the line chart to filter the map and zoom the area chart"
  :height="320"
  :initialSpec="{
    '$schema': 'https://vega.github.io/schema/vega-lite/v5.json',
    data: {
      url: 'https://raw.githubusercontent.com/FIT3179/Vega-Lite/main/6_advanced_examples/data/earthquake_lite.csv',
    },
    vconcat: [
      {
        width: 450,
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
layout: section
---
# Part 3

Parameters for maps
---
layout: default
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Demo first</p>

# Choropleth with controls demo

<VegaLitePlayground
  title="Use the controls to change year, zoom, and centre"
  :height="340"
  :initialSpec="{
    '$schema': 'https://vega.github.io/schema/vega-lite/v5.json',
    title: 'Median house price per suburb (2010-2020)',
    width: 500,
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
zoom: 0.84
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Explain the code</p>

# Year and zoom sliders

- Lines `7-17`: `Year_selection` is a range slider.
- Lines `18-28`: `zoom_level` is another range slider.
- These are UI controls bound to parameters, not selections from chart marks.
- Other parts of the spec read the live parameter values.

::right::

<div style="overflow-y: auto; max-height: 460px;">

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
zoom: 0.84
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Explain the code</p>

# Map centre dropdown

- Lines `29-43`: `center_to` is a dropdown with named locations.
- Line `31`: the default centre is Melbourne CBD.
- Lines `34-39`: each option is a longitude-latitude pair.
- Line `40`: labels make the dropdown readable.
- This is a workaround because Vega-Lite does not provide direct drag-to-pan map controls.

::right::

<div style="overflow-y: auto; max-height: 460px;">

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
zoom: 0.86
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Explain the code</p>

# Projection and base layer

- Lines `45-49`: the projection reads `center_to` and `zoom_level`.
- Lines `47-48`: `expr` means the value comes from a parameter expression.
- Lines `51-69`: the base map shows suburbs with no available data.
- Lines `56-60`: create a tooltip note for missing data.
- Lines `62-68`: draw the grey base-map polygons.

::right::

<div style="overflow-y: auto; max-height: 460px;">

```json {47-48|all} {lines:true,startLine:45}
"projection": {
  "type": "equirectangular",
  "center": {"expr": "center_to"},
  "scale": {"expr": "zoom_level"}
}
```

```json {56-60|all} {lines:true,startLine:56}
"transform": [
  {
    "calculate": "'Data is not available in ' + datum.properties.NAME",
    "as": "note"
  }
]
```

```json {62-68|all} {lines:true,startLine:62}
"mark": {
  "type": "geoshape",
  "fill": "#ddd",
  "stroke": "white",
  "strokeWidth": 1
},
"encoding": {"tooltip": {"field": "note"}}
```

</div>
---
layout: two-cols
zoom: 0.86
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Explain the code</p>

# Lookup, filter, and encoding

- Lines `76-87`: join each CSV row to its suburb geometry.
- Line `89`: keep only rows from the selected year.
- Line `93`: use the joined `geo` field as the shape.
- Lines `94-99`: colour each suburb by median price.
- Lines `101-110`: add readable tooltip fields.

::right::

<div style="overflow-y: auto; max-height: 430px;">

```json {76-87|89|all} {lines:true,startLine:76}
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

```json {93|94-99|101-110|all} {lines:true,startLine:91}
"mark": {"type": "geoshape", "stroke": "#fff", "strokeWidth": 0.5},
"encoding": {
  "shape": {"field": "geo", "type": "geojson"},
  "color": {
    "field": "price",
    "type": "quantitative",
    "title": "Price",
    "scale": {"domain": [400000, 1800000], "scheme": "reds"},
    "legend": {"format": ".2s"}
  },
  "tooltip": [
    {"field": "locality", "type": "nominal", "title": "Suburb"},
    {"field": "price", "type": "quantitative", "title": "Median Price"},
    {"field": "year", "type": "quantitative", "title": "Year"}
  ]
}
```

</div>
---
layout: default
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Practice</p>

# Why load the CSV first?

- the CSV has one row per `suburb-year`
- the TopoJSON has one feature per suburb
- the selected year is a row filter, so the year lives naturally in the CSV layer
- after filtering, each selected CSV row looks up its matching geometry
- if suburb names do not match, the geometry will be missing
---
layout: default
zoom: 0.72
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Solution preview</p>

# Choropleth with controls solution preview

<VegaLitePlayground
  title="Use the controls to change year, zoom, and centre"
  :height="340"
  :initialSpec="{
    '$schema': 'https://vega.github.io/schema/vega-lite/v5.json',
    title: 'Median house price per suburb (2010-2020)',
    width: 500,
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
layout: section
---
# Part 4

Small multiples
---
layout: default
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Demo first</p>

# Small multiples with `repeat` demo

<VegaLitePlayground
  title="Six repeated choropleth views"
  :height="340"
  :initialSpec="{
    '$schema': 'https://vega.github.io/schema/vega-lite/v5.json',
    title: 'Median house price per suburb',
    repeat: ['2010', '2012', '2014', '2016', '2018', '2020'],
    columns: 2,
    spec: {
      projection: {
        type: 'equirectangular',
        center: [144.4, -37.6],
        scale: 21000,
      },
      width: 210,
      height: 160,
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
            url: 'https://raw.githubusercontent.com/FIT3179/Vega-Lite/main/6_advanced_examples/data/house_price_by_suburb_wide_format.csv',
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
          mark: { type: 'geoshape', stroke: '#fff', strokeWidth: 0.5 },
          encoding: {
            shape: { field: 'geo', type: 'geojson' },
            color: {
              field: { repeat: 'repeat' },
              type: 'quantitative',
              scale: { domain: [400000, 1800000], scheme: 'reds' },
              legend: { format: '.2s', title: 'Median price' },
            },
            tooltip: [
              { field: 'locality', type: 'nominal', title: 'Suburb' },
              {
                field: { repeat: 'repeat' },
                type: 'quantitative',
                title: 'Median Price',
                format: ',',
              },
            ],
          },
        },
        {
          data: {
            values: [
              {
                '2010': 'Year: 2010',
                '2012': 'Year: 2012',
                '2014': 'Year: 2014',
                '2016': 'Year: 2016',
                '2018': 'Year: 2018',
                '2020': 'Year: 2020',
              },
            ],
          },
          mark: {
            type: 'text',
            align: 'right',
            baseline: 'bottom',
            x: 'width',
            y: 0,
          },
          encoding: { text: { field: { repeat: 'repeat' } } },
        },
      ],
    },
  }"
/>
---
layout: two-cols
zoom: 0.86
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Explain the code</p>

# `repeat`

- Line `4`: create one view for each listed field.
- Line `5`: arrange the repeated views in two columns.
- Line `6`: `spec` is the template reused for every view.
- Line `58`: colour uses the current repeated field.
- Line `66`: tooltip also uses the current repeated field.

::right::

<div style="overflow-y: auto; max-height: 500px;">

```json {4|5|6|all} {lines:true,startLine:1}
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "title": "Median house price per suburb",
  "repeat": ["2010", "2012", "2014", "2016", "2018", "2020"],
  "columns": 2,
  "spec": {
    ...
  }
}
```

```json {58|66|all} {lines:true,startLine:55}
"encoding": {
  "shape": {"field": "geo", "type": "geojson"},
  "color": {
    "field": {"repeat": "repeat"},
    "type": "quantitative",
    "scale": {"domain": [400000, 1800000], "scheme": "reds"}
  },
  "tooltip": [
    {"field": "locality", "type": "nominal", "title":
    "Suburb"},
    {
      "field": {"repeat": "repeat"},
      "type": "quantitative",
      "title": "Median Price"
    }
  ]
}
```

</div>
---
layout: two-cols
zoom: 0.86
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Explain the code</p>

# Manual year labels

- Lines `75-86`: create one inline row containing labels for every year.
- Lines `87-93`: draw a text mark in the top-right of each repeated view.
- Line `94`: choose the correct label using the current repeated field.
- This workaround is needed because repeated view titles are not easy to set dynamically.
---
layout: default
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Practice</p>

# Modify the small multiples

Try one change before looking at the preview again:

- change the years in `repeat`
- change `columns` from `2` to `3`
- remove the text label layer and compare readability
- change the colour scheme
---
layout: default
zoom: 0.74
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Solution preview</p>

# Small multiples with `repeat` solution preview

<VegaLitePlayground
  title="Six repeated choropleth views"
  :height="340"
  :initialSpec="{
    '$schema': 'https://vega.github.io/schema/vega-lite/v5.json',
    title: 'Median house price per suburb',
    repeat: ['2010', '2012', '2014', '2016', '2018', '2020'],
    columns: 2,
    spec: {
      projection: {
        type: 'equirectangular',
        center: [144.4, -37.6],
        scale: 21000,
      },
      width: 210,
      height: 160,
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
            url: 'https://raw.githubusercontent.com/FIT3179/Vega-Lite/main/6_advanced_examples/data/house_price_by_suburb_wide_format.csv',
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
          mark: { type: 'geoshape', stroke: '#fff', strokeWidth: 0.5 },
          encoding: {
            shape: { field: 'geo', type: 'geojson' },
            color: {
              field: { repeat: 'repeat' },
              type: 'quantitative',
              scale: { domain: [400000, 1800000], scheme: 'reds' },
              legend: { format: '.2s', title: 'Median price' },
            },
            tooltip: [
              { field: 'locality', type: 'nominal', title: 'Suburb' },
              {
                field: { repeat: 'repeat' },
                type: 'quantitative',
                title: 'Median Price',
                format: ',',
              },
            ],
          },
        },
        {
          data: {
            values: [
              {
                '2010': 'Year: 2010',
                '2012': 'Year: 2012',
                '2014': 'Year: 2014',
                '2016': 'Year: 2016',
                '2018': 'Year: 2018',
                '2020': 'Year: 2020',
              },
            ],
          },
          mark: {
            type: 'text',
            align: 'right',
            baseline: 'bottom',
            x: 'width',
            y: 0,
          },
          encoding: { text: { field: { repeat: 'repeat' } } },
        },
      ],
    },
  }"
/>


::right::

<div style="overflow-y: auto; max-height: 460px;">

```json {75-86|87-93|94|all} {lines:true,startLine:74}
{
  "data": {
    "values": [
      {
        "2010": "Year: 2010",
        "2012": "Year: 2012",
        "2014": "Year: 2014",
        "2016": "Year: 2016",
        "2018": "Year: 2018",
        "2020": "Year: 2020"
      }
    ]
  },
  "mark": {
    "type": "text",
    "align": "right",
    "baseline": "bottom",
    "x": "width",
    "y": 0
  },
  "encoding": {"text": {"field": {"repeat": "repeat"}}}
}
```

</div>
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
---
layout: default
---
<p class="text-xs uppercase tracking-[0.18em] text-slate-500">Reminder</p>

# Before next week

- Test 2 is during the `Week 11` workshop.
- Keep building `DV2` charts, map, layout, and interactions.
- Make static charts work before adding interactions.
- Bring one specific code question to consultation or Ed.
