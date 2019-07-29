# Project for CS 340 Databases

## Configuration

### Database connection

Copy `config/database.yml.sample` to `config/database.yml` and update accordingly.

### Database schema

The schema can be loaded by running the following command (replace the user/database as necessary):

```
mysql -u cs340_osuLogin -p -h classmysql.engr.oregonstate.edu cs340_osuLogin
source schema.sql
```

## Running


Create a python virtual environment if not already present, activate it, and install needed packages from requirements.txt
```
python3 -m venv DatabasesPythonEnv
source ~/classes/databases/DatabasesPythonEnv/bin/activate.csh
pip install -r requirements.txt
```

### Locally

**Note:** To run in debug mode, add a python shebang to the app.py file
```
#!/path/to/virtualenv/python
```

Running the app.py file will start a local development server
```
python app.py
```

Or you can use the flask cli. Note this will not use the arguments defined in `app.run` in app.py.

```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

### On Flip

**NOTE** Be sure to change app.py to `app.run(host='flipX.engr.oregonstate.edu', port=####)`

Run the app with npm forever to allow it to persist once you disconnect from a flip ssh session.
```
npm install forever
./node_modules/forever/bin/forever start -c python3 ./CS340FlaskProject/app.py
```
View running processes: `./node_modules/forever/bin/forever list`
Stop all running processes: `./node_modules/forever/bin/forever stopall`


# Additional Resources

## Mysql for flask

* https://pymysql.readthedocs.io/en/latest/index.html
* https://github.com/PyMySQL/PyMySQL
* https://www.python.org/dev/peps/pep-0249/#cursor-objects


## Dependencies

This will generate a requirements.txt file if new packages are installed in the environment or if the environment is created from scratch
```
pip freeze --local > requirements.txt
```
