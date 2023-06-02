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
# Flaskではsessionを使う際、session情報を暗号化する為のsession_keyの設定が必要
key = os.urandom(10) # 10桁の乱数を生成
app.secret_key = key # セッション情報の暗号化


# ================
# データベース関係
# ================

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# app.configについて
# 
# Flaskの設定オブジェクトで、アプリの設定を行うことができる
# 辞書形式であり、設定を格納することができる
# app.config['KEY1'] = 'value1'
# 上記は、app.configという辞書にキーと値を格納する文法
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
URI = 'sqlite:///trip.db'                             # アプリで使用するDBのURIを定義 
app.config['SQLALCHEMY_DATABASE_URI'] = URI           # アプリがデータベースに接続する際に使用するURIを設定
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 自動的な更新処理も行わないように設定
print('------辞書の中身を出力------')
print(app.config)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# データベースオブジェクトについて
#
# SQLAlchemyオブジェクトは、データベースの操作やクエリの実行など、データベース関連の機能を提供している
# dbという変数にSQLAlchemyオブジェクトを代入することで、アプリ内のどの部分でもdbを使用して
# データベース操作を行うことができるようになる
# dbを介してテーブルの作成、データの追加や更新、クエリの実行などが行える
# 例えば、db.create_all()を呼び出すと、モデルクラスを基にデータベース内にテーブルを作成することができる
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FlaskのインスタンスをセットしてDB変数に格納（Flaskアプリへの関連付けを行う）
db = SQLAlchemy(app)                                  

# -----------------------------
# db.Modelを継承したクラスを作成
# -----------------------------
# データベースとモデルを紐づける（マッピング）
# このクラスをインスタンス化してデータの保存、取得、削除を行う
class Trip(db.Model):
    __tablename__ = 'trip_table'                   # テーブルの作成
    id = db.Column(db.Integer, primary_key=True)   # 登録データのID
    title = db.Column(db.String(30), unique=True)  # タイトル
    content = db.Column(db.String(300))            # 本文
    latitude = db.Column(db.String(100))           # 緯度
    longitude = db.Column(db.String(100))          # 経度
    create_date = db.Column(                       # 登録時間
        db.DateTime,
        nullable=False,
        default=datetime.now()
    )

# ------------------------------------------------
# テーブルとデータベースを初期化するための関数を定義
# ------------------------------------------------
# VSCodeのターミナルから実行する
# 作業ディレクトリ内で、flask initialize_DB　のコマンドを実行する
# パスが通ってない場合は、python -m flask initialize_DB　のコマンドを実行する
@app.cli.command('initialize_DB') # Flaskアプリ内で実行可能なカスタムコマンドを作成
def initialize_DB():              # initialize_DB()は、initialize_DBというコマンドで登録される
    db.create_all()               # Tripクラスの記述を基にデータベース内にテーブルを作成することができる
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
    all_data = Trip.query.all() # データベースから保存されているデータを取得
    print('-------DBから取得したデータ-------')
    print(all_data)
    return render_template('index.html', title=title, all_data=all_data) # titleを渡す

# ------------
# 新規作成画面
# ------------
@app.route('/new')
def new():
    title = 'Trip Log : 新規作成'
    return render_template('new.html', title=title) # titleを渡す

# -----------------------
# データベースへの登録処理
# -----------------------
@app.route('/create', methods=['POST'])
def create():
    title = request.form['title']             # フォームに入力されたname属性を取得して変数に格納
    if title:                                 # titleに値が入力されているか判定
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
        flash('登録できました') # index.htmlに載せる

        # redirect() 引数に指定したページにリダイレクトさせる
        # 特定の関数へのURLを作成
        return redirect(url_for('index'))
    else:
        flash('作成できませんでした。入力内容を確認してください') # index.htmlに載せる
        return redirect(url_for('index'))

# --------
# 詳細画面
# --------
@app.route('/detail') # GETメソッドを使う場合は、引数に['GET']を省略して良い
def detail():
    title = 'Trip Log : 詳細画面'
    id = request.args.get('id')                     # 送られてきたidを取得
    data = Trip.query.get(id)                       # idを引数にして該当するデータをDBから取得（個別に取得する場合はquery.get()を使用）
    map = create_map(data.latitude, data.longitude) # create_map関数に緯度経度を渡して地図を作成
    return render_template('detail.html', title=title, data=data, map=map)


# ===================
# Flaskサーバーの起動
# ===================
if __name__ == '__main__':
    app.run(debug=True)
