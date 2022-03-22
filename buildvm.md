ubuntu 21.10

# nginx

    sudo su
    apt uodate
    apt upgrade -y
    apt install nginx -y
    FROM ubuntu:21.10
RUN apt-get update -y 
RUN apt-get install nginx -y
RUN apt-get install curl -y 

# check nginx commands

    sudo nginx -t
    sudo nginx -s reload

    sudo systemctl stop nginx
    sudo systemctl start nginx
    sudo systemctl status nginx

# stop nginx

    sudo systemctl stop nginx

# install docker

    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh
    
# test docker

    docker run -dp 80:80 docker/getting-started
    
# create nginx Dockerfile
    
    FROM ubuntu:21.10
    RUN apt-get update -y 
    RUN apt-get install nginx -y
    RUN apt-get install curl -y 

        
