from flask import Blueprint

hello = Blueprint('hello', __name__) 
hoge  = Blueprint('hoge', __name__)

@hello.route('/')
def SayHello():
    return 'Hello world'

@hoge.route('/hoge')
def SayHoge():
    return 'hoge'

