var express = require("express");
var easypost = require("easypost");
var app = express();
app.use(express.logger());
app.use(express.bodyParser());
var cloudinary = require("cloudinary");
var fs = require("node-fs");
var http = require("client-http");
var url = require("url");
var request = require("request");
var img64 = require("img64");
var base64 = require("base64-stream");

//-----------------------------------------------------------------------------------------
cloudinary.config({ 
  cloud_name: 'lcbklf5b3', 
  api_key: '876552226582264',
  api_secret: 'vAIdVdyFhfT_4Zb1iAZORNyQxLs'
});
//-------------------------------------------------------------------------------------------
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
var sendToCloud = function(base64String) {
  var filename = 'encode.png';
  var newname = 'encode' + '-' + tm();

  var buf = new Buffer(base64String,'base64');
  fs.writeFile(filename, buf, function(err) {
    if(err) {
        console.log(err);
    } else {
       cloudinary.uploader.upload(filename, function(result) { 
           //console.log(result),           
           console.log("File " + filename + " was saved!"),
           cloudinary.image(filename, { width: 100, height: 150, crop: "fill" })},
       { public_id: newname }); 
    }
  }); 
}
//-------------------------------------------------------------------------------------------
app.post('/sendToCloud', function(req, res){
  console.log("BASE64-IMAGE coming from tablet ");
  console.log("Status  " + res.statusCode);

  var js = JSON.stringify(req.body);
  //console.log('body: ' + js);

  var jparse = JSON.parse(js);
  var jbody = jparse.name;
  //console.log('body: ' + jbody);
  sendToCloud(jbody);

  res.send(null);
});
//-------------------------------------------------------------------------------------------
app.post('/sendTest', function(request, response)  {
  //var base = request.param('name');
  console.log("from client");
  console.log('body: ' + JSON.stringify(request.body));
  //var msg = "Parameter info is " + base;

  //sendToCloud(base);
  response.send(null);
})
//-------------------------------------------------------------------------------------------
app.post('/sendPost/:id', function(request, response)  {
  var base = request.params.id;
  console.log("BASE64-IMAGE " + base);
  var msg = "Parameter post info is " + base;

  //sendToCloud(base);
  response.send(msg);
});
//-------------------------------------------------------------------------------------------
app.get('/sendimage/:id', function(request, response, body)  {
  var p = request.params.id;

  console.log("PARAM " + p);
  var msg = "Sending image";

  var fimg = "http://res.cloudinary.com/lcbklf5b3/raw/upload/v1383329790/decodestr";
  var gimg = cloudinary.url(fimg);
  msg = msg + "<br><br>" + gimg;

  var http = require('http');

  var request = http.get(gimg, function(res) {
      var str = '';
      res.on('data', function(chunk) {
       str += chunk; 
      });   
      res.on('end', function() {
        //console.log('AT END '  + str);
        sendToCloud(str);
      });   
  });   
  response.send(msg);
});
//-------------------------------------------------------------------------------------------
app.get('/', function(request, response) {
  console.log("RETURNING NOW " + tm());
  response.send('This is immense-reef-2061 ' + tm());
});
//-----------------------------------------------------------------------------------------
var port = process.env.PORT || 5000;
app.listen(port, function() {
  console.log("Listening on " + port);
});
//-------------------------------------------------------------------------------------------
