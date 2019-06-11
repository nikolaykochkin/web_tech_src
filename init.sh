sudo mkdir -p /var/www/web
sudo chown -R $USER:$USER /var/www/web
sudo chmod -R 755 /var/www/web
git clone https://github.com/nikolaykochkin/web_tech_src /var/www/web
sudo ln -s /var/www/web/etc/nginx.conf /etc/nginx/sites-enabled/test
sudo mv /etc/nginx/sites-enabled/test /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
