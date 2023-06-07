# ####################################
# アプリケーションの核となるファイル
# ------------------------------------
# データベースの設定
# リクエストに応じてHTMLファイルを返す
# ####################################

# =====================
# ライブラリのインポート
# =====================
from flask import Flask, render_template, request, flash, redirect, url_for, Blueprint
import os                                 # 暗号鍵生成で使用
from flask_sqlalchemy import SQLAlchemy   # ORMを使う為
from datetime import datetime             # DBで日付を扱うのに必要
from create_map import create_map
from display import index_bp, new_bp, detail_bp, edit_bp
from database import create_bp, update_bp, delete_bp

# ==================
# インスタンスの作成
# ==================
app = Flask(__name__)


# =================================================
# BlueprintオブジェクトをFlaskアプリケーションに登録
# =================================================

# --------
# 画面遷移
# --------
app.register_blueprint(index_bp)
app.register_blueprint(new_bp)
app.register_blueprint(detail_bp)
app.register_blueprint(edit_bp)

# -------
# DB関係
# -------
app.register_blueprint(create_bp)
app.register_blueprint(update_bp)
app.register_blueprint(delete_bp)


# ============
# 暗号鍵の生成
# ============
key = os.urandom(10) 
app.secret_key = key 


# ================
# データベース関係
# ================
# DBの作成、設定
URI = 'sqlite:///trip.db'                             
app.config['SQLALCHEMY_DATABASE_URI'] = URI           
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
print('------辞書の中身を出力------')
print(app.config)

# Flaskアプリへの関連付け
db = SQLAlchemy(app)   

# ------------------------------------------------
# テーブルとデータベースを初期化するための関数を定義
# ------------------------------------------------
# VSCodeのターミナルから実行する（python -m flask initialize_DB）
@app.cli.command('initialize_DB') 
def initialize_DB():              
    db.create_all()               
    print('データベースの初期化が完了しました。')
    

# ===================
# Flaskサーバーの起動
# ===================
if __name__ == '__main__':
    app.run(debug=True)
