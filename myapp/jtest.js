//--------------------------------------------------------------------------------
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
//--------------------------------------------------------------------------------
var x = "test";
var y = "{" + "\"" + "name" + "\"" +  ":"  + "\"" + x + "\"" + "}";
//--------------------------------------------------------------------------------
var ctr = 0;

var blockingIO = function(callbackWhenFinished) {

	setTimeout(function() {
		callbackWhenFinished(" the blocking task has been completed ");
	}, 5000 );
}
//--------------------------------------------------------------------------------
var doThisWhenFinished = function(something) {
        console.log("prints from doThisWhenFinished " + something);
        debugger; 
}
//--------------------------------------------------------------------------------
blockingIO(doThisWhenFinished);
//--------------------------------------------------------------------------------
var doit = function() {
        console.log("prints from doit " );
        ctr = 100;
        debugger; 
}
//--------------------------------------------------------------------------------
doit();
//--------------------------------------------------------------------------------
console.log("json is " + y);
debugger; 
//--------------------------------------------------------------------------------
//app.get('/', function(request, response)  {
//      response.send("nbr of rows loaded ");
//});
//function doThisWhenFinished(something) {
//--------------------------------------------------------------------------------
//function blockingIO(callbackWhenFinished) {
//--------------------------------------------------------------------------------



