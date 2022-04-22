# install virtual env

sudo apt install -y python3-venv

# create jupyterhub folder

mkdir jupyterhub
cd jupyterhub

# create env

python3 -m venv env

# activate env

source venv/bin/activate


download

/home/andrew_gaitskell/jupyterhub/jupyterhub_config.py

## start & stop service

sudo systemctl stop jupyterhub
