const visContainers = document.querySelectorAll("[data-vega-spec]");

function normaliseSpec(rawSpec) {
  const existingConfig = rawSpec.config ?? {};
  const existingLegend = existingConfig.legend ?? {};

  return {
    ...rawSpec,
    width: rawSpec.width ?? "container",
    padding: rawSpec.padding ?? { top: 12, right: 20, bottom: 36, left: 44 },
    autosize: rawSpec.autosize ?? {
      type: "fit-x",
      contains: "padding",
      resize: true,
    },
    config: {
      ...existingConfig,
      legend: {
        orient: "bottom",
        direction: "horizontal",
        title: null,
        labelLimit: 120,
        ...existingLegend,
      },
    },
  };
}

async function renderVisualisations() {
  if (typeof vegaEmbed === "undefined") {
    return;
  }

  for (const container of visContainers) {
    const specPath = container.getAttribute("data-vega-spec");

    if (!specPath) {
      continue;
    }

    try {
      const response = await fetch(specPath);
      const spec = await response.json();

      await vegaEmbed(container, normaliseSpec(spec), {
        // actions: false,
        renderer: "svg",
      });
    } catch (error) {
      container.textContent = "Unable to load visualisation.";
      console.error(`Failed to render ${specPath}`, error);
    }
  }
}

renderVisualisations();
