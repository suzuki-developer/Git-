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
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
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

# --------
# 編集画面
# --------
# パスは文字列の為、idを整数型に変換
@app.route('/edit/<int:id>', methods=['GET'])
def edit(id):
    title = 'Trip Log : 編集画面'
    data = Trip.query.get(id)
    return render_template('edit.html', title=title, data=data)

# --------------
# DBへの登録処理
# --------------
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

        # フォームに入力されたname属性の確認
        print('------フォームに入力されたname属性の確認------')
        print(title)
        print(content)
        print(latitude)
        print(longitude)

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

# ------------------
# レコードの更新処理
# ------------------
@app.route('/update', methods=['POST'])
def update():
    # リクエストフォームから送信されてきたidを取得
    id = request.form['id']

    # 送られてきたidのレコードを取得
    edit_data = Trip.query.get(id)

    # フォームで入力された値に置き換える
    edit_data.title = request.form['title']
    edit_data.content = request.form['content']
    edit_data.latitude = request.form['latitude']
    edit_data.longitude = request.form['longitude']

    # edit_dataの型を確認
    print('------edit_dataの型を確認------')
    print(type(edit_data))

    # idを確認
    print('------idの確認------')
    print(id)

    # edit_dataの中身を確認
    print('------edit_dataの中身を確認------')
    print(edit_data)

    # edit_dataの各要素の型を確認
    print('------edit_dataの各要素を確認------')
    print(type(edit_data.title))
    print(type(edit_data.content))
    print(type(edit_data.latitude))
    print(type(edit_data.longitude))

    # edit_dataの各要素の中身を確認
    print('------edit_dataの各要素を確認------')
    print(edit_data.title)
    print(edit_data.content)
    print(edit_data.latitude)
    print(edit_data.longitude)


    # 編集したデータをDBに更新
    db.session.merge(edit_data)

    # 確定
    db.session.commit()
    flash('更新しました')
    return redirect(url_for('index')) 

# ------------------
# レコードの削除処理
# ------------------
@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    # 送られてきたidのレコードを取得
    delete_data = Trip.query.get(id)
    
    # 該当するidのレコードを削除
    db.session.delete(delete_data)

    # 確定
    db.session.commit()
    flash('削除しました')
    return redirect(url_for('index'))


# ===================
# Flaskサーバーの起動
# ===================
if __name__ == '__main__':
    app.run(debug=True)
