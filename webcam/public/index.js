var video = document.querySelector("#videoElement");
var canvas = document.createElement("canvas");

if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({video: { width: 426, height: 240 }})
        .then(function (stream) {
            video.srcObject = stream;
        })
        .catch((e) => {console.error(e)});

    const WS_URL = 'ws://localhost:3001';
    const ws = new WebSocket(WS_URL);
    ws.onopen = () => {
        console.log(`Connected to ${WS_URL}`);
        setInterval(() => {
            const canvas = document.createElement('canvas');
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            canvas.getContext('2d').drawImage(video, 0, 0);
            canvas.toBlob((b) => {
                ws.send(b);
            })
        }, 3000);
    }

    ws.onmessage = message => {
        console.log(message);
        const slouchRoot = document.querySelector('#slouch');
        data = JSON.parse(message.data);
        console.log(data);
        slouchRoot.textContent = data.predictions[0].tagName;
        request.open('GET', 'https://ghibliapi.herokuapp.com/films', true)
        //TODO: connect to py backend at localhost:4999/users/update to update # slouch

    }
}

// async function takePicture() {
//     let context = canvas.getContext("2d");

//     let width = 1280;
//     let height = 720;

//     context.drawImage(video, 0, 0, width, height);

//     const data = canvas.toBlob(async (b) => {

//             let url = "https://eastus.api.cognitive.microsoft.com/customvision/v3.0/Prediction/0799ea6d-d91a-487f-9f89-c06de9cc1466/classify/iterations/Iteration3/image";

//             fetch(url, {
//                 method: 'POST',
//                 body: b,
//                 headers: {
//                     "Prediction-Key": "60c283a92d554a958c43d0da935e9dfc",
//                     "Content-Type": "application/octet-stream"
//                 }
//             })
//             .then((res) => {
//                 return res.json();
//             })
//             .then((res) => {
//                 console.log(res);
//             })
//             .catch((e) => {
//                 console.error(e);
//             })
        
//     })
// }