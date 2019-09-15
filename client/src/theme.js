export default {
  axis: {
    style: {
      axis: {
        fill: "#ffffff",
        stroke: "#ffffff",
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
        stroke: "#ffffff"
      },
      tickLabels: {
        fill: "#ffffff"
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
    Colorscale: ["#ffffff"],
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
        fill: "#ffffff",
        stroke: "#ffffff",
        strokeWidth: 2
      }
    }
  },
  stack: {
    colorscale: ["#ffffff"]
  }
};
