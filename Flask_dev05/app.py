# ===========================
# 必要なライブラリのインポート
# ===========================
from flask import Flask, render_template, session, request, redirect, url_for
import os                               # 暗号鍵作成で使用
from pref_question import pref_location # 県庁所在地当てクイズに関するファイル
from wiki import wiki


# ==================
# インスタンスの作成
# ==================
app = Flask(__name__)


# ============
# 暗号鍵の生成
# ============
# Flaskではsessionを使う際、session情報を暗号化する為のsession_keyの設定が必要
key = os.urandom(21) # 21桁の乱数を作成
app.secret_key = key


# ============================================
# ログインするためのユーザーIDとパスワードを作成
# ============================================
id_pwd = {'suzuki': '12345'}


# ============
# ルーティング
# ============

# ------
# メイン
# ------
@app.route('/')
def index():
    if not session.get('login'):             # loginセッションがないかどうか判定
        return redirect(url_for('login'))    # def loginが走る
    else:
        return render_template('index.html') # index.htmlを表示させる

# --------
# ログイン
# --------
@app.route('/login')
def login():
    return render_template('login.html')

# ----------------------------
# ログイン認証（セッション管理）
# ----------------------------
@app.route('/logincheck', methods=['POST'])
def logincheck():
    # フォームで入力されたユーザーIDとパスワードを変数に格納
    user_id = request.form['user_id']
    password = request.form['password']

    # ユーザーIDとパスワードをチェック
    if user_id in id_pwd:                 # user_idがid_pwdという辞書のキーとして存在するかをチェック
        if password == id_pwd[user_id]: # 入力されたパスワードが、id_pwdという辞書の中で対応するユーザーIDのパスワードと一致するかどうかをチェック
            session['login'] = True       # session['login']にTrueをセット
        else:
            session['login'] = False      # session['login']にFalseをセット
    else:                                 # 力されたユーザーIDが登録されていない場合
        session['login'] = False

    # リダイレクト
    # redirect関数 引数に与えられたページに転送する
    # url_for関数  引数に与えられた関数を実行する
    if session['login']:                  # TrueかFalseであるか判定
        return redirect(url_for('index')) # Trueの場合  def indexが走る
    else:
        return redirect(url_for('login')) # Falseの場合 def loginが走る
    
# ----------
# ログアウト
# ----------
@app.route('/logout')
def logout():
    session.pop('login', None)        # セッションを削除
    return redirect(url_for('index')) # def indexが走る

# --------------------
# 県庁所在地当てクイズ
# --------------------
@app.route("/pref_quiz", methods=['POST'])
def pref_quiz():
    # # pref_location()の戻り値を変数に代入
    # random_pref, city_name, pref_url = pref_location()

    # pref_location()の戻り値を取得
    result = pref_location()
    print("-----pref_location()の戻り値------")
    print(result)

    # 戻り値を変数に代入
    random_pref = result[0]
    city_name = result[1]
    pref_url = result[2]
    print("------戻り値を変数に代入------")
    print(random_pref)
    print(city_name)
    print(pref_url)

    # セッション変数に戻り値を保存
    session['prefecture'] = random_pref
    session['city'] = city_name
    session['URL'] = pref_url
    print("------セッション変数-------")
    print(session['prefecture'])
    print(session['city'])
    print(session['URL'])

    # quiz.htmlへ遷移
    # random_prefをprefectureという変数に格納して、quiz.htmlに渡す
    return render_template('quiz.html', prefecture=random_pref)



# -------------------------------
# クイズの答えが送信された際の処理
# -------------------------------
@app.route('/answercheck', methods=['POST'])
def answercheck():
    # フォームで入力されたcity属性を取得
    user_answer = request.form['city']

    # セッション変数から都道府県、都市名、URLを取得
    prefecture = session.get('prefecture')
    city = session.get('city')
    url = session.get('URL')
    print(prefecture)
    print(city)
    print(url)

    if user_answer == city:
        result = '正解'
    else:
        result = '残念'

    # result, prefecture, city, urlを、result.htmlに渡す
    return render_template('result.html', result=result, prefecture=prefecture, city=city, url=url)


# -------------------
# wikipediaで調べもの
# -------------------
@app.route('/wikipedia', methods=['POST'])
def wikipedia():
    # この時点ではユーザーから検索ワードを受け取っておらず、返す結果がないため第二引数は空の文字列
    return render_template('wiki_result.html', result='初めてのアクセスです！')
    # # 以下でも可
    # return render_template('wiki_result.html')

# -------------------
# wikipediaの検索結果
# -------------------
@app.route('/wiki_answer', methods=['POST'])
def wiki_answer():
    word = request.form['word'] # ユーザー入力値の取得
    if word == '':              # 入力値が空欄の場合の処理
        result = '入力がないため、該当する結果がありませんでした。'
    else:
        result = wiki(word)     # wiki()の引数にワード指定して結果結果の概要を取得

    return render_template('wiki_result.html', result=result) # 取得した検索結果の概要を渡す


# =====================
# アプリケーションの起動
# =====================
if __name__ == '__main__':
    app.run(debug=True)