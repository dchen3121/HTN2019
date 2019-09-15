import React from "react";
import "./App.css";
import Statistics from "./Stats";
import Webcam from "./Webcam";
import Graph from "./Graph";
import Transition from "react-addons-css-transition-group";

class Navigation extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div
        style={{
          height: "100px",
          backgroundColor: "white",
          width: "100%",
          position: "fixed",
          top: 0,
          boxShadow: "0 1px 6px 0 rgba(32,33,36,0.28)"
        }}
      >
        <nav style={{}}>
          <Transition
            transitionName="nave"
            transitionAppear={true}
            transitionAppearTimeOut={350}
            transitionEnterTimeout={350}
            transitionLeaveTimeout={350}
          >
            <div>
              <li id="place" onClick={this.props.toVideo}>
                VIDEO
              </li>
              <li id="place" onClick={this.props.toData}>
                DATA
              </li>
              <li style={{ right: 0, fontWeight: "bolder" }}>
                {this.props.slouchStatus ? "SLOUCHED" : "NOT SLOUCHED"}
              </li>
            </div>
          </Transition>
        </nav>
      </div>
    );
  }
}

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isSlouch: false,
      page: null
    };

    this.toVideo = this.toVideo.bind(this);
    this.toData = this.toData.bind(this);
    this.state = {
      slouchedBefore: false
    }
  }

  componentDidMount() {
    this.setState({
      page: "video"
    });
  }

  toVideo() {
    console.log("video");
    this.setState({
      page: "video"
    });
  }

  toData() {
    console.log("data");
    this.setState({
      page: "data"
    });
  }

  changeSlouch(slouchStatus) {
    console.log(slouchStatus);
    if (slouchStatus === "slouch") {
      if (this.state.slouchedBefore) {
        return;
      }
      this.setState({
        slouchedBefore: true
      })
      new Notification("You're slouching! Correct your posture");
      this.setState({
        isSlouch: true
      });
    } else {
      this.setState({
        slouchedBefore: false
      })
      this.setState({
        isSlouch: false
      });
    }
  }

  render() {
    console.log(this.state.isSlouch);
    return (
      <div>
        <Navigation
          page={this.state.page}
          toVideo={this.toVideo}
          toData={this.toData}
          slouchStatus={this.state.isSlouch}
        ></Navigation>
        {this.state.page === "video" ? <Webcam
          display={this.state.page === "video" ? "visible" : "hidden"}
          page={this.state.page}
          changeSlouch={slouchStatus => this.changeSlouch(slouchStatus)}
        /> : <Graph id="Graph"/>} 
      </div>
    );
  }
}

export default App;

{
  /* <div className="App" id="content">
            <div id="Graph">
              <Graph />
            </div>
            <div id="Stats">
            <Statistics />
          </div>
          </div> */
}
