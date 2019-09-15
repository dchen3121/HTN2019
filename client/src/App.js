import React from "react";
import "./App.css";
import Statistics from "./Stats";
import Webcam from "./Webcam";
import Graph from "./Graph";

class App extends React.Component {
  constructor() {
    super();
    this.state = {
      isSlouch: false
    };
  }

  changeSlouch(slouchStatus) {
    console.log(slouchStatus);
    if (slouchStatus === "slouched") {
      this.setState({
        isSlouch: true
      });
    } else {
      this.setState({
        isSlouch: false
      });
    }
  }

  render() {
    return (
      <div id="content">
        <div id="Webcam">
          <Webcam
            changeSlouch={slouchStatus => this.changeSlouch(slouchStatus)}
          />
        </div>
        <div className="App" id="content">
          <div id="Graph">
            <Graph />
          </div>
          {/*<div id="Stats">
            <Statistics />
          </div>*/}
        </div>
      </div>
    );
  }
}

export default App;
