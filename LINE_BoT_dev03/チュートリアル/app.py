# モジュールのインポート
from flask import Flask, redirect, url_for, request

# おまじない
app = Flask(__name__)

# ルーティングの基本
@app.route('/') # デコレータ
def index():    # '/'にアクセスした時に実行される関数
    return 'Hello World'

@app.route('/hoge')
def hoge():
    return 'hoge'

# リダイレクト
@app.route('/hello')
def hello():
    return redirect("/")

# 指定した関数に対応するルーティングにリダイレクト
@app.route('/sage')
def sage():
    return redirect(url_for('index'))

# 特定のルーティングでメソッドを切り分けてアクセスを振り分ける
# '/my'に'GET'でアクセスした場合
@app.route('/my', methods=['GET'])
def my_route_get():
    return 'GET'

# '/my'に'POST'でアクセスした場合 
@app.route('/my', methods=['POST'])
def my_route_post():
    return 'POST'

# -----------------------------------------------
# 上記のコードはif文で分岐させることも可能
# -----------------------------------------------
# @app.route('/my', methods=['GET', 'POST'])
# def my_route():
#     if request.method == 'GET':
#         return 'GET'
#     elif request.method == 'POST':
#         return 'POST'
# -----------------------------------------------

# おまじない
# この部分を書かない場合は、ターミナルで'FLASK_APP=app.py flask run'を打つ ⇒ 動かない
if __name__ == "__main__":
    app.run(debug=True)