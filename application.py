from flask import Flask
import pymysql.cursors

app = Flask(__name__)

connection = pymysql.connect(host='classmysql.engr.oregonstate.edu',
                             user='cs340_gomesr',
                             password='8619',
                             db='cs340_gomesr',
                             charset='utf8mb4',
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
