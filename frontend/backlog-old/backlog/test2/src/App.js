import React from "react";
import "./App.css";
import Statistics from "./Stats";
import Webcam from "./Webcam";
import BarGraph from "./BarGraph";

function App() {
  return (
    <div className="App">
      <div>
        <Statistics />
      </div>
      <div>
        <Webcam />
      </div>
    </div>
  );
}

export default App;
