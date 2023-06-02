# ####################################
# アプリケーションの核となるファイル
# ------------------------------------
# データベースの設定
# リクエストに応じてHTMLファイルを返す
# ####################################

# =====================
# ライブラリのインポート
# =====================
from flask import Flask, render_template
import os # 暗号鍵生成で使用
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# ==================
# インスタンスの作成
# ==================
app = Flask(__name__)


# ============
# 暗号鍵の生成
# ============
# Flaskではsessionを使う際、session情報を暗号化する為のsession_keyの設定が必要
key = os.urandom(10) # 10桁の乱数を生成
app.secret_key = key # セッション情報の暗号化


# ===================
# データベースとの接続
# ===================
URI = 'sqlite:///trip.db'
app.config['SQLALCHEMY_DATABASE_URI'] = URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Trip(db.Model):
    __tablename__ = 'trip_table'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), unique=True)
    content = db.Column(db.String(300))
    

# ============
# ルーティング
# ============
@app.route('/')
def index():
    title = 'Trip Log : 一覧画面'
    return render_template('index.html', title=title) # titleを渡す


# ===================
# Flaskサーバーの起動
# ===================
if __name__ == '__main__':
    app.run(debug=True)
