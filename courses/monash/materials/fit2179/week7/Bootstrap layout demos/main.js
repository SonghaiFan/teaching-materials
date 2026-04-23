async function embedChart(selector, spec, options = {}) {
  const element = document.querySelector(selector);
  if (!element || typeof vegaEmbed === "undefined") return;

  element.innerHTML = "";

  await vegaEmbed(selector, spec, {
    actions: false,
    renderer: "svg",
    ...options,
  });
}

const storyBarSpec = {
  $schema: "https://vega.github.io/schema/vega-lite/v6.json",
  width: "container",
  height: 300,
  data: {
    values: [
      { category: "Asia", value: 42 },
      { category: "Europe", value: 35 },
      { category: "Africa", value: 28 },
      { category: "Americas", value: 31 },
      { category: "Oceania", value: 18 },
    ],
  },
  mark: "bar",
  encoding: {
    x: {
      field: "category",
      type: "nominal",
      axis: { labelAngle: 0, title: null },
    },
    y: {
      field: "value",
      type: "quantitative",
      title: "Value",
    },
    tooltip: [
      { field: "category", type: "nominal" },
      { field: "value", type: "quantitative" },
    ],
  },
};

embedChart("#vis-main", storyBarSpec);
