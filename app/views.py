from flask import Blueprint, jsonify
from . import schema
from . import mongo

todos = Blueprint("todos", __name__, url_prefix="/v1/todos")

@todos.route("/")
def gettodos():
    schemas = schema.TodoSchema(many=True)
    todos_List = mongo.db.todos.find()
    return jsonify(schemas.dump(todos_List))