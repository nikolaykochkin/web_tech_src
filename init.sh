#!/usr/bin/env bash
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test
sudo mv /etc/nginx/sites-enabled/test /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn-wsgi.conf /etc/gunicorn.d/test-wsgi
sudo /etc/init.d/gunicorn restart
