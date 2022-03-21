# docker-nginx-letsencrypt

## starting point

https://hub.docker.com/_/nginx

## Create Container

sudo docker build -t container-nginx-1 .

## Run Container

sudo docker run --name running-container-nginx-1 -d -p 8080:80 container-nginx-1


