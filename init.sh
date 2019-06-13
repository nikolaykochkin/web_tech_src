sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test
sudo mv /etc/nginx/sites-enabled/test /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
