For Linux

To delete all containers including its volumes use,

sudo docker rm -vf $(sudo docker ps -aq)

To delete all the images,

sudo docker rmi -f $(sudo docker images -aq)
