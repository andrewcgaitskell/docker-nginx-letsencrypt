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

## create service

nano /lib/systemd/system/jupyterhub.service


## start & stop service

sudo systemctl stop jupyterhub

# create shared folder

cd  /usr/local/share

sudo groupadd jupyterhub

sudo usermod -a -G jupyterhub

sudo chgrp -R jupyterhub /usr/local/share/jupyterhub

sudo chmod -R 2775 /usr/local/share/jupyterhub


sudo usermod -a -G jupyterhub jupyterhub


python3 -m venv env

source env/bin/activate


pip install jupyterhub

pip install jupyterlab notebook

jupyterhub --generate-config

jupyter --data-dir


nano /lib/systemd/system/jupyterhub.service

source env/bin/activate

pip install jupyterhub

sudo journalctl -u jupyterhub -n 100 --no-pager


sudo systemctl status jupyterhub

pip install jupyterhub-firstuseauthenticator

nano jupyterhub_config.py
