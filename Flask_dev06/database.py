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
create_bp = Blueprint('create', __name__)
update_bp = Blueprint('update', __name__)
delete_bp = Blueprint('delete', __name__)


# --------------
# DBへの登録処理
# --------------
@create_bp.route('/create', methods=['POST'])
def create_():
    # 
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


@update_bp.route('/update', methods=['POST'])
def update():
    id = request.form['id']
    edit_data = Trip.query.get(id)

    edit_data.title = request.form['title']
    edit_data.content = request.form['content']
    edit_data.latitude = request.form['latitude']
    edit_data.longitude = request.form['longitude']

    db.session.merge(edit_data)
    db.session.commit()
    flash('更新しました')
    return redirect(url_for('index')) 

@delete_bp.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    delete_data = Trip.query.get(id)
    db.session.delete(delete_data)
    db.session.commit()
    flash('削除しました')
    return redirect(url_for('index'))