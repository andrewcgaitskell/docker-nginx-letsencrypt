# install virtual env

sudo apt install -y python3-venv

# create jupyterhub folder

mkdir jupyterhub
cd jupyterhub

# create env

python3 -m venv env

# activate env

source venv/bin/activate

# install jupyterhub

https://jupyterhub.readthedocs.io/en/stable/quickstart.html

python3 -m pip install jupyterhub

npm install -g configurable-http-proxy

python3 -m pip install jupyterlab notebook  # needed if running the notebook servers in the same environment



download

/home/andrew_gaitskell/jupyterhub/jupyterhub_config.py

## start & stop service

sudo systemctl stop jupyterhub
