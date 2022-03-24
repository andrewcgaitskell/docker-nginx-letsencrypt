ubuntu 21.10
make sure port forwarding is enabled

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

# remove default conf files

    rm /etc/nginx/sites-enabled/default
    rm /etc/nginx/sites-available/default

# add default to conf.d folder

    nano /etc/nginx/conf.d/default.conf
    
    #
    # The default server
    #
    server {
        listen       80;
        server_name  _;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
            root   /usr/share/nginx/html;
            index  index.php index.html index.htm;
        }

        error_page  404              /404.html;
        location = /404.html {
            root   /usr/share/nginx/html;
        }

        # redirect server error pages to the static page /50x.html
        #
        }
    

# stop nginx

    sudo systemctl stop nginx

# install docker

    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh
    
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
    
    #RUN certbot run -n --nginx --agree-tos -d www.example.com  -m  mygmailid@gmail.com  --redirect
    EXPOSE 80
    CMD ["nginx", "-g", "daemon off;"]
    
# create nginx Dockerfile - get cert
    
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
    
    RUN certbot run -n --nginx --agree-tos -d test.dmtools.info  -m  andrew@gaitskell.com  --redirect
    EXPOSE 80 443
    CMD ["nginx", "-g", "daemon off;"]
    
    
# web root

Creating certificates

docker run -it --rm \ 
--volumes-from nginx \ 
certbot/certbot certonly \ 
--webroot \ 
--webroot-path /var/www/html \ 
--agree-tos \ 
--staging \ 
--dry-run \ 
-m your@email.com \ 
-d staging.vea.re

I will go throug


# create nginx Dockerfile - get cert
    
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
    
    RUN certbot run -n --nginx --webroot --webroot-path /var/www/html --agree-tos --staging --dry-run -d test.dmtools.info  -m  andrew@gaitskell.com  --redirect
    EXPOSE 80 443
    CMD ["nginx", "-g", "daemon off;"]
    
# create nginx Dockerfile - get cert
    
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
    COPY  ./index.html /var/www/html/test.dmtools.info
    
    RUN certbot certonly --webroot -w /var/www/html --agree-tos --staging --dry-run -d test.dmtools.info  -m  andrew@gaitskell.com  --redirect
    EXPOSE 80 443
    CMD ["nginx", "-g", "daemon off;"]
    
# tried ready made

https://github.com/andrewcgaitskell/nginx-certbot

did not work - too many redirects

# now looking at node and how to connect containers

    sudo su
    apt update
    apt install nodejs npm
    
    
