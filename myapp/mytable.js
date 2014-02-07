var express = require("express");
var cloudinary = require("cloudinary");
var getdatabase = require("./getDatabase.js");
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
//-------------------------------------------------------------------------------------------
var Scooper = backbone.Model.extend({
    defaults: {
      name: "not used" 
    }
});
var ScooperCollection = backbone.Collection.extend({
     model: Scooper
});
var scoopers = new ScooperCollection();
//-------------------------------------------------------------------------------------------
// access database
//-------------------------------------------------------------------------------------------
var arr =[];
var idx = 0;  //global variable
var fin = 0;  //global variable
pg.connect(process.env.DATABASE_URL, function(err, client) {
    var query = client.query('select * from mytable');
    query.on('row', function(row) { 
        arr[idx] = row.name;
        idx++;

        var jObj = row;
        var scooper = new Scooper();
        scooper.set('name', jObj.name);
        scoopers.add([scooper]); 
    });
});
//--------------------------------------------------------------------------------
exports.variable = function (r) {
       return arr;
};
//--------------------------------------------------------------------------------
//console.log("FROM MYTABLE.JS " + arr[idx]);
//blockingIO(doThisWhenFinished);
//console.log(scooper.get('name'));
//function blockingIO(callbackWhenFinished) {
//
//          pg.connect(process.env.DATABASE_URL, function(err, client) {
//            var query = client.query('SELECT * FROM mytable');
//            query.on('row', function(row) { 
//               arr[idx] = row.name;
//
//               console.log("QUERY ROW NAME IS " + arr[idx]);
//               idx++;
//	       callbackWhenFinished(idx);
//             });
//          });
//}
//--------------------------------------------------------------------------------
//function doThisWhenFinished(idx) {
//        fin = fin + idx; 
//        console.log("this prints first " + idx);
//        console.log("this prints second " + fin);
//        return fin;
//}
//--------------------------------------------------------------------------------

