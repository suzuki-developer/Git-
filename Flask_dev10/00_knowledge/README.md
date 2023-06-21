## 各種要件など
- 要件
    - Web APIの作成
        - HTTPリクエストを受け取ったらデータをJSONで返す簡易的なシステム
        - 受け取るリクエスト
            - GET /api/hello
            - GET /api/articles
            - GET /api/articles/<id>
            - POST /api/articles

- 使用言語
    - Python

- 実行環境
    - ローカル

- 参考
    - 【Python入門】PythonでWeb APIをサクッと作成してみる
    - https://www.true-fly.com/entry/2022/08/01/080000


## 作業メモ
- ディレクトリ構成
- C:\Users\suzuki-s\Desktop\Git修正後用\Flask_dev10
    .
    ├── app
    │   ├── apis
    │   │   ├── articles.py  ... /api/articles へのリクエストを受け付けるメソッドを定義
    │   │   └── hello.py     ... /api/hello    へのリクエストを受け付けるメソッドを定義
    │   │     
    │   ├── models
    │   │   └── articles.py  ... リクエストを処理
    │   │     
    │   └── server.py        ... Flaskアプリケーションを定義
    │      
    ├── request.py　　　　　　... Web APIにリクエストを送るファイル
    │ 
    └── run.py               ... 起動ファイル



### app/apis/hello.py
- /api/helloへのリクエストを受け付けるメソッドを定義
- api = Blueprint()でAPIを定義（これをapp/server.py で読込している）
- get()のデコレータ@api.route('')でリクエストを受け取る処理を記述
- `name = request.args.get('name', 'world')`について
    - request.args.get()
        - `第1引数がパラメータ名、第2引数がパラメータを指定されなかったときのデフォルト値`
        - requestからクエリパラメータの値を取得するためのメソッド
        - requestは、Flaskアプリケーションが受け取ったHTTPリクエストに関する情報を格納している
        - request.argsから指定したキー（この場合は'name'）に対応する値を取得する
        - 指定したキーが存在しない場合、デフォルトの値として提供された2番目の引数（この場合は'world'）が返される

    - request.args
        - リクエストのクエリパラメータを表す辞書オブジェクト
        - 例
            - URLが/api/hello?name=John&age=25のようになっている場合、
            - request.argsには{'name': 'John', 'age': '25'}という辞書が格納される


### app/api/articles.py
- 以下のリクエストを処理
    - GET  /api/articles
        - GET でアクセスされたらリクエストを受け付ける
    
    - GET  /api/articles/<id>
        - GET でアクセスされたらリクエストを受け付ける
        - 引数でIDを受け取り、IDに対応するデータを返す

    - POST /api/articles
        - POSTでアクセスされたらリクエストを受け付ける

- `request.form[フィールド名]`について
    - POSTメソッドによって送信されたフォームデータの中のフィールドの値を取得するための方法
    - request.form
        - リクエストがPOSTメソッドで送信された場合に、そのリクエストに含まれるフォームデータを表す辞書オブジェクト
        - ユーザーがフォームを送信すると、request.formには{'title': '入力された値'}のような辞書が格納される
    - 例
        - request.form['title']は、この辞書からキーが'title'に対応する値を取得する


### app/api/models/articles.py
- 記事のデータを扱うファイル
- get(id: int = None)
    - idが
        - 指定されていれば指定のデータを返す
        - 指定されていなければ全データを返す
        - 存在しなければ空の辞書を返す
            - for文内の処理が全て終わった後に判定する

- post(title:str, link:str)
    - 値を受け取ったら標準出力して、辞書の形でデータを返す

- def get(id: int = None):
    - id が整数型であることを意味している
    - 引数が省略された場合はNoneが代入される


### request.py
- ファイルが直接実行された場合にのみ、if __name__ == '__main__':のブロック内のコードが実行される