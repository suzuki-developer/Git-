## 各種要件など
- 要件
    - Flaskのフォルダ構成の基本を覚える

- 使用言語
    - Python
        - Flaskを使用

- 実行環境
    - ローカル

- 参考
    - [Flask] Flaskの基本的な構成（を思い出す）
    - https://t-kojima.github.io/2018/06/25/0019-flask-tutorial-create-app/


## 作業メモ
- ディレクトリ構成
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── app
│   ├── __init__.py
│   ├── controllers
│   │   ├── __init__.py
│   │   └── auth_controller.py
│   ├── forms
│   │   ├── __init__.py
│   │   └── auth_form.py
│   ├── models
│   │   ├── __init__.py
│   │   └── auth.py
│   ├── static
│   └── templates
│       ├── 404.html
│       └── auth
│           └── signin.html
├── config.py
└── run.

## 備考
- signin.htmlの書き方が分からず挫折した