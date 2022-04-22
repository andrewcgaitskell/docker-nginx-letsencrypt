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

# B4 The default server
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

    location /hello/ {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_pass http://127.0.0.1:8080/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        # location /overview {
        #     proxy_pass http://127.0.0.1:3000$request_uri;
        #     proxy_redirect off;
        # }
    }


    location /dev/ {
        proxy_pass http://localhost:5050/dev/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

    error_page  404              /404.html;
    location = /404.html {
        root   /usr/share/nginx/html;
    }

    # redirect server error pages to the static page /50x.html
    #
    }



certbot --nginx -d dev1.dmtools.info
    
 
IMPORTANT NOTES:
 - Unable to install the certificate
 - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/dev1.dmtools.info/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/dev1.dmtools.info/privkey.pem
   Your certificate will expire on 2022-07-21. To obtain a new or
   tweaked version of this certificate in the future, simply run
   certbot again with the "certonly" option. To non-interactively
   renew *all* of your certificates, run "certbot renew"

# setup server blocks

https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04#step-5-%E2%80%93-setting-up-server-blocks-(recommended)


