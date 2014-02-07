
var Router = require('node-simple-router')
// Alternative: assumes router.js is located at the current working directory.
//var Router = require('./router')

var http   = require('http')

var router = Router();

router.get('/', function (request, response) {
  response.end('Home page');})

router.get('/hello/:who', function(request, response) {
  response.end("Hello, " + request.params.who);})

server = http.createServer(router)

server.listen(3000)













