//-------------------------------------------------------------------------------------------
//K Woodall
//-------------------------------------------------------------------------------------------
var express = require("express");
var cloudinary = require("cloudinary");
var getdatabase = require("./getDatabase.js");
var circle = require('./circle.js');
var getmytable = require('./mytable.js');
var underscore = require("underscore")
var backbone = require("backbone");
var fs = require("node-fs");
var http = require("client-http");
var url = require("url");
var request = require("request");
var app = express();
var pg = require('pg');
app.use(express.logger());
app.use(express.bodyParser());
app.use(app.router);
//var img64 = require("img64");
var base64 = require("base64-stream");
//-------------------------------------------------------------------------------------------
//development
//-------------------------------------------------------------------------------------------
var getbase64 = function(base64String) {
  var filename = 'encode.png';
  var newname = 'encode' + '-' + getDateTime();

  var buf = new Buffer(base64String,'base64');
  fs.writeFile(filename, buf, function(err) {
    if(err) {
        console.log(err);
    } else {
       cloudinary.uploader.upload(filename, function(result) { 
           console.log(result),           
           console.log("File " + filename + " was saved!"),
           cloudinary.image(filename, { width: 100, height: 150, crop: "fill" })},
       { public_id: newname }); 
    }
  }); 
}
//-------------------------------------------------------------------------------------------
cloudinary.config({ 
  cloud_name: 'lcbklf5b3', 
  api_key: '876552226582264',
  api_secret: 'vAIdVdyFhfT_4Zb1iAZORNyQxLs'

});
//-------------------------------------------------------------------------------------------
// urls
//-------------------------------------------------------------------------------------------
//app.get('/getimage/:id', function(request, response)  {
app.get('/getimage', function(request, response)  {
  //var p = request.params.id;
  //cloudinary.api.resources(function(result){}, { resource_type: 'raw' });
  //console.log("PARAM " + p);
  var msg = "<ul> <li>Getting cloudinary image </li> </ul>";
  //var lastmsg="You entered: " + p;
  msg = msg + "<br>" ;
  //var cimg = cloudinary.image("logo_lpg70n.jpg", { width: 100, height: 150, crop: "fill" })
  var cimg = cloudinary.image("contributemobile_xc1oyf.png", { width: 600, height: 100, crop: "fill" })
  var dimg = cloudinary.image("logo_lpg70n.png")
  var eimg = cloudinary.image("sample.png");
  var fimg = "http://res.cloudinary.com/lcbklf5b3/image/upload/c_fill,h_150,w_500/v1379440681/sample.jpg";
  var gimg = "http://res.cloudinary.com/lcbklf5b3/image/upload/v1388694801/encode-2014-01-02-20-33-21.png";

  var f = cloudinary.image(fimg);
  msg = msg + "<br><br>" + f;
  var g = cloudinary.image(gimg);
  msg = msg + "<br><br>" + g + "<br><br>" ;

  response.send(msg);
});
//-------------------------------------------------------------------------------------------
//app.get('/geteclipse/:id', function(request, response)  {
app.get('/geteclipse', function(request, response)  {
  //var p = request.params.id;
  var str = "";
  var idx = 0;  //global variable

  var conString = "postgres://cjvatmqpxnvimt:6gCrbHPOadjUwwn-DuhcTeMdfI@ec2-54-221-229-7.compute-1.amazonaws.com:5432/d5r8jc5o13gr9r";

  var client = new pg.Client(conString);
  client.connect(function(err) {
    client.query('SELECT  * FROM person', function(err, result) {
      if(err) {
        response.send(err);
      }
      var rval = JSON.stringify(result.rows);
      var jObj = JSON.parse(rval);    

      jObj.forEach(function(item) {    
           str = str + '<br>' + item.firstname + " " + item.lastname;  
      })
      response.send("Returning values " + str);
      //client.end();
    });
  });
});
//-------------------------------------------------------------------------------------------
//app.get('/getsql/:id', function(request, response)  {
app.get('/getsql', function(request, response)  {
  //var p = request.params.id;
  //console.log("PARAM " + p);
  var msg = "getting text";
  var str = "Listing of photo information " + '<br>';
  var idx = 0;  //global variable

  pg.connect(process.env.DATABASE_URL, function(err, client) {
     var query = client.query('SELECT * FROM mytable order by id desc');
     query 
     .on('row', function(row) {

       //arr[idx] = row.name;
       //console.log("FROM MYTABLE.JS " + arr[idx]);
       //idx++;

       if (row.imageurl == null) { 
           row.imageurl = "image not available"; 
       };

       var sp = "&nbsp&nbsp&nbsp&nbsp&nbsp";
       //str = str + '<br>' + row.name + sp + row.email + sp + row.description + sp + '<a href=' + '"' + row.imageurl + '"' + '>' + row.imageurl + '</a>';  

       str = str + '<br>' + row.name + '<br>' + row.email + '<br>' + row.description + '<br>' + '<a href=' + '"' + row.imageurl + '"' + '>' + row.imageurl + '</a>' + '<br>';  
       //str = str + row.name + '<br>';   
     })
     .on('end', function(row) {
         response.send(str);
         //response.send(str + "<br>" + process.env.DATABASE_URL);
         //client.end();
     });
  });
});
//-------------------------------------------------------------------------------------------
//app.get('/gettext/:id', function(request, response)  {
app.get('/gettext', function(request, response)  {
  //var p = request.params.id;
  //console.log("PARAM " + p);
  var msg = "getting text";

  var fimg = "http://res.cloudinary.com/lcbklf5b3/raw/upload/v1383329790/decodestr";

  var ximg = "http://res.cloudinary.com/lcbklf5b3/raw/upload/v1382378592/package.json";
  //var fimg = "http://res.cloudinary.com/lcbklf5b3/raw/upload/y.txt";
  var gimg = cloudinary.url(fimg);
  msg = msg + "<br><br>" + gimg;

  var http = require('http');

  //http.get(gimg, function(res) {
      //var buffer = '';
      //res.on('data', function(chunk) {
      //buffer += chunk; 
      //console.log('DATA ' + buffer);
      //getbase64(buffer);
      //msg = msg + buffer;

      //var jObj = JSON.parse(buffer);    
      //var lst = '';  
      //console.log('DATA JSON ' + jObj.top[0].id);
      //jObj.forEach(function(item) {    
      //     lst = lst + '<br>' + item.name;  
      //});
      //console.log('JSON LIST ' + lst);
      // response.send(lst);
      //response.send(buffer);
     //});   
  //});   
  response.send(msg);
});
//-------------------------------------------------------------------------------------------
app.get('/sendjson/:id', function(request, response)  {
  var p = request.params.id;
  var msg = "<ul> <li>sending json </li> </ul>";

  //cloudinary.api.delete_resources([p5],
  //   function(result){ console.log(result)});

  //cloudinary.api.delete_resources_by_prefix('pack',
  //  function(result){ console.log(result) });

  //cloudinary.api.tags(function(result) { console.log(result) });

  //cloudinary.api.resources(function(result){  console.log(result) },
  //  { type: 'upload', prefix: 'pack' });

  //cloudinary.uploader.destroy('http://res.cloudinary.com/lcbklf5b3/raw/upload/v1382640521/pass3.json', function(result) { console.log(result) });
  //cloudinary.uploader.destroy('http://res.cloudinary.com/lcbklf5b3/image/upload/v1388691877/encode-2014-01-02-19-44-37.png', function(result) { console.log(result) });

  //cloudinary.uploader.destroy('pass3.json', function(result) { console.log(result) });
  //cloudinary.uploader.destroy('Users/kwoodall/myapp/package2.json', function(result) { console.log(result) });

  //cloudinary.uploader.upload("package.json", 
  //                         function(result) { console.log(result) },
  //                         { public_id: "package.json",
  //                           resource_type: "raw" });

 response.send(msg + " " + p);
});
//-------------------------------------------------------------------------------------------
app.get('/getjson/:id', function(request, response)  {
  var p = request.params.id;

  console.log("PARAM " + p);
  var msg = "<ul> <li>getting json file </li> </ul>";

  var fimg = "http://res.cloudinary.com/lcbklf5b3/raw/upload/package.json";
  var gimg = cloudinary.url(fimg);
  msg = msg + "<br><br>" + gimg;

  var http = require('http');

  http.get(gimg, function(res) {
      var buffer = '';
      res.on('data', function(chunk) {
      buffer += chunk; 
      console.log('DATA ' + buffer);
      msg = msg + buffer;

      var jObj = JSON.parse(buffer);    
      var lst = '';  
      console.log('DATA JSON ' + jObj.name);
      //jObj.forEach(function(item) {    
           //lst = lst + '<br>' + jobj.name[0];  
      // });
      console.log('JSON LIST ' + lst);
      // response.send(lst);
      response.send(buffer + " " + lst);
     });   
  });   
  //response.send(msg);
});
//-------------------------------------------------------------------------------------------
app.get('/sendtext/:id', function(request, response)  {
  var p = request.params.id;

  var msg = "<ul> <li>sending file </li> </ul>";

//var txtFile = "http://res.cloudinary.com/lcbklf5b3/raw/upload/x.txt";

 cloudinary.uploader.upload("decode.txt", 
                           function(result) { console.log(result) },
                           { public_id: "decodestr",
                             resource_type: "raw" });

 var fimg = "http://res.cloudinary.com/lcbklf5b3/raw/upload/decode.txt";
 var u = cloudinary.url("decode.txt", { resource_type: "raw" } )

var fileName = fimg;

fs.exists(fileName, function(exists) {
  if (exists) {
    fs.stat(fileName, function(error, stats) {
      fs.open(fileName, "r", function(error, fd) {
        var buffer = new Buffer(stats.size);
 
        fs.read(fd, buffer, 0, buffer.length, null, function(error, bytesRead, buffer) {
          var data = buffer.toString("utf8", 0, buffer.length);
 
          //console.log('READING DATA ' + data);
          //console.log(data);
          //msg = data;
          fs.close(fd);
        });
      });
    });
  }
});

 msg = msg +  u;
 response.send(msg);

});
//-------------------------------------------------------------------------------------------
app.get('/geturl/:id', function(request, response)  {
  //console.log( 'The area of a circle of radius 4 is ' + result); 

  var p = request.params.id;
  var s = "{\"name\":\"" + p + "\"}";

  var u = "http://projects.reviewjournal.com/data/index8.php";
  var u1 = "http://projects.reviewjournal.com/data/index7.php?name="+ p;
  var u2 = "http://kwoodall.herokuapp.com/getmytable/" + p;

  var http = require('http');

  var surl = '/getmytable/' + p; 
  console.log('surl is ' + u1);

  http.get(u1, function(res) {
      var buffer = '';
      response.send("wassup");

      //res.on('data', function(chunk) {
      //buffer += chunk; 
      //console.log('DATA JSON ' + buffer);

      //var jObj = JSON.parse(buffer);    
      //var lst = '';  

      //console.log('DATA JSON ' + jObj.top[0].id);

      //jObj.forEach(function(item) {    
      //    lst = lst + '<br>' + item.name;  
      //});
      //console.log('JSON LIST ' + lst);
      //response.send(lst);
      //response.send(buffer);
     //});   

  });   
});
//-------------------------------------------------------------------------------------------
function doit() {
      console.log('HIT BUTTON');
      alert("Hit button");
}
//-------------------------------------------------------------------------------------------
app.get('/', function(request, response)  {

      function doit() {
       console.log('HIT BUTTON');
        alert("Hit button");
      }

      var variable = getmytable.variable(4);
      var h2 = "<h2>";  

      var d = "<br><input type=\"button\" value=\"Messaging\" onclick=\"doit()\">";
      //console.log("D PARAMETER IS " + d);

      var c = "<br><br><button onclick=\"doit()\">Display Message</button>";
      var b = "<button type=\"button\">Click Me!</button>"; 

      response.send("<h3>" + "nbr of rows loaded " + variable.length + "<br><h4>" + "name: " + variable[0] + "<br>" + d);
      //response.send("<h3>" + "nbr of rows loaded " + variable.length + "name: " + variable[0] + "<br>" + d);
      //response.send("<h3>" + "nbr of rows loaded " + "<br><h4>" + variable.length + "name: " + variable[0] + "<br>" + d);
});
//-------------------------------------------------------------------------------------------
app.get('/sendimage/:id', function(request, response)  {
  var p = request.params.id;

  var newfile = "http://res.cloudinary.com/lcbklf5b3/raw/upload/v1383329790/decodestr";
  var gimg = cloudinary.url(newfile);
  console.log("SENDIMAGE " + gimg);

  var msg = "<ul> <li>sending image file </li> </ul>";

  var simg = "http://projects.reviewjournal.com/data/test/Bob-2013-08-29T14:08:27-07:00/rjphoto.png";
  var filename = "http://projects.reviewjournal.com/data/test/Lee-2013-08-29T13:31:16-07:00/rjphoto.png";
  //var filename = "mobile.png";
  var mimg = "Bob-2013-08-29T14:08:27-07:00-rjphoto";
  var newname = "testpng";

  cloudinary.uploader.upload(filename, function(result) { 
    console.log(result)}, 
  { public_id: newname }); 
  cloudinaary.image("logo_lpg70n.jpg", { width: 100, height: 150, crop: "fill" })

  response.send(msg);
});
//-------------------------------------------------------------------------------------------
  var mostCurrentImage = " ";  

  cloudinary.api.resources(function(result) {
           var pars =JSON.stringify(result); 
           var jObj = JSON.parse(pars);    
           var idx = 0;
           jObj.resources.forEach(function(item) {    
              if (idx === 0) { 
                 mostCurrentImage = '<b><br>' + 'Most current image' + '</b><br>' + '<a href=' + '"' + item.url +'"' + '>' + item.url + '</a>';  
              };          
              idx++;  
           });
           }, 
           { resource_type: 'image' 
           }
  );
//-------------------------------------------------------------------------------------------
  var files = " ";  
  cloudinary.api.resources(function(result) {
             
           var pars =JSON.stringify(result); 
           var jObj = JSON.parse(pars);    
           jObj.resources.forEach(function(item) {    
               files = files + '<br>' + item.url;  
           });
           }, 
           { resource_type: 'raw' 
           }
  );
//-------------------------------------------------------------------------------------------
  var imgs = " ";  
  cloudinary.api.resources(function(result) {
             
           var pars =JSON.stringify(result); 
           var jObj = JSON.parse(pars);    
           jObj.resources.forEach(function(item) {    
               imgs = imgs + '<br><a href=' + '"' + item.url +'"' + '>' + item.url + '</a>';  
           });
           }, 
           { resource_type: 'image' 
           }
  );
//-------------------------------------------------------------------------------------------
app.post('/insertmytable', function(request, response)  {
//app.get('/insertlastimage', function(request, response)  {

      var jss = JSON.stringify(request.body);
      var jparse = JSON.parse(jss);

      var jnm = jparse.name;
      var jem = jparse.email;
      var jdesc = jparse.description;

      //var jnm = "jack";
      //var jem = "jack@email.com";
      //var jdesc = "pebble beach";

      cloudinary.api.resources(function(result) {
           var currentImage = " "; 
           var jimage = " "; 
           var pars =JSON.stringify(result); 
           var jObj = JSON.parse(pars);    
           var idx = 0;

           jObj.resources.forEach(function(item) {    
              if (idx === 0) { 
                var currentImage = "{" + "\"" + "imageurl" + "\"" +  ":"  + "\"" + item.url + "\"" + "}";    
                var jimageurl = item.url;

                var conString = "postgres://wmapqujuisnnra:IWUsYseUZy5cjLIQoUliu18AJr@ec2-54-221-240-24.compute-1.amazonaws.com:5432/d3ssb1qo6p2d8j";
                var client = new pg.Client(conString);

                var sq = 'insert into mytable (name,email,description,imageurl) values (' + '\'' + jnm + '\'' + ',' + '\'' + jem + '\'' + ',' +  '\'' + jdesc + '\'' + ',' + '\'' +  jimageurl +'\'' +  ')';

                client.connect(function(err) {
                    client.query(sq, function(err, result) {
                       if(err) {
                          response.send("somethings wrong check logs" + err);
                       }
                       //response.send("done " + sq);
                       response.send(null);
                    });
                    //response.send("done " + sq);
                });
              };          
              idx++;  
           });
           }, 
           { resource_type: 'image' 
           }
     );
});
//-------------------------------------------------------------------------------------------
app.get('/getlastimage/:id', function(request, response)  {
      cloudinary.api.resources(function(result) {

           var currentImage = " "; 
           var jimage = " "; 
           var pars =JSON.stringify(result); 
           var jObj = JSON.parse(pars);    
           var idx = 0;
           jObj.resources.forEach(function(item) {    
              if (idx === 0) { 
                //currentImage = '<b><br>' + '</b><br>' + '<a href=' + '"' + item.url +'"' + '>' + item.url + '</a>';  
                var currentImage = "{" + "\"" + "imageurl" + "\"" +  ":"  + "\"" + item.url + "\"" + "}";    
                //jimage = JSON.stringify(currentImage);
                response.send(currentImage);
              };          
              idx++;  
           });
           }, 
           { resource_type: 'image' 
           }
     );
});
//-------------------------------------------------------------------------------------------
//app.get('/getimages/:id', function(request, response)  {
app.get('/getimages', function(request, response)  {
  //var p = request.params.id;
  //console.log("PARAM " + p);
  var img = "<b>Listing of image Cloudinary files</b>";

      var currentImage = "none available"; 
      cloudinary.api.resources(function(result) {
           var currentImage = " "; 
           var pars =JSON.stringify(result); 
           var jObj = JSON.parse(pars);    
           var idx = 0;
           jObj.resources.forEach(function(item) {    

              //if (idx === 0) { 
              //  currentImage = '<b><br>' + 'Most current image' + '</b><br>' + '<a href=' + '"' + item.url +'"' + '>' + item.url + '</a>';  
              //  response.send(img + '<br>'+ currentImage);
              //};          

              currentImage = currentImage +  '</b><br>' + '<a href=' + '"' + item.url +'"' + '>' + item.url + '</a>';  
              idx++;  
           });
           response.send(img + '<br>'+ currentImage);
           }, 
           { resource_type: 'image' 
           }
     );
});
//-------------------------------------------------------------------------------------------
app.get('/getfiles/:id', function(request, response)  {
  var p = request.params.id;
  console.log("PARAM " + p);
  var fil = "<b>Listing of raw Cloudinary files</b>";

      var currentFile = "none available"; 
      cloudinary.api.resources(function(result) {
           var currentFile = " "; 
           var pars =JSON.stringify(result); 
           var jObj = JSON.parse(pars);    
           var idx = 0;
           jObj.resources.forEach(function(item) {    

              //if (idx === 0) { 
              //  currentImage = '<b><br>' + 'Most current image' + '</b><br>' + '<a href=' + '"' + item.url +'"' + '>' + item.url + '</a>';  
              //  response.send(img + '<br>'+ currentImage);
              //};          

              currentFile = currentFile +  '</b><br>' + '<a href=' + '"' + item.url +'"' + '>' + item.url + '</a>';  
              idx++;  
           });
           response.send(fil + '<br>'+ currentFile);
           }, 
           { resource_type: 'raw' 
           }
     );
});
//-------------------------------------------------------------------------------------------
app.get('/getfilesold/:id', function(request, response)  {
  var p = request.params.id;

  console.log("PARAM " + p);
  //var lst = " ";  
  var fi = "<b>Listing of raw Cloudinary files</b><br> ";
  var img = "<b>Listing of image Cloudinary files</b><br> ";

  //var rs = cloudinary.api.resources(function(result){}, { resource_type: 'raw' });
  //var rs; 

  //console.log("JSON RESULTS " + JSON.stringify(rs));

  //cloudinary.api.resources(function(result) {console.log("LIST OF FILES " + JSON.stringify(result)) },{ resource_type: 'raw' }
  //);

  //cloudinary.api.resources(function(result) {
  //         //console.log("LIST OF FILES1 " + JSON.stringify(result)); 
  //         //console.log("LIST OF FILES2 " + JSON.stringify(result)) 
  //         var pars =JSON.stringify(result); 
  //         var jObj = JSON.parse(pars);    
  //         //console.log('LIST OF FILES3 ' + jObj);
  //         //console.log('LIST OF FILES4 ' + jObj.resources[0].url);
  //         console.log('LIST OF RAW FILES');
  //         jObj.resources.forEach(function(item) {    
  //             console.log(item.url);
  //             lst = lst + '<br>' + item.url;  
  //         });
  //         }, 
  //         { resource_type: 'raw' 
  //         }
  //);

  //console.log("JSON RESULTS " + JSON.stringify(result));
  //cloudinary.api.resources(function(result)  { console.log(JSON.stringify(result)) });
  //function(result) { console.log(result.toSource()) },
  //{ public_id: "package.json",
  //  resource_type: "raw" });
  // console.log("NUMBER OF FILES  " + result);

  response.send(fi + files + '<br><br>' + img + imgs + '<br><br> '+ mostCurrentImage  );
});
//-------------------------------------------------------------------------------------------
var port = process.env.PORT || 5000;
app.listen(port, function() {
  console.log("Listening on " + port);
});
//-------------------------------------------------------------------------------------------
// curl operations to list and delete cloudinary files/images
//-------------------------------------------------------------------------------------------
//curl 'https://API_KEY:API_SECRET@api.cloudinary.com/v1_1/CLOUD_NAME/resources/image?exif=1'
//curl 'https://876552226582264:vAIdVdyFhfT_4Zb1iAZORNyQxLs@api.cloudinary.com/v1_1/lcbklf5b3/resources/image?exif=1'
//curl 'https://876552226582264:vAIdVdyFhfT_4Zb1iAZORNyQxLs@api.cloudinary.com/v1_1/lcbklf5b3/resources/raw?exif=1'
//curl -X DELETE 'https://876552226582264:vAIdVdyFhfT_4Zb1iAZORNyQxLs@api.cloudinary.com/v1_1/lcbklf5b3/resources/raw/upload?public_ids=y.txt'
//curl 'https://876552226582264:vAIdVdyFhfT_4Zb1iAZORNyQxLs@api.cloudinary.com/v1_1/lcbklf5b3/resources/raw/upload/v1382640521/y.txt'

//cloudinary.api.delete_resources_by_prefix('sunday',
//    function(result){});

//cloudinary.config({ 
//  cloud_name: 'lcbklf5b3', 
//  api_key: '876552226582264',
//  api_secret: 'vAIdVdyFhfT_4Zb1iAZORNyQxLs'
//-------------------------------------------------------------------------------------------
app.get('/getimagejson/:id', function(request, response)  {
  var p = request.params.id;
  console.log("PARAM " + p);
  var msg = "<ul> <li>getting image </li> </ul>";

  var lastmsg="You entered: " + p;
  msg = msg + "<br>" + lastmsg;
  var dimg = cloudinary.image("logo_lpg70n.png")
  msg = msg + "<br><br>" + dimg;

  var img = 'http://res.cloudinary.com/lcbklf5b3/image/upload/logo_lpg70n.png';
  var fileName = 'testpng.txt';

  fs.exists(fileName, function(exists) {
    if (exists) {
      fs.stat(fileName, function(error, stats) {
        fs.open(fileName, "r", function(error, fd) {
          var buffer = new Buffer(stats.size);
 
          fs.read(fd, buffer, 0, buffer.length, null, function(error, bytesRead, buffer) {
            data = buffer.toString("utf8", 0, buffer.length);
            console.log('READING DATA ' + data);
            fs.close(fd);
          });
        });
      });
    //response.send(data);
    }
  response.send(msg);
});
});

//-------------------------------------------------------------------------------------------
function getDateTime() {
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
}
//-------------------------------------------------------------------------------------------
app.get('/getnowsql/:id', function(request, response)  {
  var p = request.params.id;

var conString = "postgres://wmapqujuisnnra:IWUsYseUZy5cjLIQoUliu18AJr@ec2-54-221-240-24.compute-1.amazonaws.com:5432/d3ssb1qo6p2d8j";

var client = new pg.Client(conString);
client.connect(function(err) {
  //if(err) {
  //  return console.error('could not connect to postgres', err);
  //}

  client.query('SELECT NOW() AS "theTime"', function(err, result) {
    if(err) {
      response.send(err);
      //return console.error('error running query', err);
    }
    response.send("Returning timestamp " + result.rows[0].theTime);
    //client.end();
  });
         //response.send("ok");
});
         //response.send(conString);
});
//-------------------------------------------------------------------------------------------
app.get('/getnodesql/:id', function(request, response)  {
  var p = request.params.id;
  var str = "";

  var conString = "postgres://wmapqujuisnnra:IWUsYseUZy5cjLIQoUliu18AJr@ec2-54-221-240-24.compute-1.amazonaws.com:5432/d3ssb1qo6p2d8j";

  var client = new pg.Client(conString);
  client.connect(function(err) {
    client.query('SELECT  * FROM mytable', function(err, result) {
      if(err) {
        response.send(err);
      }
      var rval = JSON.stringify(result.rows);
      var jObj = JSON.parse(rval);    
      jObj.forEach(function(item) {    
           str = str + '<br>' + item.name + ";  " + item.email + ";  " + item.description + "; " + item.imageurl;  
     })
      response.send("Returning values " + str);
    });
  });
});
//-------------------------------------------------------------------------------------------
app.post('/insertmytablex', function(req, res)  {
//app.post('/insertmytable', function(req, res)  {

  var jss = JSON.stringify(req.body);
  var jparse = JSON.parse(jss);
  var jnm = jparse.name;
  var jem = jparse.email;
  var jdesc = jparse.description;
  var conString = "postgres://wmapqujuisnnra:IWUsYseUZy5cjLIQoUliu18AJr@ec2-54-221-240-24.compute-1.amazonaws.com:5432/d3ssb1qo6p2d8j";
  var client = new pg.Client(conString);

  client.connect(function(err) {
    var sq = 'insert into mytable (name,email,description) values (' + '\'' + jnm + '\'' + ',' + '\'' + jem + '\'' + ',' +  '\'' + jdesc + '\'' + ')';
    client.query(sq, function(err, result) {
      if(err) {
        res.send(err);
      }
      res.send(null);
      //client.end();
    });
  });
});
//-------------------------------------------------------------------------------------------
app.get('/insertnodesql/:id', function(request, response)  {
  var p = request.params.id;
  //var chg = {"name":"howard","email":"kwoodall@reviewjournal.com","description":"new email setup"};
  var chg = JSON.parse(p);    

  var conString = "postgres://wmapqujuisnnra:IWUsYseUZy5cjLIQoUliu18AJr@ec2-54-221-240-24.compute-1.amazonaws.com:5432/d3ssb1qo6p2d8j";

  var client = new pg.Client(conString);
  client.connect(function(err) {
    var idx = 20;
    var sq = 'insert into mytable (name,email,description) values (' + '\'' + chg.name + '\'' + ',' + '\'' + chg.email + '\'' + ',' +  '\'' + chg.description + '\'' + ')';

    client.query(sq, function(err, result) {
      if(err) {
        response.send(err);
      }
      response.send("Insert done "  + sq);
      //client.end();
    });
    //response.send("Insert done "  + " " + p.email );
  });
});
//-------------------------------------------------------------------------------------------
app.get('/deletenodesql/:id', function(request, response)  {
  var p = request.params.id;
  //p = {'name':'howard'};
  var chg = JSON.parse(p);    

  var conString = "postgres://wmapqujuisnnra:IWUsYseUZy5cjLIQoUliu18AJr@ec2-54-221-240-24.compute-1.amazonaws.com:5432/d3ssb1qo6p2d8j";

  var client = new pg.Client(conString);
  client.connect(function(err) {

    var sq = 'delete from mytable where name = ' + '\'' + chg.name + '\'';
    client.query(sq, function(err, result) {
    //client.query('delete from mytable where name = \'hey\' ', function(err, result) {
      if(err) {
        response.send(err);
      }
      response.send("delete done");
      //client.end();
    });
  });
});
//-------------------------------------------------------------------------------------------
app.get('/updatenodesql/:id', function(request, response)  {
  var p = request.params.id;
  //p = {'namefrom':'howard','nameto':'hughes'};
  var chg = JSON.parse(p);    
  var sq = 'update mytable set name = ' + '\'' + chg.nameto + '\'' + ' where name = ' + '\'' +  chg.namefrom + '\'';

  var conString = "postgres://wmapqujuisnnra:IWUsYseUZy5cjLIQoUliu18AJr@ec2-54-221-240-24.compute-1.amazonaws.com:5432/d3ssb1qo6p2d8j";

  var client = new pg.Client(conString);
  client.connect(function(err) {
    client.query(sq, function(err, result) {
      if(err) {
        response.send(err);
      }
      response.send("update done " + sq);
      //client.end();
    });
  });
});
//-------------------------------------------------------------------------------------------


