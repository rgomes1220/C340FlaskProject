from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h3>Hello CS 340 Databses!!</h3>'


if __name__=='__main__':
    app.run(port=8619, debug=True)
