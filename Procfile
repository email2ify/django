release: python manage.py makemigrations && python manage.py migrate

web: gunicorn django_app.wsgi
