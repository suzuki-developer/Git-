## 各種要件など
- 要件
    - ディレクトリ構成を意識したwebアプリ
    - REST API

- 使用言語
    - Python

- 実行環境
    - ローカル環境
    - venv（仮想環境使用）

- 参考
    - Pythonフレームワーク「Flask」でWeb APIを作成する
    - https://devlog.grapecity.co.jp/python-flask-web-api/#rest-api


## 作業メモ
- ディレクトリ構成
  └─src
        app.py       ... Pythonの起動
        db.py        ... DBに対するCRUD処理
        __init__.py  ... Python実行時の初期設定（今回はDBに対する接続設定）

## 備考
- 挫折した
- 下記エラーメッセージに表示されている通り、`@app._got_first_request`に変更したが動かなかった
    ```
    (.venv) C:\Users\suzuki-s\Desktop\Git修正後用\Flask_dev09>flask run
    Traceback (most recent call last):
    File "<frozen runpy>", line 198, in _run_module_as_main
    File "<frozen runpy>", line 88, in _run_code
    File "C:\Users\suzuki-s\Desktop\Git修正後用\Flask_dev09\.venv\Scripts\flask.exe\__main__.py", line 7, in <module>
    File "C:\Users\suzuki-s\Desktop\Git修正後用\Flask_dev09\.venv\Lib\site-packages\flask\cli.py", line 1063, in main
        cli.main()
    File "C:\Users\suzuki-s\Desktop\Git修正後用\Flask_dev09\.venv\Lib\site-packages\click\core.py", line 1055, in main
        rv = self.invoke(ctx)
            ^^^^^^^^^^^^^^^^
    File "C:\Users\suzuki-s\Desktop\Git修正後用\Flask_dev09\.venv\Lib\site-packages\click\core.py", line 1657, in invoke
        return _process_result(sub_ctx.command.invoke(sub_ctx))
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "C:\Users\suzuki-s\Desktop\Git修正後用\Flask_dev09\.venv\Lib\site-packages\click\core.py", line 1404, in invoke
        return ctx.invoke(self.callback, **ctx.params)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "C:\Users\suzuki-s\Desktop\Git修正後用\Flask_dev09\.venv\Lib\site-packages\click\core.py", line 760, in invoke
        return __callback(*args, **kwargs)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "C:\Users\suzuki-s\Desktop\Git修正後用\Flask_dev09\.venv\Lib\site-packages\click\decorators.py", line 84, in new_func
        return ctx.invoke(f, obj, *args, **kwargs)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "C:\Users\suzuki-s\Desktop\Git修正後用\Flask_dev09\.venv\Lib\site-packages\click\core.py", line 760, in invoke
        return __callback(*args, **kwargs)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "C:\Users\suzuki-s\Desktop\Git修正後用\Flask_dev09\.venv\Lib\site-packages\flask\cli.py", line 911, in run_command
        raise e from None
    File "C:\Users\suzuki-s\Desktop\Git修正後用\Flask_dev09\.venv\Lib\site-packages\flask\cli.py", line 897, in run_command
        app = info.load_app()
            ^^^^^^^^^^^^^^^
    File "C:\Users\suzuki-s\Desktop\Git修正後用\Flask_dev09\.venv\Lib\site-packages\flask\cli.py", line 312, in load_app
        app = locate_app(import_name, None, raise_if_not_found=False)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "C:\Users\suzuki-s\Desktop\Git修正後用\Flask_dev09\.venv\Lib\site-packages\flask\cli.py", line 218, in locate_app
        __import__(module_name)
    File "C:\Users\suzuki-s\Desktop\Git修正後用\Flask_dev09\.venv\app.py", line 4, in <module>
        from src import app
    File "C:\Users\suzuki-s\Desktop\Git修正後用\Flask_dev09\.venv\src\__init__.py", line 14, in <module>
        import src.db
    File "C:\Users\suzuki-s\Desktop\Git修正後用\Flask_dev09\.venv\src\db.py", line 17, in <module>
        @app.before_first_request
        ^^^^^^^^^^^^^^^^^^^^^^^^
    AttributeError: 'Flask' object has no attribute 'before_first_request'. Did you mean: '_got_first_request'?
    ```

