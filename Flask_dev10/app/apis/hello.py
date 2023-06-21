from flask import Blueprint, jsonify, request

api = Blueprint('hello', __name__, url_prefix='/api/hello')

@api.route('')
def get():
    name = request.args.get('name', 'world')
    return jsonify({'message': 'Hello ' + name + '!'}), 200
