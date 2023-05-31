# 必要なライブラリのインポート
from flask import Flask, render_template, session, request, redirect, url_for
import os

# インスタンスの作成
app = Flask(__name__)

# メイン
@app.route('/')
def index():
    return 'Hello demon Slayer'

@app.route('/kaminari')
def kaminari():
    return '雷'

# アプリケーションの起動
if __name__ == '__main__':
    app.run(debug=True)
