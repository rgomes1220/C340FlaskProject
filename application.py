from flask import Flask
import pymysql.cursors
import yaml

app = Flask(__name__)

config = {}
with open("config/database.yml", 'r') as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        exit(1)

connection = pymysql.connect(host=config['host'],
                         user=config['user'],
                         password=config['password'],
                         db=config['db'],
                         charset=config['charset'],
                         cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def hello_world():
    with connection.cursor() as cursor:
        sql='select * from bsg_cert_people'
        cursor.execute(sql)
        result = cursor.fetchall()
    # return '<h3>' + str(result[1]['cid']) + '</h3>'
    return '<h3>' + str(result) + '</h3>'


if __name__=='__main__':
    app.run(port=8619, debug=True)
