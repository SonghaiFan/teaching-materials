function barchart() {
  var spec = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "description": "A simple bar chart with embedded data.",
    "autosize": { "type": "fit-x", "contains": "padding" },
    "width": "container",
    "height": 400,
    "background": "white",
    "data": {
      "url": "https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/7_OneCatOneNum_header.csv"
    },
    "mark": "bar",
    "encoding": {
      "x": {
        "field": "Country",
        "type": "nominal",
        "axis": { "labelAngle": -45 }
      },
      "y": {
        "field": "Value",
        "type": "quantitative"
      },
      "color": { "value": "#69b3a2" }
    }
  };

  vegaEmbed('#viz1', spec);
}

export { barchart };
