export default {
  axis: {
    style: {
      axis: {
        fill: "#69bed6",
        stroke: "#69bed6",
        strokeWidth: 1
      },
      grid: {
        fill: "none",
        stroke: "none",
        pointerEvents: "painted"
      },
      ticks: {
        fill: "transparent",
        size: 1,
        stroke: "#69bed6"
      },
      tickLabels: {
        fill: "#69bed6"
      }
    }
  },
  bar: {
    style: {
      data: {
        fill: "#ffffff",
        padding: 8,
        strokeWidth: 0
      }
    }
  },
  boxplot: {
    style: {
      max: {
        padding: 8,
        stroke: "#ffffff",
        strokeWidth: 1
      },
      median: {
        padding: 8,
        stroke: "#ffffff",
        strokeWidth: 1
      },
      min: {
        padding: 8,
        stroke: "#ffffff",
        strokeWidth: 1
      },
      q1: {
        padding: 8,
        fill: "#ffffff"
      },
      q3: {
        padding: 8,
        fill: "#ffffff"
      }
    },
    boxWidth: 20
  },
  legend: {
    Colorscale: ["#69bed6"],
    gutter: 10,
    orientation: "vertical",
    titleOrientation: "top",
    style: {
      data: {
        type: "circle"
      }
    }
  },
  line: {
    style: {
      data: {
        fill: "#69bed6",
        stroke: "#69bed6",
        strokeWidth: 2
      }
    }
  },
  pie: {
    style: {
      data: {
        padding: 10,
        stroke: "transparent",
        strokeWidth: 1
      }
    },
    Colorscale: ["#69bed6"],
    width: 400,
    height: 400,
    padding: 50
  },
  scatter: {
    style: {
      data: {
        fill: "#69bed6",
        stroke: "transparent",
        strokeWidth: 0
      }
    }
  },
  stack: {
    colorscale: ["#69bed6"]
  },
  voronoi: {
    style: {
      data: {
        fill: "transparent",
        stroke: "transparent",
        strokeWidth: 0
      },
      flyout: {
        stroke: "#69bed6",
        strokeWidth: 1,
        fill: "#f0f0f0",
        pointerEvents: "none"
      }
    }
  }
};
