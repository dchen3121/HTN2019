export default {
  axis: {
    style: {
      axis: {
        fill: "#373738",
        stroke: "#373738",
        strokeWidth: 1
      },
      grid: {
        fill: "none",
        stroke: "none",
        pointerEvents: "painted"
      },
      ticks: {
        fill: "#373738",
        size: 1,
        stroke: "#373738"
      },
      tickLabels: {
        fill: "#373738"
      }
    }
  },
  bar: {
    style: {
      data: {
        fill: "#373738",
        padding: 8,
        strokeWidth: 0
      }
    }
  },
  boxplot: {
    style: {
      max: {
        padding: 8,
        stroke: "#373738",
        strokeWidth: 1
      },
      median: {
        padding: 8,
        stroke: "#373738",
        strokeWidth: 1
      },
      min: {
        padding: 8,
        stroke: "#373738",
        strokeWidth: 1
      },
      q1: {
        padding: 8,
        fill: "#373738"
      },
      q3: {
        padding: 8,
        fill: "#373738"
      }
    },
    boxWidth: 20
  },
  legend: {
    Colorscale: ["#373738"],
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
        fill: "#373738",
        stroke: "#373738",
        strokeWidth: 2
      }
    }
  },
  stack: {
    colorscale: ["#373738"]
  }
};
