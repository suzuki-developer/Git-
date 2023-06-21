# =====================
# ライブラリのインポート
# =====================
from flask import Flask, render_template, request, flash, redirect, url_for, Blueprint
import os                                 # 暗号鍵生成で使用
from flask_sqlalchemy import SQLAlchemy   # ORMを使う為
from datetime import datetime             # DBで日付を扱うのに必要
from create_map import create_map
from app import app


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