# Project for CS 340 Databases

**Running locally**  
python application.py  
or from command line
export FLASK_APP=application.py  
flask run  


**On Flip**  
python3 -m venv DatabasesPythonEnv  
source ~/classes/databases/DatabasesPythonEnv/bin/activate.csh  
pip freeze --local > ./CS340FlaskProject/requirements.txt  
npm install forever  
* change application.py to `app.run(host='flipx.engr.oregonstate.edu', port=####)`  

./node_modules/forever/bin/forever start -c python3 ./CS340FlaskProject/application.py

**Mysql for flask**  
https://pymysql.readthedocs.io/en/latest/index.html  
https://github.com/PyMySQL/PyMySQL  
https://www.python.org/dev/peps/pep-0249/#cursor-objects  
