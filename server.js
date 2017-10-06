const express = require('express'),
      mongoose = require('mongoose');
       


var app = express();


app.get('/testResponse', function (req, res) {
   res.send('Hello World');
})

app.post('/testGetJson', (req, res) => {
   console.log(req.headers);
   res.send(JSON.stringify(req.headers));

})

var server = app.listen(8081, function () {
   var host = server.address().address
   var port = server.address().port
   
   console.log("ComBoard listening at http://%s:%s", host, port)
})
