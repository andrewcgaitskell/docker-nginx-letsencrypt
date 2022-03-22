FROM nginx
RUN rm /etc/nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY ./modules-available /usr/share/nginx/modules-available
COPY ./var/www /usr/share/nginx/html
COPY ./etc/nginx /etc/nginx
COPY ./letsencrypt /letsencrypt

