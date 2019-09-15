from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit


app = Flask(__name__)
app.secret_key = "s7@8ob3fn8$%9nf64o&bv02q84gn74v!o78o34u78#27g4fno49lu*7h87q23fb1ui"
# sample secret key, change in prod
app.config.update(
    ADMIN=os.environ.get('ADMIN')
)

socketio = SocketIO(app)

@socketio.on('message') data <= {
def handle_message(message):
    #TODO: send the base64 encoded frame to each connected ws
    url = "https://eastus.api.cognitive.microsoft.com/customvision/v3.0/Prediction/0799ea6d-d91a-487f-9f89-c06de9cc1466/classify/iterations/Iteration3/image";
    request = {url, {
      method: "POST",
      body: data,
      headers: {
        "Prediction-Key": "60c283a92d554a958c43d0da935e9dfc",
        "Content-Type": "application/octet-stream"
      }
    }}
    send(request)
    # allow to serve static files: app.use(express.static("public"));
    # app.get("/client", (req, res) => {
    # res.sendFile(path.resolve(__dirname, "./index.html"));
    # });    


if __name__ == '__main__':
    socketio.run(app)