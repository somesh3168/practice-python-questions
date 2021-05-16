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

WSGIDeamonProcess <mongoproj> python-path=/var/www/mongoproj python-home=/var/www/<env:virtualenv path>
WSGIProcessGroup mongoproj
WSGIScriptAlias / /var/www/mongoproj/mongoproj/wsgi.py

... to disable site
sudo a2dissite 000-default.conf
...enable site again
sudo a2ensite 000-default.conf

WSGIDaemonProcess djangomac python-path=/var/www/djangomac python-home=/var/www/djangomac/djangomac
    WSGIProcessGroup djangomac
    WSGIScriptAlias / /var/www/djangomac/djangomacproj/wsgi.py
