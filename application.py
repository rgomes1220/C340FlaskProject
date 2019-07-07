from flask import Flask
from database import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    with connection.cursor() as cursor:
        sql='select * from bsg_cert_people'
        cursor.execute(sql)
        result = cursor.fetchall()
    # return '<h3>' + str(result[1]['cid']) + '</h3>'
    return '<h3>' + str(result) + '</h3>'

@app.route('/diagnostic')
def diagnostic():
    with connection.cursor() as cursor:
        sql='SELECT * FROM diagnostic;'
        cursor.execute(sql)
        result = cursor.fetchall()
    return '<h3>' + str(result) + '</h3>'

if __name__=='__main__':
    app.run(port=8619, debug=True)
