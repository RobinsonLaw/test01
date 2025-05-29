from flask import Flask,request

app=Flask(__name__)
@app.route('/add')

def add():
    _a= request.args.get('a',type=int)
    _b= request.args.get('b',type=int)
    return str( _a+_b)
    
