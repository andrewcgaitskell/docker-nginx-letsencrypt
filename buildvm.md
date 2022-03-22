ubuntu 21.10

# nginx

    sudo su
    apt uodate
    apt upgrade -y
    apt install nginx -y

# check nginx

    sudo nginx -t
    sudo nginx -s reload

    sudo systemctl stop nginx
    sudo systemctl start nginx
    sudo systemctl status nginx

# docker

    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh
    

        
