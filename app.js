// Dependencies
var express = require('express');
var http = require('http');
var path = require('path');
var socketIO = require('socket.io');

var app = express();
var server = http.Server(app);
var io = socketIO(server);

var assignments = [];

var currentPassword = -741086112;

app.set('port', 5000);
app.use('/static', express.static(__dirname + '/static'));

// Routing
app.get('/', function(request, response) {
  response.sendFile(path.join(__dirname, 'index.html'));
});

app.get('/api', function(request,response){
  response.send(assignments)
})
const port=process.env.PORT || 3000
server.listen(port,() => {
console.log(`Server running at port `+port);
});

io.on('connection', function(socket) {
});

var buzzerStates = {};

io.on('connection', function(socket) {
  socket.on('new assignment', function(assignment){
    console.log(assignment)
    console.log(assignment[3])
    if (assignment[3] == currentPassword){
      console.log("succsessful password attempt");
      var entry = {
        "assignment":assignment[0],
        "duedate":assignment[1],
        "hour":assignment[2]
      }
      assignments.push(entry);
      console.log(assignments)
      io.sockets.emit("good");
    }
    else{
      io.sockets.emit("error");
    }
  });

});
