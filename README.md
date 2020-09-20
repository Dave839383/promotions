# Clothing Promotion Competition
Consists of an Angular frontend (promotion-frontend folder) that sends requests to a
Python backend written in Django Rest Framework (promotion-backend folder).

### Run Angular
```
cd promotions-frontend
ng serve --open
```

### Run Rest Framework Server
create a virtual environment
```
python3 -m venv env
source env/bin/activate
```
install dependencies and run server
```
cd promotions_backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
