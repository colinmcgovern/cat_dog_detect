var app = require('express')();
var express = require('express'); 
var http = require('http').Server(app);
var io = require('socket.io')(http);
var port = process.env.PORT || 8080;

app.use("/", express.static(__dirname + '/'));

app.get('/', function(req, res){
  res.sendFile(__dirname + '/');
});

http.listen(port, function(){
	console.log('this is for testing locally');
  console.log('listening on *:' + port);
});
