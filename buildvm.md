ubuntu 21.10

# nginx

    sudo su
    apt update
    apt upgrade -y
    apt install curl -y
    apt install nginx -y
  

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
    EXPOSE 80

# Clear all containers and images

## To delete all containers including its volumes use,

    sudo docker rm -vf $(sudo docker ps -aq)

## To delete all the images,

    sudo docker rmi -f $(sudo docker images -aq)


# Make image from local file

    docker build -t my-nginx-im-1 .
    
# Run Image

    docker run -dp 80:80 my-nginx-im-1 --name my-nginx-ct-1

# List Running Containers

    docker ps -a | grep my-nginx-ct-1

# Check Logs

    docker logs [OPTIONS] CONTAINER

    docker logs my-nginx-ct-1

# EXTRAS

    sudo docker build -t container-nginx-1 .

    sudo docker run --name running-container-nginx-1 -d -p 8080:80 container-nginx-1

    sudo docker run --name running-container-nginx-1 -d -p 443:443 container-nginx-1
