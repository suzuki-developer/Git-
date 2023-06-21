from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

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

from flaskr.auth import login_required
from flaskr.db import get_db     # ToDo get_db → connect_db

bp = Blueprint('blog', __name__) # ToDo bp →　blog_bp


@bp.route('/')          # ToDo bp →　blog_bp
def index():
    db    = get_db()    # ToDo get_db → connect_db
    posts = db.execute( # ToDo posts  → userArticles
        'SELECT p.id, title, body, created, author_id, username '
        'FROM post p JOIN user u ON p.author_id = u.id ' # ToDo post → article
        'ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts) # ToDo posts → userArticles


@bp.route('/create', methods=('GET', 'POST')) # ToDo bp →　blog_bp
@login_required
def create(): # create → create_user_article
    if request.method == 'POST':
        title = request.form['title']
        body  = request.form['body']
        error = None

        if not title:
            error = 'Title is required（タイトルは必須です）'

        if error is not None:
            flash(error)
        else:
            db = get_db() # ToDo get_db → connect_db
            db.execute(
                'INSERT INTO post (title, body, author_id) ' # ToDo post → article
                'VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))
    
    return render_template('blog/create.html')


def get_post(id, check_author=True): # ToDo get_post → get_user_article
    post = get_db().execute(         # ToDo post, get_db → userArticle, connect_db
        'SELECT p.id, title, body, created, author_id, username '
        'FROM post p JOIN user u ON p.author_id = u.id ' # ToDo post → article
        'WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None: # ToDo post → userArticle
        abort(404, f"Post id {id} doesn't exist.(投稿IDが存在しません)")

    if check_author and post['author_id'] != g.user['id']: # ToDo post → userArticle
        abort(403)


@bp.route('/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update(id):         # ToDo update → update_user_article
    post = get_post(id) # ToDo post, get_post → userArticle, get_user_article
    
    print('------ postの中身 ------')
    print('post:', post)
    
    if request.method == 'POST':
        title = request.form['title']
        body  = request.form['body']
        error = None

        if not title:
            error = 'Title is required（タイトルは必須です）'
        
        if error is not None:
            flash(error)
        else:
            db = get_db() # ToDo get_db → connect_db
            db.execute(
                'UPDATE post SET title = ?, body = ?' # ToDo post → article
                'WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))
    
    print('------ post内の各値 ------')
    print("post['id']:", post['id'])
    print("post['title']:", post['title'])
    print("post['body']:", post['body'])
    
    return render_template('blog/update.html', post=post) # ToDo post → userArticle


@bp.route('/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def delete(id):   # ToDo delete → delete_user_article
    get_post(id)  # ToDo get_post → get_user_article
    db = get_db() # ToDo get_db → connect_db
    db.execute('DELETE FROM post WHERE id = ?', (id,)) # ToDo post → article
    db.commit()
    return redirect(url_for('blog.index'))
