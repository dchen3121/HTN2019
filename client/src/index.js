import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import * as serviceWorker from "./serviceWorker";

ReactDOM.render(<App />, document.getElementById("root"));

var firebaseConfig = {
    apiKey: "AIzaSyBSO7IT5_sfrmwWq-qUH8iBskqq5N7A_08",
    authDomain: "htn2019-d987b.firebaseapp.com",
    databaseURL: "https://htn2019-d987b.firebaseio.com",
    storageBucket: "htn2019-d987b.appspot.com",
    serviceAccount: "do_not_commit/htn2019-d987b-firebase-adminsdk-pz1d6-52193b1ef8.json",
    projectId: "htn2019-d987b",
    messagingSenderId: "472926526203",
    appID: "1:472926526203:web:53ee8612353b83279dee5e",
  };

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
