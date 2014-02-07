var express = require("express");
var cloudinary = require("cloudinary");
var underscore = require("underscore")
var backbone = require("backbone");
var fs = require("node-fs");
var http = require("client-http");
var url = require("url");
var request = require("request");
var app = express();
var pg = require('pg');
app.use(express.logger());
app.use(app.router);
var img64 = require("img64");
var base64 = require("base64-stream");
//-------------------------------------------------------------------------------------------
//development
//-------------------------------------------------------------------------------------------
cloudinary.config({ 
  cloud_name: 'lcbklf5b3', 
  api_key: '876552226582264',
  api_secret: 'vAIdVdyFhfT_4Zb1iAZORNyQxLs'
});
//-------------------------------------------------------------------------------------------
var img = "https://res.cloudinary.com/lcbklf5b3/image/upload/t_media_lib_thumb/v1379442111/logo_lpg70n.png";
//-------------------------------------------------------------------------------------------
var newdata;   
setdata = function(parm) {
  newdata=parm; 
  //console.log(getparmdata());
}
getparmdata = function() {
     var jString = JSON.stringify({
         data: newdata});
     return jString;
}
//-------------------------------------------------------------------------------------------
getdata = function() {
  var base64_data = fs.readFileSync('mobile.png').toString('base64');
  console.log(base64_data);

  fs.writeFile("decode.png", base64_data, function(err) {
    if(err) {
           console.log(err);
     } else {
           console.log("The file was saved!");
           //console.log(buf);
     }
  }); 

  var buf = new Buffer(base64_data,'base64');

  fs.writeFile("encode.png", buf, function(err) {
    if(err) {
        console.log(err);
    } else {
        console.log("The file was saved!");
    }
  }); 
  /*
  var fileName = 'decode.png';
  fs.exists(fileName, function(exists) {
    if (exists) {
      fs.stat(fileName, function(error, stats) {
        fs.open(fileName, "r", function(error, fd) {
          var buffer = new Buffer(stats.size);
          fs.read(fd, buffer, 0, buffer.length, null, function(error, bytesRead, buffer) {
            data = buffer.toString("utf8", 0, buffer.length);
            setdata(data);
            var b64string= data;
            var buf = new Buffer(base64_data,'base64');

            fs.writeFile("encode.png", buf, function(err) {
               if(err) {
                    console.log(err);
               } else {
                    console.log("The file was saved!");
               }
            }); 
            fs.close(fd);
          });
        });
      });
    }
  });
  */
}
getdata();
