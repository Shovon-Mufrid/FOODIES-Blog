# FOODIES-Blog
 This is a blog site made with Django & Bootstrap


<!-- Installing  -->
$ python -m venv venv

$ pip install -r requirements.txt

$ python manage.py migrate
$ python mangage.py makemigrations
$ python manage.py migrate

$ python manage.py runserver


<!-- SECURITY -->
$ python manage.py check --deploy

% Database Json Convert
python manage.py dumpdata > food.json

python manage.py loaddata food.json
