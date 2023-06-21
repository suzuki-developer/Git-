from flask import Flask

from app.apis import hello, articles

app = Flask(__name__)
app.register_blueprint(hello.api)
app.register_blueprint(articles.api)

