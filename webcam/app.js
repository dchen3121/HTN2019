const path = require("path");
const express = require("express");
const WebSocket = require("ws");
const app = express();
const request = require("request-promise");

const WS_PORT = process.env.WS_PORT || 3001;
const HTTP_PORT = process.env.HTTP_PORT || 3000;

const wsServer = new WebSocket.Server({ port: WS_PORT }, () =>
  console.log(`WS server is listening at ws://localhost:${WS_PORT}`)
);

// array of connected websocket clients
let connectedClients = [];

wsServer.on("connection", (ws, req) => {
  console.log("Connected");
  // add new connected client
  connectedClients.push(ws);
  // listen for messages from the streamer, the clients will not send anything so we don't need to filter
  ws.on("message", data => {
    // send the base64 encoded frame to each connected ws
    let url =
      "https://eastus.api.cognitive.microsoft.com/customvision/v3.0/Prediction/0799ea6d-d91a-487f-9f89-c06de9cc1466/classify/iterations/Iteration3/image";
    request(url, {
      method: "POST",
      body: data,
      headers: {
        "Prediction-Key": "60c283a92d554a958c43d0da935e9dfc",
        "Content-Type": "application/octet-stream"
      }
    })
      .then(res => {
        return res;
      })
      .then(res => {
        console.log(res);
        connectedClients.forEach((ws, i) => {
          if (ws.readyState === ws.OPEN) {
            // check if it is still connected
            ws.send(res); // send
          } else {
            // if it's not connected remove from the array of connected ws
            connectedClients.splice(i, 1);
          }
        });
      })
      .catch(e => {
        console.error(e);
      });
    // Don't need this block, we need to send data to openpose
  });
});

app.use(express.static("public"));

app.get("/client", (req, res) => {
  res.sendFile(path.resolve(__dirname, "./index.html"));
});

app.listen(HTTP_PORT, () => {
  console.log(`HTTP server listening at http://localhost:${HTTP_PORT}`);
});
