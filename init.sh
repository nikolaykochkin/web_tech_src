#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install -y python3.5
sudo apt-get install -y python3.5-dev
sudo unlink /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
virtualenv -p python3 venv

sudo unlink /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE ask;"
mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED BY '123';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON ask.* TO 'box'@'localhost' WITH GRANT OPTION;"

#sudo ln -s /home/box/web/etc/gunicorn-wsgi.conf /etc/gunicorn.d/test-wsgi
#sudo /etc/init.d/gunicorn restart
