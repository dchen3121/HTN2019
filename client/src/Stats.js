import React from "react";

class Stats extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      title: "Yoga Pose of the Day:",
      stat1: "Spinal Twist",
      stat2: "Benefits: Spine, Back, Hips"
    };
  }

  render() {
    return (
      <div class="stats">
        <h2>{this.state.title}</h2>
        <p>{this.state.stat1}</p>
        <p>{this.state.stat2}</p>
      </div>
    );
  }
}

export default Stats;
