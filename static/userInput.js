var socket = io();
socket.on('message', function(data) {
  console.log(data);
});


var isPlayer = true;
const gradient = "linear-gradient(to right, #f12711, #f5af19)"


var button = document.getElementById("button");
var header = document.getElementById("head");

console.log(header);

// // 2. Append somewhere
var body = document.getElementsByTagName("body")[0];


var message = document.getElementById("message");
console.log(message);
message.innerHTML = "Please Submit a Homework Assignment. type :a to create a new alarm";

body.style.background = gradient;
var socket = io.connect();
var assignmentForm = document.getElementById("assignmentF");
var dateForm = document.getElementById("dateF");
var hourForm = document.getElementById("hourF");
var passwordForm = document.getElementById("passwordF");

// 3. Add event handler
button.addEventListener ("click", function() {
  var assign = assignmentForm.value; 
  var date = dateForm.value;
  var hour = hourForm.value;
  if (assign.startsWith(':a')){
    socket.emit('new alarm', [assign.replace(':a',''), date.replace(':a',''), hour, passwordForm.value.hashCode()]);
  }
  else{
    socket.emit('new assignment', [assignmentForm.value, dateForm.value, hourForm.value, passwordForm.value.hashCode()]);
  }
});




socket.on('good', function(){
  message.innerHTML = "assignment recorded"
  
});
socket.on('good alarm', function(){
  message.innerHTML = "alarm recorded"
  
});
socket.on('error', function(){
  message.innerHTML = "uh oh, something went wrong. Maybe you used the wrong password?"
});





