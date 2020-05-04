from flask import Blueprint, jsonify, request
from bson import ObjectId
from . import schema
from . import mongo

todos = Blueprint("todos", __name__, url_prefix="/v1/todos")

@todos.route("/")
def gettodos():
    schemas = schema.TodoSchema(many=True)
    todos_List = mongo.db.todos.find()
    return jsonify(schemas.dump(todos_List))

@todos.route("/insert", methods=["POST"])
def addTodos():
    data = request.get_json()
    mongo.db.todos.insert_one(data)
    schemas = schema.TodoSchema()
    return jsonify(schemas.dump(data))

@todos.route("/close/<_id>", methods=["PUT"])
def closetodos(_id):
    todo = mongo.db.todos.update_one({"_id": ObjectId(_id)},
        {"$set": {"status": False}})
    return jsonify({"modified": todo.modified_count})