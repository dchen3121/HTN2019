import React from "react";
import request from "request";
import Transition from "react-addons-css-transition-group";

class Webcam extends React.Component {
  establishWebcam() {
    var video = document.querySelector("video");
    // var canvas = document.createElement("canvas");

    if (navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices
        .getUserMedia({
          video: {
            width: window.outerWidth + 500,
            height: window.outerHeight + 500
          }
        })
        .then(function(stream) {
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
        canvas.toBlob(async b => {
          let oReq = new XMLHttpRequest();
          oReq.open(
            "POST",
            "https://eastus.api.cognitive.microsoft.com/customvision/v3.0/Prediction/40e592e7-67fd-4e0f-9122-02d3631f7f4f/classify/iterations/Iteration1/image"
          );
          oReq.setRequestHeader(
            "Prediction-Key",
            "17b8411197b6462094a8292195f5725e"
          );
          oReq.setRequestHeader("Content-Type", "application/octet-stream");

          oReq.onreadystatechange = () => {
            if (oReq.readyState === 4) {
              let parsed = JSON.parse(oReq.response);
              if (!parsed.predictions) return;
              this.props.changeSlouch(parsed.predictions[0].tagName);
            }
          };

          oReq.send(b);
        });
      }, 5000);
    }
  }

  componentDidMount() {
    this.establishWebcam();
  }

  render() {
    return (
      <div>
        <div className="webcam">
          <video autoplay="true" id="videoElement"></video>
          <div id="info">
            <p id="slouch"></p>
          </div>
        </div>
      </div>
    );
  }
}

export default Webcam;
