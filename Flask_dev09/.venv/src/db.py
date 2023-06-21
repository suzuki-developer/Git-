from src import app
from src import db
from src import ma
from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, desc

# DBの作成
class Order(db.Model):
    __tablename__ = 'Order'
    id      = db.Column(Integer, primary_key=True)
    product = db.Column(String(32))
    date    = db.Column(String(8))
    amount  = db.Column(Integer)

# APIに初めてリクエストが送信されたときにだけデータベースを作成
# @app.before_first_request
@app._got_first_request
def init():
    db.create_all()


class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
order_schema = OrderSchema(many=True)


# GET(全件参照)
@app.route('/order', methods=['GET'])
def getAll():
    data = Order.query.all()
    return jsonify(order_schema.dump(data))


