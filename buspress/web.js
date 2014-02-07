var express = require("express");
var app = express();
app.use(express.logger());
app.use(express.bodyParser());
var cloudinary = require("cloudinary");
var fs = require("node-fs");
var http = require("client-http");
var url = require("url");
var request = require("request");
//var img64 = require("img64");
var base64 = require("base64-stream");
//var mysql = require("mysq");
var jsoncsv = require("jsoncsv");

//-----------------------------------------------------------------------------------------
var tm = function() {
    var date = new Date();
    var hour = date.getHours();
    hour = (hour < 10 ? "0" : "") + hour;
    var min  = date.getMinutes();
    min = (min < 10 ? "0" : "") + min;
    var sec  = date.getSeconds();
    sec = (sec < 10 ? "0" : "") + sec;
    var year = date.getFullYear();
    var month = date.getMonth() + 1;
    month = (month < 10 ? "0" : "") + month;
    var day  = date.getDate();
    day = (day < 10 ? "0" : "") + day;
    var ts = year + "-" + month + "-" + day + "-" + hour + "-" + min + "-" + sec;
    console.log("TIMESTAMP IS " + ts);
    return ts;
};
//-------------------------------------------------------------------------------------------
app.get('/', function(request, response) {
  console.log("RETURNING NOW " + tm());
  response.send('This is immense-reef-2061 ' + tm());
});
//-----------------------------------------------------------------------------------------
var port = process.env.PORT || 3000;
app.listen(port, function() {
  console.log("Listening on " + port);
});
//-------------------------------------------------------------------------------------------
