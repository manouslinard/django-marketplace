To make a python venv, run:
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
