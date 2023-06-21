# =====================
# ライブラリのインポート
# =====================
from flask import Flask, render_template, request, flash, redirect, url_for, Blueprint
import os                                 # 暗号鍵生成で使用
from flask_sqlalchemy import SQLAlchemy   # ORMを使う為
from datetime import datetime             # DBで日付を扱うのに必要
from create_map import create_map
from app import app, db, Trip

# ---------
# app.py用
# ---------
index_bp = Blueprint('index', __name__)
new_bp = Blueprint('new', __name__)
detail_bp = Blueprint('detail', __name__)
edit_bp = Blueprint('edit', __name__)

# --------
# 一覧画面
# --------
@index_bp.route('/')
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
@new_bp.route('/new')
def new():

    title = 'Trip Log : 新規作成'
    return render_template('new.html', title=title) 

# --------
# 詳細画面
# --------
@detail_bp.route('/detail') 
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
@edit_bp.route('/edit/<int:id>', methods=['GET'])
def edit(id):
    title = 'Trip Log : 編集画面'
    data = Trip.query.get(id)
    return render_template('edit.html', title=title, data=data)