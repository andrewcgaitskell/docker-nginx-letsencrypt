//include http module 
var http = require('http');

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

http.createServer(function(req,res){
	//store URL in variable q_string

	var q_string = req.url;
	switch(q_string) {
		case '/':
                        	res.writeHead(200, { 'Content-Type': 'text/plain' });
                        	res.write('Welcome To Tecmint.com!')
                        	res.end();
                        	break;
                	case '/about':
                		res.writeHead(200, { 'Content-Type': 'text/plain' });
                        	res.write('About Us');
                        	res.write('\n\n');
                        	res.write('Tecmint.com - Best Linux HowTos on the Web.');
                        	res.write('\n');
                        	res.end('Find out more: https://www.tecmint.com/who-we-are/');
                        	break;
                	case '/tecmint/authors':
                        	res.writeHead(200, { 'Content-Type': 'text/plain' });
                        	res.write('Tecmint Authors');
                        	res.write('\n\n');
                        	res.end('Find all our authors here: https://www.tecmint.com/who-we-are/');
                        	break;
                	default:
                       		res.writeHead(404, { 'Content-Type': 'text/plain' });
                       		res.end('Not Found');
                        	break;
	}
}).listen(PORT, HOST);
console.log('Server started on 0.0.0.0:8080; press Ctrl-C to terminate....');
