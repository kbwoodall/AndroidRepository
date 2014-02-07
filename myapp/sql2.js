var pg = require('pg');

//var conString = "postgres://postgres:1234@localhost/postgres";
var conString = "postgres://wmapqujuisnnra:IWUsYseUZy5cjLIQoUliu18AJr@ec2-54-221-240-24.compute-1.amazonaws.com:5432/d3ssb1qo6p2d8j";

var client = new pg.Client(conString);
client.connect(function(err) {
  if(err) {
    return console.error('could not connect to postgres', err);
  }
  client.query('SELECT NOW() AS "theTime"', function(err, result) {
    if(err) {
      return console.error('error running query', err);
    }
    console.log(result.rows[0].theTime);
    //output: Tue Jan 15 2013 19:12:47 GMT-600 (CST)
    client.end();
  });
});



