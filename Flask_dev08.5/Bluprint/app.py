from flask import Flask
from app2 import hello 
from app2 import hoge  

app = Flask(__name__)

app.register_blueprint(hello)
app.register_blueprint(hoge)


if __name__ == '__main__':
    app.run(debug=True)