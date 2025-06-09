from flask import Flask,request,make_response,render_template,send_from_directory
try:
    from .utils.auth import encode,decode
except ImportError:
    from utils.auth import encode,decode

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('home.html')

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
    
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('public', 'favicon.ico')
@app.route('/favicon.png')
def favicon_png():
    return send_from_directory('public', 'favicon.png')

if __name__ == "__main__":
    app.run(debug=True)
