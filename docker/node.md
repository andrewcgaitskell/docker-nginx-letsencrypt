https://www.digitalocean.com/community/tutorials/how-to-build-a-node-js-application-with-docker

sudo apt install nodejs npm

https://github.com/nodejs/docker-node/blob/main/docs/BestPractices.md#docker-run

# server.js

    use strict';

    const express = require('express');

    // Constants
    const PORT = 8080;
    const HOST = '0.0.0.0';

    // App
    const app = express();
    app.get('/', (req, res) => {
      res.send('Hello World from Docker');
    });

    app.listen(PORT, HOST);
    console.log(`Running on http://${HOST}:${PORT}`);

    //var http = require('http');
    //http.createServer(function(req,res){
    //        res.writeHead(200, { 'Content-Type': 'text/plain' });
    //        res.end('Hello World!');


# Dockerfile - nodeapp1

    FROM node:16

    # Create app directory
    WORKDIR /usr/src/app

    # Install app dependencies
    # A wildcard is used to ensure both package.json AND package-lock.json are copied
    # where available (npm@5+)
    COPY package.json ./

    RUN npm install
    # If you are building your code for production
    # RUN npm ci --only=production

    # Bundle app source
    COPY . .

    # Expose the port we want to use
    EXPOSE 8080



docker rmi -f $(sudo docker images -aq)

sudo docker rm -vf $(sudo docker ps -aq)


docker build -t my-nodeapp-im-1 .

docker run --name nodejs-image-demo-c1 -p 80:8080 -d my-nodeapp-im-1

# nginx dockerfile

    FROM nginx
    COPY default.conf /etc/nginx/conf.d/default.conf

# default.conf

    server {
        location / {
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;

            proxy_pass http://nodeserver:5000;
        }
    }


# docker-compose.yml

    version: "3.8"
    services:
        nodeserver:
            build:
                context: ./nodeapp1
            ports:
                - "5000:5000"
        nginx:
            restart: always
            build:
                context: ./nginx1
            ports:
                - "80:80"  

