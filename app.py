from flask import Flask

app = Flask(__name__)

@app.route("/hello1")
def hello_world1():
    return "Hello, World1!"

@app.route("/hello2")
def hello_world2():
    return "Hello, World2!"

@app.route('/age_finder')
def age():
    a = 2023 - 1994
     
    return 'the age is {}'.format(a)

from flask import request
@app.route('/input')
@app.route('/input')
def input_req():
    data = int(request.args.get('x'))
    data1 = int(request.args.get('y'))
    data3 = data1 + data
    return 'This is the input: {}'.format(data3)

if __name__=="__main__":
    app.run(host="0.0.0.0")
