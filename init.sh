sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test
sudo mv /etc/nginx/sites-enabled/test /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
cd /home/box/web
source venv/bin/activate
gunicorn -b 0.0.0.0:8080 -w 2 -p /tmp/gunicorn.pid -D hello:app
