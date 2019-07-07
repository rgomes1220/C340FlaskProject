# Project for CS 340 Databases

## Configuration

### Database connection

Copy `config/database.yml.sample` to `config/database.yml` and update accordingly.

### Database schema

The schema can be loaded by running the following command (replace the user/database as necessary):

```
mysql -u cs340_reynokel -p -h classmysql.engr.oregonstate.edu cs340_reynokel < schema.sql
```

## Running

### Locally

```
python application.py
```
or from command line

```
export FLASK_APP=application.py
flask run
```

### On Flip

**NOTE** Be sure tochange application.py to `app.run(host='flipX.engr.oregonstate.edu', port=####)`

```
python3 -m venv DatabasesPythonEnv
source ~/classes/databases/DatabasesPythonEnv/bin/activate.csh
pip freeze --local > ./CS340FlaskProject/requirements.txt
npm install forever
./node_modules/forever/bin/forever start -c python3 ./CS340FlaskProject/application.py
```

# Additional Resources

## Mysql for flask

https://pymysql.readthedocs.io/en/latest/index.html
https://github.com/PyMySQL/PyMySQL
https://www.python.org/dev/peps/pep-0249/#cursor-objects
