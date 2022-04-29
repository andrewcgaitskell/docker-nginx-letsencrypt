'use strict';

const express = require('express');

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// App
const app = express();
app.get('/', (req, res) => {
  res.send('Hello World from within Docker');
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);

//var http = require('http');
//http.createServer(function(req,res){
//        res.writeHead(200, { 'Content-Type': 'text/plain' });
//        res.end('Hello World!');
//}).listen(8080);

