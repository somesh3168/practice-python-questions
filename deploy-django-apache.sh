# cd to file etc/apache2/sites-available
# 000-default.conf,  default-ssl.conf
# add lines into nano 000-default.conf -- before Error Log
# comment out >>> DocumentRoot /var/www/html
Alias /static /var/www/<mongoproj:project_name>/static
<Directory /var/www/<mongoproj:project_name>/static>
  Require all granted
</Directory>
<Directory /var/www/<mongoproj:project_name>/<mongoproj>>
  <Files wsgi.py>
    Require all granted
  </Files>
  Require all granted
</Directory>
..
..
	  Alias /static /var/www/djangomac/static
    <Directory /var/www/djangomac/static>
        Require all granted
    </Directory>
	
	<Directory /var/www/djangomac/djangomacproj>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>
    --------

WSGIDaemonProcess <mongoproj python-path=/var/www/mongoproj python-home=/var/www/mongoproj/env/lib/python3.6/site-packages
WSGIProcessGroup mongoproj
WSGIScriptAlias / /var/www/mongoproj/mongoproj/wsgi.py

... to disable site
sudo a2dissite 000-default.conf
...enable site again
sudo a2ensite 000-default.conf
sudo service apache2 restart

sudo tail /var/log/apache2/error.log

WSGIDaemonProcess mongoproj python-path=/var/www/env python-home=/var/www/mongoproj/mongoproj
    WSGIProcessGroup mongoproj
    WSGIScriptAlias / /var/www/mongoproj/mongoproj/wsgi.py
