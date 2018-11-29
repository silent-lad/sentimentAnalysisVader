const express = require("express");
const logger = require("morgan");

var app = express();

app.use(logger("dev"));
app.use(express.urlencoded({ extended: false }));
app.use(express.json());

app.get("/", (req, res) => {
  //   var sentenceArray = JSON.parse(req.body);
  var python = require("child_process").spawn;
  var sentiment = python("python", ["./pythonVader/main.py", 9]);
  sentiment.stdout.on("data", function(data) {
    res.send(data.toString());
  });
});

app.listen(8080, () => {
  console.log("Listening");
});
