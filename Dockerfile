FROM ubuntu:21.10
RUN apt-get update -y 
RUN apt-get install nginx -y
RUN apt-get install curl -y 


----------------------------
FROM nginx
RUN rm /etc/nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY ./modules-available /usr/share/nginx/modules-available
COPY ./var/www /usr/share/nginx/html
COPY ./etc/nginx /etc/nginx
COPY ./letsencrypt /letsencrypt

------------------------------

COPY abdhesh /etc/nginx/sites-available/ 
RUN rm -f /etc/nginx/nginx.conf 
COPY  ./nginx.conf  /etc/nginx/
RUN rm -f /etc/nginx/sites-enabled/* 
RUN ln -s /etc/nginx/sites-available/abdhesh /etc/nginx/sites-enabled/ 
EXPOSE 80:80 
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
