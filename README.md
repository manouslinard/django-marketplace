# Prerequisites
## Python Venv:
You should initialize the python venv in the same folder as requirements.txt (initial repo folder).<br>To create a python venv, run:
```
python3 -m venv env
```
Then to activate it:
```
source env/bin/activate
```
Once you activated the venv, you can install the requirements of the app like so (from project directory):
```
pip install -r puddle/requirements.txt
```
If you want to delete the venv, run:
```
sudo rm -rf env
```

---
## User accounts:
### Default admin account:
username: admin
<br>
password: pass123

### Default user account:
username: user
<br>
password: pass123456

---
## Environment Variables:
All the environmnent variables used in this project are inside the file: .env (located in the app directory - the same as data.json). The fields required in this file are:
```
DEBUG=<set values 1 or 0, where 1 is true and 0 false>
PAGE_DOMAIN=<your_page_domain>
SECRET_KEY=<your_secret_key>
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
DATABASE=postgres
SQL_PORT=5432
POSTGRES_USER=<name_of_psql_user>
POSTGRES_PASSWORD=<password_of_psql_user>
POSTGRES_DB=<name_of_psql_db>
EMAIL_ACC=<your_email>
EMAIL_KEY=<your_email_key>
```
The EMAIL_ACC and EMAIL_KEY variables are used to send email verification. Make sure to have configured your email account correctly so it will be available to send email verifications. 
<br>
Also, in PAGE_DOMAIN variable, you put your website domain (it is used for the link for email verification). The project's page domain is usually http://localhost:8000/
<br>
It is important for the .env file to stay in the .gitignore file (so no sensitive information is leaked). Any further sensitive variables should be handled in this way.

---
# Docker Execution
## Docker Compose:
To build the docker-compose file, run:
```
docker-compose build
```
Then to run the image, run:
```
docker-compose up -d
```
To stop, run:
```
docker-compose down -v
```
You can check if the docker works correctly by visiting http://localhost:8000/
<br>
Also, you can set env variable DEBUG = 0 (false), because all the media files are served from nginx and gunicorn in docker.

---
## Docker Handling:
To get the container id, run:
```
docker ps
```
To connect to running docker image, run:
```
docker exec -it <container_id> sh
```
Then you can view its contents like normal ubuntu terminal.

---
# Local Execution
## Run app (without Docker):
To run the app without docker compose, go to the app's folder (/puddle) and run:
```
python manage.py runserver
```
This should run the app on http://localhost:8000/ without the need for docker compose (works only with env var DEBUG=1, because propably nginx and gunicorn is not configured to your local machine - here is a [tutorial](https://pylessons.com/django-deployment) to configure it).

---
## Psql Local Config:
In the development phase, <name_of_psql_db> = markeplace, thus the following commads:<br>
To create required db, run:
```
createdb -h localhost -p 5432 -U postgres marketplace
```
It is also important to set the postgres user's password to 'pass123' for django app to work.<br>
To delete created db, run:
```
dropdb -h localhost -p 5432 -U postgres marketplace
```
There is also a data.json file which has default values for db. To load it, run on the project's folder (puddle folder where the data.json file is):
```
python manage.py migrate --run-syncdb
python manage.py loaddata data.json
```