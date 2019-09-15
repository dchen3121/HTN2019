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
const sampleData = [
  { x: 2, y: 32 },
  { x: 4, y: 24 },
  { x: 6, y: 16 },
  { x: 8, y: 29 },
  { x: 10, y: 40 },
  { x: 12, y: 36 },
  { x: 14, y: 47 },
  { x: 16, y: 47 },
  { x: 18, y: 53 },
  { x: 20, y: 43 },
  { x: 22, y: 62 },
  { x: 24, y: 68 }
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
  }

  render() {
    return (
      <VictoryChart
        // adding the material theme provided with Victory
        theme={VictoryTheme.material}
        domainPadding={20}
      >
        <VictoryAxis
          tickValues={[1, 2, 3, 4, 5, 6, 7, 8]}
          tickFormat={["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00"]}
        />
        <VictoryAxis
          dependentAxis
          tickFormat={(x) => (`${x}`)}
        />
        <VictoryBar
          data={[
            {quarter: 1, earnings: 24},
            {quarter: 2, earnings: 29},
            {quarter: 3, earnings: 32},
            {quarter: 4, earnings: 24},
            {quarter: 5, earnings: 36},
            {quarter: 6, earnings: 38},
            {quarter: 7, earnings: 43},
            {quarter: 8, earnings: 59}
          ]}
          x="quarter"
          y="earnings"
        />
      </VictoryChart>
    );
  }
}
export default Graph;
