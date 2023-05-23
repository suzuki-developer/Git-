# 参考書籍 Python & Flask 初めてのWebアプリケーション作成に挑戦!!

# 必要なモジュールのインポート
from flask import Flask, render_template, session, request, redirect, url_for
import os # 暗号鍵の生成に必要

# インスタンスの作成
app = Flask(__name__)

# 暗号鍵の生成
key = os.urandom(21) # 引数に任意の整数値を設定するとその桁数のランダムな値が生成される
app.secret_key = key

# app.pyにログインするためのユーザーIDとパスワードを生成
id_pwd = {'suzuki' : '1234'}

# メイン
@app.route('/') # ルーティング
def index():    # 上記のURLにアクセスがあった場合の挙動
    if not session.get('login'): 
        return redirect(url_for('login')) # loginセッションがない場合login関数へ
    else:
        return render_template('index.html') # loginセッションがある場合はindex.htmlを表示

@app.route('/login')
def login():
    return render_template('login.html')

# ログイン認証
@app.route('/logincheck', methods=['POST'])
def logincheck():
    user_id = request.form['user_id']   # login.htmlで入力された値を取り出して変数に格納
    password = request.form['password'] # login.htmlで入力された値を取り出して変数に格納

    # ---------------------------------------------------------------------
    # 取得したログインIDとパスワードがid_pwdに含まれているか判定
    # IDとパスワードが両方含まれている　⇒　True　を　session['login']　に格納
    # そうでない場合　　　　　　　　　　⇒　False を　session['login']　に格納
    # ---------------------------------------------------------------------
    if user_id in id_pwd:
        if password == id_pwd[user_id]:
            session['login'] = True
        else:
            session['login'] = False
    else:
        session['login'] = False

    if session['login']:
        return redirect(url_for('index')) # Trueの場合
    else:
        return redirect(url_for('login')) # Falseの場合
    
# ログアウト
@app.route('/logout')
def logout():
    session.pop('login', None) # セッションを削除
    return redirect(url_for('index'))

# アプリケーションの起動
if __name__ == '__main__':
    app.run(debug=True) # 引数を指定することで、エラーを表示

