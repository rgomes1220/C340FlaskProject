import database
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h3>Hello, world from Flask!</h3>'

@app.route('/diagnostic')
def diagnostic():
    mysqlConn = database.connectMySql()
    with mysqlConn.cursor() as cursor:
        sql='SELECT * FROM diagnostic;'
        cursor.execute(sql)
        result = cursor.fetchall()
    return '<h3>' + str(result) + '</h3>'

if __name__=='__main__':
    #app.run(port=8619, host='flip1.engr.oregonstate.edu')
    app.run(port=8619)
