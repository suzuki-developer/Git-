## 各種要件など
- 要件
    - ディレクトリ構成を意識したwebアプリ

- 使用言語
    - Python

- 実行環境
    - ローカル

- 参考
    - 【Python】Flask + MySQL + SQLAlchemyでAPIを開発してみよう Part1
    - https://swallow-incubate.com/archives/blog/20190819


## 作業メモ
### ディレクトリ構成
    app.py ... 起動ファイル
    |
    config.py 　　　　　　　　　　... DBの接続情報、外部から読み込み可能
    |
    api
    ├── __init__.py 　　　　　　　... FlaskApp本体、DBとの連携
    │
    ├── database.py 　　　　　　　... アプリでDB操作を行えるように初期設定する
    │
    ├── models 　　　　　　　　　　... Model群
    │   └── user.py　　　　　　　 ... DB構造、DB操作(一覧情報の取得、登録)
    │   └── __init__.py
    │
    └── views  　　　　　　　　　　... Controller群
        └── user.py               ... ルーティング


### app.pyに関して
- 起動するだけのファイル
- モジュールのインポートについて
    ```
    from api import app
    ```
    - 「api」というパッケージから「app」という名前のモジュールをインポートする
        1. 「api」パッケージ内の「init.py」ファイルに含まれるFlaskアプリケーションオブジェクト（通常は「app」と呼ばれる）をインポートします。
        2. 「app.py」ファイル内で、Flaskアプリケーションを起動するために使用される


### __init.py__について
- ディレクトリについて
    ```
    from .views.user import user_router
    ```
    - .viewsの先頭の`.`は、現在の階層を示す（パスでいう`./`）
    - 分かりやすくパスで書き換えると、`/views/user`のようになる


- url_prefixについて
    ```
    app.register_blueprint(user_router, url_prefix='/api')
    ```
    - url_prefixをつけることで、Blueprintの登録先のURLに対して接頭辞（プレフィックス）を追加する
        ```
        @user_router.route('/users', methods=['GET'])
        ```
        - 上記の場合であれば、/api/usersのようになる
        - Blueprintとurl_prefixを組み合わせることで、アプリケーション内でのURLの階層構造を整理し、異なる機能やエンドポイントをグループ化することができる


### user.pyについて
- '/api/users'にアクセスした場合にJSON形式でデータを返すためのエンドポイントを定義している
- make_response():
    - レスポンスオブジェクトを作成するために使用される
    - 通常、レスポンスを返す際に使用される
    - この関数は、引数として渡されたデータを含むレスポンスオブジェクトを作成する

- jsonify():
    - PythonオブジェクトをJSON形式に変換するために使用される
    - 通常、JSONレスポンスを返す際に使用される
    - 引数として渡されたPythonオブジェクトをJSON形式に変換し、適切なHTTPヘッダーを設定してレスポンスオブジェクトを作成

## 備考
- 挫折した
- class UserSchema(ma.ModelSchema)の書き方に問題がある？
　```
        C:\Users\suzuki-s\Desktop\Git修正後用\Flask_dev08>python app.py
    Traceback (most recent call last):
    File "C:\Users\suzuki-s\Desktop\Git修正後用\Flask_dev08\app.py", line 1, in <module>
        from api import app
    File "C:\Users\suzuki-s\Desktop\Git修正後用\Flask_dev08\api\__init__.py", line 2, in <module>
        from .views.user import user_router
    File "C:\Users\suzuki-s\Desktop\Git修正後用\Flask_dev08\api\views\user.py", line 2, in <module>
        from api.models import User, UserSchema
    File "C:\Users\suzuki-s\Desktop\Git修正後用\Flask_dev08\api\models\__init__.py", line 1, in <module>
        from .user import User, UserSchema
    File "C:\Users\suzuki-s\Desktop\Git修正後用\Flask_dev08\api\models\user.py", line 39, in <module>
        class UserSchema(ma.ModelSchema):
                        ^^^^^^^^^^^^^^
    AttributeError: 'Marshmallow' object has no attribute 'ModelSchema'
```