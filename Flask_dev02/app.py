# ライブラリのインストール
from flask import Flask

# インスタンスの初期化
app = Flask(__name__)

@app.route("/")
def test():
    return "It Works!!"

# Webサーバーの起動
if __name__ == "__main__":
    app.run(debug=True)