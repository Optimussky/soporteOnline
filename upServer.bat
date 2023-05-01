#rem crear proyecto django

echo "Después de crear el entorno virtual se instalará lo siguiente:"
echo "Instalando Django 3.2"

pipenv install django==3.2
echo "django==3.2 instalado"


echo "Creando proyecto con django-admin startproject %1 ."
django-admin startproject %1 .

echo "Creando App con django-admin startapp %2"
django-admin startapp %2

echo "Creando migraciones con makemigrations"
python manage.py makemigrations

echo "Creando migración con migrate"
python manage.py migrate

echo "Creando super usuario"
python manage.py createsuperuser


echo "*********************************************"
echo "Instalación completada"

echo "*********************************************"
echo "Levantar servidor en el puerto 0.0.0.0:%3"
python manage.py runserver 0.0.0.0:%3