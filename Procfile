release: python manage.py makemigrations award_app
release: python manage.py migrate

web: gunicorn award_project.wsgi --log-file -

