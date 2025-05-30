from flask import Flask,request

app=Flask(__name__)
@app.route('/')
@app.route('/add')
def index():
    return "Hello world"

def add():
    _a= request.args.get('a',type=int)
    _b= request.args.get('b',type=int)
    return str( _a+_b)
    
# thisiswsc> implement subtraction
#   request: /sub?a=5&b=2
#  response: 3
@app.route('/sub')
def sub():
    _a= request.args.get('a',type=int)
    _b= request.args.get('b',type=int)
    return str( _a-_b)
    
