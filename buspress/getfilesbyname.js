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

var param = process.argv[2];
console.log("PARAMETER IS : " + param);

var cat = param;
var t1 = "bizforms_";
var tbl = "bizforms_" + cat;

var sql = 'select ' + "\"" + cat + "\"" + ',company_name,address,zip,phone,exec_first_name,exec_last_name, exec_title, author_first_name, author_last_name,author_phone,author_email from ' + tbl;

pconnection.connect();

pconnection.query(sql, function(err, rows, fields) {
  if (err) throw err;
  arrayOfJSON = JSON.stringify(rows);

  json2csv({data: rows, fields: [cat, 
                                'company_name',
                                'address', 
                                'zip', 
                                'phone', 
                                'exec_first_name', 
                                'exec_last_name', 
                                'exec_title', 
                                'author_first_name', 
                                'author_last_name', 
                                'author_phone', 
                                'author_email']}, 
                                 function(err, csv) {
    if (err) console.log(err);
       //console.log(csv);
       fs.writeFile('temp.csv', csv, function(err) {
          if (err) throw err;
          console.log('file saved');
       });
  });
});

pconnection.end();

















