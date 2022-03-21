FROM nginx
RUN rm /etc/nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY ./var/www /usr/share/nginx/html
COPY ./etc/nginx /etc/nginx
