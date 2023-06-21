## 各種要件など
- 要件
    - Flask Blueprint の使い方を知る

- 使用言語
    - Python

- 実行環境
    - ローカル

- 参考
    - Flask Blueprint の使い方
    - https://hogetech.info/programming/python/flask/blueprint


## 作業メモ
### Blueprint とは
- Flask における Blueprint とは、アプリケーションの機能を複数のファイル (モジュール) に分割する方法
- ソースコードが長すぎる場合に、機能ごとにファイルを分割し管理しやすくするために利用

- 使い方
    - Blueprintの作成
        ```
        # Blueprintを作成
        hello = Blueprint('hello', __name__) # 引数1は一意である必要がある
        hoge  = Blueprint('hoge', __name__)

        # デコレータの名前はBlueprintの変数名と同じにして関連づける
        @hello.route('/')
        def SayHello():
            return 'Hello world'

        @hoge.route('/hoge')
        def SayHoge():
            return 'hoge'

        ```

    - 起動ファイルへの登録
        ```
        # appにあるbp変数をインポート
        from app2 import hello # blueprintの名前を入れる
        from app2 import hoge  

        app = Flask(__name__)

        # インポートしたbp変数(Blueprintオブジェクト)を登録
        app.register_blueprint(hello)
        app.register_blueprint(hoge)

        ```