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
    

# check nginx config and reload

    sudo nginx -t
    sudo nginx -s reload


# install node

# now looking at node and how to connect containers

    apt update
    apt install nodejs npm


# install venv

# activate venv

# letsencrypt

apt install certbot python3-certbot-nginx

certbot --nginx -d dev1.dmtools.info
    
    
