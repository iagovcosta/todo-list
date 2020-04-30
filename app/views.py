from flask import Blueprint

todos = Blueprint("todos", __name__, url_prefix="/v1/todos")

@todos.route("/")
def gettodos():
    return ""