from flask import Flask,request,make_response
from .utils.auth import encode,decode

app=Flask(__name__)
@app.route('/')
def index():
    return "Hello world"

@app.route('/getkey')
def getkey():
    return encode()

@app.route('/verify')
def verify():
    token=request.args.get('token',type=str)
    err = decode(token)
    if err==0:
        return "Decoded JWT"
    if err==1:
        return make_response("Token has expired",410)
    if err==2:
        return make_response("Invalid token",401)
     


@app.route('/add')
def add():
    _a= request.args.get('a',type=int)
    _b= request.args.get('b',type=int)
    token=request.args.get('token',type=str)
    err = decode(token)
    if err==0:
        return str( _a+_b)
    if err==1:
        return make_response("Token has expired",410)
    if err==2:
        return make_response("Invalid token",401)
    
    
# thisiswsc> implement subtraction
#   request: /sub?a=5&b=2
#  response: 3
@app.route('/sub')
def sub():
    _a= request.args.get('a',type=int)
    _b= request.args.get('b',type=int)
    return str( _a-_b)
    
