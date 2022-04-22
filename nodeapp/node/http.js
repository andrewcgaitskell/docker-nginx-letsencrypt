var http = require('http');

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

http.createServer(function(req,res){
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.write(req.url);
      res.end();		
      }).listen(PORT, HOST);
console.log('Server started on 0.0.0.0:8080; press Ctrl-C to terminate...!');
