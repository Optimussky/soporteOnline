#!/bin/bash
echo "Este Bash ejecuta o crea el entorno para automatizarlo para Django"
echo "Instalación de Django=3.2"
pipenv install django==3.2
echo "Django 3.2 instalado"
echo ""
echo "Creando django-admin startproject $1 ."
django-admin startproject $1 .
echo "startproject $1 creado"
django-amin startpp $2
echo "startapp $2 creada"
echo ""
echo "Crear migraciones migrate y makemigrations"
python3 manage.py migrate
python3 manage.py makemigrations
python3 manage.py migrate

echo "Migraciones creadas para crear un super usuario"
python3 manage.py createsuperuser
echo "Super usuario creado"
echo "Levantar servidor con el puerto deseado"

python3 manage.py runserver $3
