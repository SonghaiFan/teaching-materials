function drawBarChart() {
  const spec = {
    $schema: "https://vega.github.io/schema/vega-lite/v5.json",
    width: 500,
    height: 300,
    data: {
      values: [
        { day: "Mon", count: 1820 },
        { day: "Tue", count: 1760 },
        { day: "Wed", count: 1940 },
        { day: "Thu", count: 2010 },
        { day: "Fri", count: 2280 },
        { day: "Sat", count: 1560 },
        { day: "Sun", count: 1320 }
      ]
    },
    mark: "bar",
    encoding: {
      x: { field: "day", type: "ordinal", title: "Day" },
      y: { field: "count", type: "quantitative", title: "Average hourly counts" }
    }
  };

  vegaEmbed("#vis", spec, { actions: false });
}

export { drawBarChart };
