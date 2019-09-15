import React from "react";
import {
  VictoryBar,
  VictoryChart,
  VictoryTheme,
  VictoryAxis,
  VictoryLabel
} from "victory";

// TO DO: FIX THIS DATA AS WELL AS JSON KEY VALUE PAIR NAMES
const data = [
  { quarter: 1, earnings: 1 },
  { quarter: 2, earnings: 2 },
  { quarter: 3, earnings: 3 },
  { quarter: 4, earnings: 4 },
  { quarter: 5, earnings: 5 },
  { quarter: 6, earnings: 6 },
  { quarter: 7, earnings: 7 }
];

class Graph extends React.Component {
  render() {
    return (
      <VictoryChart
        id="graph"
        // adding the material theme provided with Victory

        domainPadding={20}
      >
        <VictoryLabel text="Chart Title" x={175} y={30} textAnchor="middle" />
        {/*TO DO: FIX DATES to dynamically adjust */}
        <VictoryAxis
          tickFormat={[
            "Date 1",
            "Date 2",
            "Date 3",
            "Date 4",
            "Date 5",
            "Date 6",
            "Date 7"
          ]}
        />
        {/*TO DO: CHANGE AXES */}
        <VictoryAxis dependentAxis tickFormat={x => `${x}`} />
        <VictoryBar
          style={{ data: { fill: "#69bed6" } }}
          data={data}
          x="quarter"
          y="earnings"
        />
      </VictoryChart>
    );
  }
}
export default Graph;
