# Clothing Promotion Competition
Consists of an Angular frontend (promotion-frontend folder) that sends requests to a
Python backend written in Django Rest Framework (promotion-backend folder).

### To Run
create a virtual environment
```
python3 -m venv env
source env/bin/activate
```

### Run Angular
```
cd promotions-frontend
ng serve --open
```

### Run Rest Framework Server
```
pip install -r requirements.txt
cd promotions_backend
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
