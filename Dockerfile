FROM nginx
COPY static-html-directory /usr/share/nginx/html
COPY ./nginx /etc/nginx/conf.d
