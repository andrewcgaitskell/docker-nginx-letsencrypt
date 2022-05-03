
# install docker

    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh

# investigate rootless

    https://docs.docker.com/engine/security/rootless/
 
# test docker

    docker run -dp 80:80 docker/getting-started

# install docker compose

    curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose
    docker-compose --version

# create nginx Dockerfile
    
    FROM ubuntu:21.10
    RUN apt-get update -y 
    RUN apt-get install nginx -y
    RUN apt-get install curl -y
    EXPOSE 80
    ##EXPOSE 80 443
    CMD ["nginx", "-g", "daemon off;"]

# Clear all containers and images

## To delete all containers including its volumes use,

    sudo docker rm -vf $(sudo docker ps -aq)

## To delete all the images,

    sudo docker rmi -f $(sudo docker images -aq)


# Make image from local file

    docker build -t my-nginx-im-1 .
    
# Run Image

    sudo docker run --name my-nginx-ct-1 -d -p 80:80 my-nginx-im-1

# List Running Containers

    docker ps -a | grep my-nginx-ct-1

# Check Logs

    docker logs [OPTIONS] CONTAINER

    docker logs my-nginx-ct-1

# EXTRAS

    sudo docker build -t container-nginx-1 .

    sudo docker run --name running-container-nginx-1 -d -p 8080:80 container-nginx-1

    sudo docker run --name running-container-nginx-1 -d -p 443:443 container-nginx-1

# standard block server

    /etc/nginx/conf.d directory named domain‑name.conf (so in our example, www.example.com.conf).

    server {
  root     /var/www/example.com;
  location ^~ /.well-known/acme-challenge/ {
    default_type "text/plain";
  alias /var/www/acme-challenge/;
}



    server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    server_name www.example.com;
    }

# standard block server - test.dmtools.info.conf

    server {
    location /.well-known/acme-challenge/ {
        alias /var/www/html/.well-known/acme-challenge/;
    }
    }


    server {
    listen 80;
    listen [::]:80;
    root /var/www/html/test.dmtools.info;
    server_name test.dmtools.info;
    }

# create nginx Dockerfile - no cert
    
    FROM ubuntu:21.10
    RUN apt-get update -y 
    RUN apt-get install nginx -y
    RUN apt-get install curl -y
    RUN apt-get update -y
    RUN apt-get install software-properties-common -y
    RUN apt-get update -y
    RUN apt-get install python3 -y
    RUN apt-get install certbot -y
    RUN apt-get install python3-certbot-nginx -y
    COPY  ./test.dmtools.info.conf /etc/nginx/conf.d
  
    EXPOSE 80
    CMD ["nginx", "-g", "daemon off;"]
    
