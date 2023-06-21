from flask import Flask

app = Flask(__name__)

@app.route('/')
def SayHello():
    return 'Hello world'

@app.route('/hoge')
def SayHoge():
    return 'hoge'

if __name__ == '__main__':
    app.run(debug=True)
    