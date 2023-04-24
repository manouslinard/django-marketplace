## Creation of Python Venv:
You should initialize the python venv in the same folder as requirements.txt (initial repo folder).<br>To create a python venv, run:
```
python3 -m venv env
```
Then to activate it:
```
source env/bin/activate
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
## Email Verification:
To enable email verificaton, create a .env file in projects root (/puddle) - same directory as the sqlite3 database. Then, declare following values:
```
EMAIL_ACC=your_email
EMAIL_KEY=your_email_key
```
It is important for the .env file to stay in the .gitignore file (so no sensitive information is leaked). Any further sensitive variables should be handled in this way.

---
## Docker Image Creation/Handling:
To create a docker image of this app, run in the same directory as Dockerfile:
```
docker build -t django-marketplace .
```
Then, to run the image, execute:
```
docker run -p 8000:8000 -it --env-file=puddle/.env django-marketplace
```
This command also loads the .env file to the dockerfile - so it is not saved inside of the image (currently .env file is on gitignore).
<br>
To get the container id, run:
```
docker ps
```
To connect to running docker image, run:
```
docker exec -it <container_id> sh
```
Then you can view its contents like normal ubuntu terminal.<br>
To delete the image (entirely), run the following:
```
docker stop $(docker ps -a -q --filter ancestor=django-marketplace --format="{{.ID}}")
docker rm $(docker ps -a -q --filter ancestor=django-marketplace --format="{{.ID}}")
docker rmi django-marketplace
```