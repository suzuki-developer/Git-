## 各種要件など
- 要件
    - 基本的なブログアプリケーション
        - ユーザー登録
        - ログイン
        - 投稿記事の作成、編集、削除

- 使用言語
    - Python

- 実行環境
    - ローカル

- 参考
    - 公式ドキュメント
    - https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/tutorial/layout.html


## 作業メモ
### ディレクトリ構成
```
C:\Users\suzuki-s\Desktop\Git修正後用\Flask_dev12
│ 
├── flaskr/                      ... アプリケーションのコードとファイルを含んだPythonのpackage
│   ├── __init__.py              ... Pythonへflaskrディレクトリをpackageとして扱うように伝える
│   ├── db.py                    ... データベースの操作に関する処理を記述
│   ├── schema.sql               ... DBのテーブル作成
│   ├── auth.py                  ... ログインなど認証に関わるBlueprintなどを定義
│   ├── blog.py                  ... ブログの画面や操作にかかわるBlueprintなどを定義
│   ├── templates/               ... テンプレート関連のファイル群
│   │   ├── base.html            ... 他のHTMLファイルの骨組みになるファイル
│   │   │ 
│   │   ├── auth/                ... 認証関係のファイル群
│   │   │   ├── login.html       ... ログイン画面
│   │   │   └── register.html    ... 登録画面
│   │   │ 
│   │   └── blog/                ... ブログ関係のファイル群
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   │ 
│   └── static/
│       └── style.css
│  
├── tests/                       ... テスト用moduleを含んだディレクトリ
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
│  
├── venv/                        ... Flaskとその他の依存対象がインストールされたPythonの仮想環境
│
├── setup.py
└── MANIFEST.in
```


### 仮想環境（Virtual environments）
- 参考
    - 公式ドキュメント
    - https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/installation.html

- 手順
    - プロジェクトのフォルダを作成
        - 今回なら「flask-tutorial」
    - 作成したプロジェクトのフォルダに移動
        - cd C:\Users\suzuki-s\Desktop\Git修正後用\Flask_dev12\flask-tutorial\venv
    - 仮想環境を構築
        - python -m venv venv
    - 仮想環境を有効化
        - venv\Scripts\activate
    - 仮想環境の中でFlaskをインストール
        - pip install Flask
    - アプリケーションの実行
        - flask --app flaskr --debug run


### application factory


### __init__.py
- Pythonへflaskrディレクトリをpackageとして扱うように伝えるファイル
- `app = Flask(__name__, instance_relative_config=True)`
    - instance_relative_config=True
        - 設定ファイル（の場所）がインスタンスフォルダから相対的に示されることを、appへ伝える
        - インスタンスフォルダはflaskrパッケージの外側に位置し、秘密情報の設定やデータベースのファイルなど、バージョン管理へコミットするべきではないローカルのデータを保持することができる

- `app.config.from_pyfile()`
    - もしインスタンスフォルダにconfig.pyファイルがあれば、値をそこから取り出して、標準設定を上書きする

- `app.config.from_mapping()`
    - appが使用する標準設定をいくつか設定
        - SECRET_KEY
            - データを安全に保つためにFlaskとFlask拡張によって使用される
        - DATABASE
            - SQLiteデータベースファイルが保存されるパス
            - app.instance_pathの下に設定


### db.py
- `g`
    - 特別なオブジェクトで、リクエストごとに個別なものになる
    - リクエストの（処理）期間中は複数の関数によってアクセスされるようなデータを格納するために使われる
    - connectionは（gオブジェクトに）格納されて、もしも同じリクエストの中でget_dbが2回呼び出された場合、新しいconnectionを作成する代わりに、再利用される

- `current_app`
    - 特別なオブジェクトで、リクエストを処理中のFlaskアプリケーションを指し示す
    - 現在のリクエストを処理するアプリケーションへのプロキシ

- `sqlite3.connect()`
    - キーDATABASEで示されるファイルへのconnectionを確立する
    - このファイルはまだ存在せず、後程データベースを初期化するまで存在しない

- `sqlite3.Row`
    - dictのように振る舞う行を返すようにconnectionへ伝える
    - 列名による列へのアクセスを可能にする

- `close_db`
    - g.dbが設定されているか調べることでconnectionが作成済みであるかを調べる
    - もしconnectionが存在した場合は、それを閉じる

- `click.command()`
    - init_db関数を呼び出して成功時のメッセージを表示する、init-dbと呼ばれる、コマンドラインから使用できるコマンドを定義

- `app.teardown_appcontext()`
    - レスポンスを返した後のクリーンアップを行っているときに、上記の関数（close_db）を呼び出すように、Flaskへ伝える

- `app.cli.add_command()`
    - flaskコマンドを使って呼び出すことができる新しいコマンドを追加する
