For Linux

To delete all containers including its volumes use,

sudo docker rm -vf $(sudo docker ps -aq)

To delete all the images,

sudo docker rmi -f $(sudo docker images -aq)


sudo docker build -t container-nginx-1 .

sudo docker run --name running-container-nginx-1 -d -p 8080:80 container-nginx-1

sudo docker run --name running-container-nginx-1 -d -p 443:443 container-nginx-1

# nginx

    sudo nginx -t
    sudo nginx -s reload

    sudo systemctl stop nginx
    sudo systemctl start nginx
    sudo systemctl status nginx
