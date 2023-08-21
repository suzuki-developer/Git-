# パッケージの利用で複数のソースコードをコンパイルし、実行する方法

## 参考サイト
- Java：「メインクラスを検出およびロードできませんでした」の解決法
- https://qiita.com/inahu_ono/items/ddd6985eb02ca694c58c

## 目的
- 複数クラスのjavaプログラムを実行する
- 下記エラーの解決
    ```
    エラー: メイン・クラスChapter_06.Calcを検出およびロードできませんでした
    原因: java.lang.ClassNotFoundException: Chapter_06.Calc
    ```

## 結論
- Javaのファイルが存在する一つ上のディレクトリから、コマンドを実行する
- 使用したコマンド
    - `java <実行するjavaファイルの存在するディレクトリ>.<mainメソッドが含まれるクラス名>`
        ```
        PS C:\Users\shota suzuki\Desktop\スッキリわかるJava入門\Sample2> cd "C:\Users\shota suzuki\Desktop\スッキリわかるJava入門"
        PS C:\Users\shota suzuki\Desktop\スッキリわかるJava入門> java Sample2.Sample2                                     
        山田は生徒です
        ```
- ディレクトリ構成
    ```
    │  ├─スッキリわかるJava入門
    │  │  ├─Sample2
    │  │  │      readme.md
    │  │  │      Sample2.class
    │  │  │      Sample2.java
    │  │  │      Student.class
    │  │  │      Student.java
    ```