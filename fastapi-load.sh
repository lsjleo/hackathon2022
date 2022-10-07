#!/bin/bash

DJANGO_HOME_APP=/home/django


if [ ! -d "$DJANGO_HOME_APP/csc_framework" ] 
then
    cd $DJANGO_HOME_APP
    django-admin startproject csc_framework
fi 

cd $DJANGO_HOME_APP/csc_framework

if [ ! -d "./base_auth" ] 
then
    python3 manage.py startapp base_auth
fi


if [ ! -d "./organograma" ] 
then
    python3 manage.py startapp organograma
fi

# if [ ! -d "./tree" ] 
# then
#     python3 manage.py startapp tree
# fi

if [ ! -d "./meritos_e_promocoes" ] 
then
    python3 manage.py startapp meritos_e_promocoes
fi

# echo 'yes' | python manage.py collectstatic
python3 manage.py makemigrations
python3 manage.py migrate
#python3 manage.py inspectdb > modeltemp.py
python3 manage.py runserver 0.0.0.0:8800