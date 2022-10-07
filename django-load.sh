#!/bin/bash

DJANGO_HOME_APP=/home/django


if [ ! -d "$DJANGO_HOME_APP/hackathon" ] 
then
    cd $DJANGO_HOME_APP
    django-admin startproject hackathon
fi 

cd $DJANGO_HOME_APP/hackathon

if [ ! -d "$DJANGO_HOME_APP/hackathon/startrack" ] 
then
    python3 manage.py startapp startrack
fi

# echo 'yes' | python manage.py collectstatic
python3 manage.py makemigrations
python3 manage.py migrate
# python3 manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'startrack@hackathon.com', 'startrack')"
#python3 manage.py inspectdb > modeltemp.py
python3 manage.py runserver 0.0.0.0:8800
