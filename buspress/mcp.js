var jsoncsv, data, fs, arrayOfJSON;
var mysql    = require('mysql');
var json2csv    = require('json2csv');
var express = require('express');
var fs = require('node-fs');

var pconnection = mysql.createConnection({
  host     : 'writer.mysql.stephensmedia.com',
  user     : 'django_project',
  password : 'lD*3.$~F2PM[', 
  database : 'django_bizproject',
  insecureAuth: true
});

var connection = mysql.createConnection({
  host     : 'mysql01.stephensmedia.com',
  user     : 'django',
  password : 'n0|d', 
  database : 'django_bizproject',
  insecureAuth: true
});

var arr = ["accountingfirm",
           "advertisingagency",
           "alternativeenergy",
           "angelfundinvestor",
           "architecturefirm"];

for (var i=0,len=arr.length; i<len; i++) {

    exec mcp01.js;

};



















