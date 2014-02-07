var cloudinary = require("cloudinary");
var underscore = require("underscore")
var backbone = require("backbone");
var fs = require("node-fs");
var http = require("client-http");
var url = require("url");
var request = require("request");
//var app = express();
var pg = require('pg');
//app.use(express.logger());
//app.use(app.router);
var img64 = require("img64");
var base64 = require("base64-stream");
//-------------------------------------------------------------------------------------------
//development
//-------------------------------------------------------------------------------------------
function getDateTime() {
    var date = new Date();
    console.log("date " + date);
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
    return year + "-" + month + "-" + day + "-" + hour + "-" + min + "-" + sec;
}
//-------------------------------------------------------------------------------------------
cloudinary.config({ 
  cloud_name: 'lcbklf5b3', 
  api_key: '876552226582264',
  api_secret: 'vAIdVdyFhfT_4Zb1iAZORNyQxLs'
});
//-------------------------------------------------------------------------------------------
var base64_data = fs.readFileSync('mobile.png').toString('base64');
//-------------------------------------------------------------------------------------------
getdata = function(base64String) {
  var dStr = 'decode.str';
  var filename = 'encode.png';
  var newname = 'encode' + '-' + getDateTime();

  fs.writeFile(dStr, base64String, function(err) {
    if(err) {
        console.log(err);
     } else {
        console.log("File " + dStr + " was saved!");
     }
  }); 
  var buf = new Buffer(base64_data,'base64');
  fs.writeFile(filename, buf, function(err) {
    if(err) {
        console.log(err);
    } else {
       cloudinary.uploader.upload(filename, function(result) { 
           console.log(result)}, 
       { public_id: newname }); 

       cloudinary.image(filename, { width: 100, height: 150, crop: "fill" })
       console.log("File " + filename + " was saved!");
    }
  }); 
}
//-------------------------------------------------------------------------------------------
// Test function
getdata(base64_data);
//-------------------------------------------------------------------------------------------
