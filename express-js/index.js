var express = require('express');
var app = express();

app.get('/', function(req, res){
   res.send(`
   <h1> Express-js Calculator </h1>
    <hr>
    For addition, use addition/x/y <br>
    For subtraction, use subtraction/x/y <br>
    For multiplication, use multiplication/x/y <br>
    For division, use division/x/y <br>

    where x and y are the integer parameters.
   `);
});

app.get('/hello', function(req, res){
   res.send(req.headers.host);
});

app.get('/addition/:x/:y', function(req, res){
   ans = (parseInt(req.params.x) + parseInt(req.params.y))
   res.send(req.params.x + ' + ' + req.params.y + ' = ' + ans.toString());
 });

 app.get('/subtraction/:x/:y', function(req, res){
   ans = (parseInt(req.params.x) - parseInt(req.params.y))
   res.send(req.params.x + ' - ' + req.params.y + ' = ' + ans.toString());
 });

 app.get('/multiplication/:x/:y', function(req, res){
   ans = (parseInt(req.params.x) * parseInt(req.params.y))
   res.send(req.params.x + ' * ' + req.params.y + ' = ' + ans.toString());
 });

 app.get('/division/:x/:y', function(req, res){
   ans = (parseInt(req.params.x) / parseInt(req.params.y))
   res.send(req.params.x + ' / ' + req.params.y + ' = ' + ans.toString());
 });

app.listen(3000);
