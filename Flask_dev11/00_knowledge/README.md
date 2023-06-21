## 各種要件など
- 要件
    - ディレクトリ構成を意識したWebアプリ
    - 機能
        - ログイン画面
        - CRUD処理 
            - sqllite3を使用
            - SQLALCHEMYを使用

- 使用言語
    - python

- 実行環境
    - ローカル

- 参考
    - ゼロからFlaskがよくわかる本: Pythonで作るWebアプリケーション開発入門(Amazonアンリミテッド)

## 用意するもの
- 

## 作業メモ
- ディレクトリ構成
- C:\Users\suzuki-s\Desktop\Git修正後用\Flask_dev11

### pipenv
- インストール時のメッセージ
    ```
    Installing collected packages: distlib, virtualenv-clone, setuptools, platformdirs, filelock, virtualenv, pipenv
    WARNING: The script virtualenv-clone.exe is installed in 'C:\Users\suzuki-s\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts' which is not on PATH.
    Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
    WARNING: The script virtualenv.exe is installed in 'C:\Users\suzuki-s\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts' which is not on PATH.
    Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
    WARNING: The scripts pipenv-resolver.exe and pipenv.exe are installed in 'C:\Users\suzuki-s\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts' which is not on PATH.
    Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
    Successfully installed distlib-0.3.6 filelock-3.12.0 pipenv-2023.6.2 platformdirs-3.5.1 setuptools-67.8.0 virtualenv-20.23.0 virtualenv-clone-0.5.7

    [notice] A new release of pip is available: 23.0.1 -> 23.1.2
    [notice] To update, run: C:\Users\suzuki-s\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip
    ```

- 仮想環境を作成するディレクトリに移動する

- 仮想環境の作成
    - pipenv --python 3.11.4

- 仮想環境に入る
    - pipenv shell 

- ライブラリのインストール
    - pipenv install "Flask==2.3.2"

## 備考
- 中止