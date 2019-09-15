import React from "react";

class Statistics extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      title: "Statistics",
      stat1: "Times caught slouching",
      stat2: "Time spent slouching",
      stat3: "test"
    };
  }

  render() {
    return (
      <div class="stats">
        <h2>{this.state.title}</h2>
        <p>{this.state.stat1}</p>
        <p>{this.state.stat2}</p>
        <p>{this.state.stat3}</p>
      </div>
    );
  }
}

export default Statistics;
