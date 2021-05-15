#!/bin/bash
SITENAME="mysite"
APPNAME="myapp"
source env/bin/activate
django-admin.py startproject $SITENAME
cd $SITENAME/
python3 manage.py startapp $APPNAME
cat $SITENAME/urls.py > $APPNAME/urls.py

# python3 manage.py runserver
