# ===========================
# 必要なライブラリのインポート
# ===========================
from flask import Flask, render_template, session, request, redirect, url_for
import os # 暗号鍵作成で使用


# ==================
# インスタンスの作成
# ==================
app = Flask(__name__)


# ============
# 暗号鍵の生成
# ============
# Flaskではsessionを使う際、session情報を暗号化する為のsession_keyの設定が必要
key = os.urandom(21) # 21桁の乱数を作成
app.secret_key = key


# ============================================
# ログインするためのユーザーIDとパスワードを作成
# ============================================
id_pwd = {'suzuki': '12345'}


# ============
# ルーティング
# ============

# ------
# メイン
# ------
@app.route('/')
def index():
    if not session.get('login'):             # loginセッションがないかどうか判定
        return redirect(url_for('login'))    # def loginが走る
    else:
        return render_template('index.html') # index.htmlを表示させる

# --------
# ログイン
# --------
@app.route('/login')
def login():
    return render_template('login.html')

# ------------
# ログイン認証
# ------------
@app.route('/logincheck', methods=['POST'])
def logincheck():
    # フォームで入力されたユーザーIDとパスワードを変数に格納
    user_id = request.form['user_id']
    password = request.form['password']

    # ユーザーIDとパスワードをチェック
    if user_id in id_pwd:                 # user_idがid_pwdという辞書のキーとして存在するかをチェック
        if password == id_pwd[user_id]: # 入力されたパスワードが、id_pwdという辞書の中で対応するユーザーIDのパスワードと一致するかどうかをチェック
            session['login'] = True       # session['login']にTrueをセット
        else:
            session['login'] = False      # session['login']にFalseをセット
    else:                                 # 力されたユーザーIDが登録されていない場合
        session['login'] = False

    # リダイレクト
    # redirect関数 引数に与えられたページに転送する
    # url_for関数  引数に与えられた関数を実行する
    if session['login']:                  # TrueかFalseであるか判定
        return redirect(url_for('index')) # Trueの場合  def indexが走る
    else:
        return redirect(url_for('login')) # Falseの場合 def loginが走る
    
# ----------
# ログアウト
# ----------
@app.route('/logout')
def logout():
    session.pop('login', None)        # セッションを削除
    return redirect(url_for('index')) # def indexが走る

# =====================
# アプリケーションの起動
# =====================
if __name__ == '__main__':
    app.run(debug=True)