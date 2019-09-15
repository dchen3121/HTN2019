import React from "react";
import request from "request";

class Webcam extends React.Component {
  establishWebcam() {
    var video = document.querySelector("video");
    // var canvas = document.createElement("canvas");

    if (navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices
        .getUserMedia({
          video: {
            width: 750,
            height: 350
          }
        })
        .then(function (stream) {
          video.srcObject = stream;
        })
        .catch(e => {
          console.error(e);
        });

      setInterval(() => {
        const canvas = document.createElement("canvas");
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        canvas.getContext("2d").drawImage(video, 0, 0);
        canvas.toBlob(async (b) => {
          let oReq = new XMLHttpRequest();
          oReq.open("POST", "https://eastus.api.cognitive.microsoft.com/customvision/v3.0/Prediction/0799ea6d-d91a-487f-9f89-c06de9cc1466/classify/iterations/Iteration7/image")
          oReq.setRequestHeader("Prediction-Key", "60c283a92d554a958c43d0da935e9dfc")
          oReq.setRequestHeader("Content-Type", "application/octet-stream")

          oReq.onreadystatechange = () => {
            if(oReq.readyState === 4) {
              this.props.changeSlouch(JSON.parse(oReq.response).predictions[0].tagName);
            }
          }

          oReq.send(b);
        })
      }, 1000)

    }
  }

  componentDidMount() {
    this.establishWebcam();
  }

  render() {
    return ( 
    <div className="webcam">
      <video autoplay="true" id="videoElement"></video>
      <div id="info">
        <p id="slouch"></p>
      </div> 
    </div>
    );
  }
}

export default Webcam;