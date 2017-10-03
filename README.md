SomosPool API
====

[![Build Status](https://travis-ci.org/garciadiazjaime/api-notablemint.svg)](https://travis-ci.org/garciadiazjaime/api-notablemint)

API SomosPool portfolio

Technologies:
django + djangorest


Package Installation
`pip install -r requirements.txt`

Run Server
`cd project`
`python manage.py runserver`

GUI - Admin
http://127.0.0.1:8000/admin

DB Setup
`psql -c create database notable -U postgres`
`python manage.py migrate`
`python manage.py createsuperuser` (this is the user for access the admin, feel free to type anything)
`python manage.py loaddata ../fixtures/portfolio.json` (warnings are OK)

Drop Database
`psql -c drop database notable`

Deploy project
`fab update`
`git status`
`git diff`
`fab deploy`

Login rch
rhc -l setup email

Remove Cartridge
http://stackoverflow.com/questions/31323791/how-do-you-delete-a-database-cartridge-on-an-openshift-app

Setting up Envs
rhc env set DB_NAME=value -a api
rhc env set DB_USER=value -a api
rhc env set DB_PASSWORD=value -a api
rhc env set DJANGO_SETTINGS_MODULE=settings.prod -a api

Checking Envs
rhc env list -a api

docker build -t garciadiazjaime/api-notable .
docker run -d -p 49178:3078 garciadiazjaime/api-notable
docker push garciadiazjaime/api-notable
docker pull garciadiazjaime/api-notable
