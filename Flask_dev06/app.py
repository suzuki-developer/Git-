# ####################################
# アプリケーションの核となるファイル
# ------------------------------------
# データベースの設定
# リクエストに応じてHTMLファイルを返す
# ####################################

# =====================
# ライブラリのインポート
# =====================
from flask import Flask, render_template, request, flash, redirect, url_for
import os                                 # 暗号鍵生成で使用
from flask_sqlalchemy import SQLAlchemy   # ORMを使う為
from datetime import datetime             # DBで日付を扱うのに必要
from create_map import create_map


# ==================
# インスタンスの作成
# ==================
app = Flask(__name__)


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
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
print('------辞書の中身を出力------')
print(app.config)

# Flaskアプリへの関連付け
db = SQLAlchemy(app)                                  

# -----------------------------
# db.Modelを継承したクラスを作成
# -----------------------------
class Trip(db.Model):
    __tablename__ = 'trip_table'                   
    id = db.Column(db.Integer, primary_key=True)   
    title = db.Column(db.String(30), unique=True)  
    content = db.Column(db.String(300))            
    latitude = db.Column(db.String(100))           
    longitude = db.Column(db.String(100))          
    create_date = db.Column(                       
        db.DateTime,
        nullable=False,
        default=datetime.now()
    )

# ------------------------------------------------
# テーブルとデータベースを初期化するための関数を定義
# ------------------------------------------------
# VSCodeのターミナルから実行する（python -m flask initialize_DB）
@app.cli.command('initialize_DB') 
def initialize_DB():              
    db.create_all()               
    print('データベースの初期化が完了しました。')


# ============
# ルーティング
# ============

# --------
# 一覧画面
# --------
@app.route('/')
def index():
    title = 'Trip Log : 一覧画面'
    # DBからデータを全て取得
    all_data = Trip.query.all() 
    print('-------DBから取得したデータ-------')
    print(all_data)
    return render_template('index.html', title=title, all_data=all_data) 

# ------------
# 新規作成画面
# ------------
@app.route('/new')
def new():

    title = 'Trip Log : 新規作成'
    return render_template('new.html', title=title) 

# -----------------------
# データベースへの登録処理
# -----------------------
@app.route('/create', methods=['POST'])
def create():
    # フォームに入力されたname属性を取得して変数に格納
    title = request.form['title']             
    
    # titleに値が入力されているか判定
    if title:                                 
        # フォームに入力されたname属性を取得して変数に格納
        content = request.form['content']   
        latitude = request.form['latitude']
        longitude = request.form['longitude']

        # フォームから入力されたデータを Trip モデルのインスタンスに格納
        register_data = Trip(
            title = title,
            content = content,
            latitude = latitude,
            longitude = longitude
        )

        # インスタンス化した登録データをDBに追加
        db.session.add(register_data)

        # 確定
        db.session.commit()
        flash('登録できました') 

        return redirect(url_for('index'))
    else:
        flash('作成できませんでした。入力内容を確認してください') 
        return redirect(url_for('index'))

# --------
# 詳細画面
# --------
@app.route('/detail') 
def detail():
    title = 'Trip Log : 詳細画面'
    id = request.args.get('id') 
    data = Trip.query.get(id)                    
    map = create_map(data.latitude, data.longitude) 
    return render_template('detail.html', title=title, data=data, map=map)


# ===================
# Flaskサーバーの起動
# ===================
if __name__ == '__main__':
    app.run(debug=True)
