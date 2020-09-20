# Clothing Promotion Competition
Consists of an Angular frontend (promotions-frontend folder) that sends requests to a
Python backend written in Django Rest Framework (promotions-backend folder).

### Run Angular
```
cd promotions-frontend
npm install
ng serve --open
```

### Run Rest Framework Server
create a virtual environment
```
cd promotions_backend
python3 -m venv env
source env/bin/activate
```
install dependencies and run django server
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Code Details

#### Angular Code
Main Angular code is in promotions-frontend/src/app/promotion/
A form is submitted to localhost:8000 (django server) and a message is presented to the user based on whether they've won, lost, duplicate email.
The form has validation making sure all values are entered before a request can go to server.

#### Python Code
Main Python code is in promotions_backend/promotions/viewsets.py, promotions_backend/promotions/serializers.py and promotions_backend/promotions/models.py.
A POST request from the frontend first hits perform_create.  There is a check here to see if the email has been used in the last 24 hours, and if the no new entry is created.  Otherwise the serializer generates a random integer to see if the code wins out of the 5 available codes.  A won or lost status is saved based on this.  The viewset create function then returns a status integer where 1 = Won, 0 = Lost, -1 = duplicate.  These statuses are used to show the appropriate messages for the user in the frontend.
