Managing Content and Configuration Files
There are several ways you can manage both the content served by NGINX and the NGINX configuration files. Here we cover a few of the options.

Option 1 – Maintain the Content and Configuration on the Docker Host
When the container is created we can tell Docker to mount a local directory on the Docker host to a directory in the container. The NGINX image uses the default NGINX configuration, which uses /usr/share/nginx/html as the container’s root directory and puts configuration files in /etc/nginx. For a Docker host with content in the local directory /var/www and configuration files in /var/nginx/conf, run this command (which appears on multiple lines here only for legibility):

# docker run --name mynginx2 --mount type=bind source=/var/www,target=/usr/share/nginx/html,readonly --mount type=bind,source=/var/nginx/conf,target=/etc/nginx/conf,readonly -p 80:80 -d nginx
Now any change made to the files in the local directories /var/www and /var/nginx/conf on the Docker host are reflected in the directories /usr/share/nginx/html and /etc/nginx in the container. The readonly option means these directories can be changed only on the Docker host, not from within the container.

Option 2 – Copy Files from the Docker Host
Another option is to have Docker copy the content and configuration files from a local directory on the Docker host during container creation. Once a container is created, the files are maintained by creating a new container when files change or by modifying the files in the container. A simple way to copy the files is to create a Dockerfile with commands that are run during generation of a new Docker image based on the NGINX image from Docker Hub. For the file‑copy (COPY) commands in the Dockerfile, the local directory path is relative to the build context where the Dockerfile is located.

In our example, the content is in the content directory and the configuration files are in the conf directory, both subdirectories of the directory where the Dockerfile is located. The NGINX image includes default NGINX configuration files as /etc/nginx/nginx.conf and /etc/nginx/conf.d/default.conf. Because we instead want to use the configuration files from the host, we include a RUN command that deletes the default files:

FROM nginx
RUN rm /etc/nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY content /usr/share/nginx/html
COPY conf /etc/nginx
We create our own NGINX image by running the following command from the directory where the Dockerfile is located. Note the period (“.”) at the end of the command. It defines the current directory as the build context, which contains the Dockerfile and the directories to be copied.
