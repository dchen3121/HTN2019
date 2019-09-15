import React from "react";
import {
  VictoryBar,
  VictoryChart,
  VictoryAxis,
  VictoryLabel,
  VictoryTheme
} from "victory";
import XYTheme from "./theme.js";

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

function generateData() {
  var result = {};
}

function last7Days() {
  var result = [];
  for (var i = 0; i < 7; i++) {
    var d = new Date();
    d.setDate(d.getDate() - i);
    result.push(d.getDate());
  }
  console.log(result);
  return result;
}

function getDataset() {
  let oReq = new XMLHttpRequest();
  oReq.open("GET", "localhost:4999/data/week");
  var response = oReq.response;
  console.log("SUCCESS");
  console.log(response);
  var final = {};
  for (var i = 0; i < 7; i++) {
    final[i] = { x: response[i].numSlouch, y: response[i].date };
    // do something with "key" and "value" variables
  }
  return final;
}
class Graph extends React.Component {
  constructor() {
    super();
    this.state = {
      dates: last7Days()
    };
  }

  render() {
    return (
      <VictoryChart
        id="graph"
        // adding the material theme provided with Victory
        theme={XYTheme}
        domainPadding={20}
      >
        <VictoryLabel
          text="Slouches in September"
          x={175}
          y={30}
          textAnchor="middle"
        />
        {/*TO DO: FIX DATES to dynamically adjust */}
        <VictoryAxis
          axisLabelComponent={["S", "M", "T", "W", "TH", "F", "S"]}
        />
        {/*TO DO: CHANGE AXES */}
        <VictoryAxis dependentAxis tickFormat={x => `${x}`} />
        <VictoryBar
          barRatio={0.5}
          horizontal={true}
          style={{ data: { fill: "#69bed6" } }}
          data={data}
          x="slouchCount"
          y="day"
        />
      </VictoryChart>
    );
  }
}
export default Graph;
