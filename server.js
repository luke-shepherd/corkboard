var express = require('express'),
   mongoose = require('mongoose');

var MongoClient = require('mongodb').MongoClient;
var assert = require('assert');

var app = express();
var bodyParser = require('body-parser');

var url = 'mongodb://localhost:27017/test123';
MongoClient.connect(url, function(err, db) {
   assert.equal(null, err);
   console.log("Connected correctly to database.");
   db.close();
});

app.use(bodyParser.json());

app.post("/testPost", function (req, res) {
   console.log(req.body);
   res.send(req.body);

});

app.get('/testResponse', function (req, res) {
   res.send('Hello World');
});

app.get('/getAllBoards', (req, res) => {
   console.log(req.headers);
   res.send({'coordinates': {
      'longitude': req.headers.longitude,
      'latitude': req.headers.latitude,
   }});
});

var server = app.listen(8081, function () {
   var host = server.address().address;
   var port = server.address().port;

   console.log("ComBoard listening at http://%s:%s", host, port);
});
