
ssh-keygen -t rsa -f ~/.ssh/key202204220954 -C andrew_gaitskell -b 2048

cd ~/.ssh

cat key202204220954.pub

copy output and paste into VM ssh keys

remove key202203251421.pub at start

connect to vm

ssh -i ~/.ssh/key202204220954 andrew_gaitskell@35.214.5.254


