# Remove all Images

docker rmi -f $(sudo docker images -aq)

# Remove all Containers

docker rm -vf $(sudo docker ps -aq)

# Pull Image for DockerSpawner

docker pull jupyter/base-notebook:latest

# Create Network

docker network create -d bridge jupyterhub


# Make Image

docker build -t jupyterhub_dockerfile:0.1 .

# Run Container

docker run --rm -it --user jupyterhub --network jupyterhub -v /var/run/docker.sock:/var/run/docker.sock --name jupyterhub_dockerfile -p 8000:8000 jupyterhub_dockerfile:0.1

