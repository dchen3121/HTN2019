import React from "react";
import "./App.css";
import Statistics from "./Stats";
import Webcam from "./Webcam";
import Graph from "./Graph";

function App() {
  return (
    <div className="App" id="content">
      <div id="Graph">
        <Graph />
      </div>
      <div id="right">
        <div id="Webcam">
          <Webcam />
        </div>
        <br></br>
        <div id="Stats">
          <Statistics />
        </div>
      </div>
    </div>
  );
}

export default App;
