## https://medium.com/@abdhesh_7570/how-to-setup-nginx-server-on-ubuntu-18-04-dockerfile-ecde2f4a3029

FROM ubuntu:21.10
RUN apt-get update -y 
RUN apt-get install nginx -y
RUN apt-get install curl -y 
COPY ./letsencrypt /letsencrypt
COPY ./var/www /usr/share/nginx/html

RUN rm -f /etc/nginx/nginx.conf
COPY ./etc/nginx /etc/nginx
COPY ./sites-available /etc/nginx/sites-available/

#RUN rm -f /etc/nginx/sites-enabled/* 
#RUN ln -s /etc/nginx/sites-available/* /etc/nginx/sites-enabled/

#EXPOSE 443:443 
#CMD ["/usr/sbin/nginx", "-g", "daemon off;"]

