#! /bin/bash
clear
echo "Actualizando aplicacion en servidor heroku"
echo
python manage.py makemigrations &&
echo 
git add . --all && git commit -am $1 && git push heroku master && heroku run python manage.py migrate
echo "Gracias Cesar Abel"
