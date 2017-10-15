const express = require('express'),
      mongoose = require('mongoose');
       


var app = express();
var bodyParser = require('body-parser');

//app.use(bodyParser());
/**bodyParser.json(options)
 * Parses the text as JSON and exposes the resulting object on req.body.
 */
app.use(bodyParser.json());

app.post("/testPost", function (req, res) {
    console.log(req.body)
	
});

app.get('/testResponse', function (req, res) {
   res.send('Hello World');
})

app.post('/testGetJson', (req, res) => {
   console.log(req.headers);
   res.send(JSON.stringify(req));

})

var server = app.listen(8081, function () {
   var host = server.address().address
   var port = server.address().port
   
   console.log("ComBoard listening at http://%s:%s", host, port)
})
