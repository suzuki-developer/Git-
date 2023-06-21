import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
# from flaskr.db import get_db # ToDo get_db → connect_db

"""
公式ドキュメント通りのディレクトリ構成にしてもモジュールの読み込みに失敗するため下記の通り変更
"""
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
"""
変更箇所ここまで
"""

from flaskr.db import get_db # ToDo get_db → connect_db

bp = Blueprint('auth', __name__, url_prefix='/auth') # ToDo bp → auth_bp


@bp.route('/register', methods=('GET', 'POST')) # ToDo bp → auth_bp
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db       = get_db() # ToDo get_db → connect_db
        error    = None

        if not username:
            error = 'Uername is required.（ユーザー名は必須です）'
        elif not password:
            error = 'Password is required.（パスワードは必須です）'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered（ユーザー名は登録済みです）"
            else:
                return redirect(url_for("auth.login"))
            
        flash(error)

    return render_template('auth/register.html')
    

@bp.route('/login', methods=('GET', 'POST')) # ToDo bp → auth_bp
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db       = get_db()                  # ToDo get_db → connect_db
        error    = None
        user     = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username（ユーザー名が正しくありません）'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password（パスワードが正しくありません）'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        
        flash(error)

    return render_template('auth/login.html')


@bp.route('/logout') # ToDo bp → auth_bp
def logout():
    session.clear()
    return redirect(url_for('index'))


@bp.before_app_request # ToDo bp → auth_bp
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute( # ToDo get_db → connect_db
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        
        return view(**kwargs)
    
    return wrapped_view
