from flask import request, jsonify
from models import *
from initializer import app

# Initialize the schemas.
TODO_ITEM_SCHEMA  = TodoItemSchema()
TODO_ITEMS_SCHEMA = TodoItemSchema(many=True)

# Create a todo-item.
@app.route('/todo-item', methods=['POST'])
def create_todo_item():
    new_todo_item = TodoItem(request.json['description'])

    db.session.add(new_todo_item)
    db.session.commit()

    return TODO_ITEM_SCHEMA.jsonify(new_todo_item)

# Get all of the todo-items.
@app.route('/todo-items', methods=['GET'])
def read_todo_items():
    all_todo_items = TodoItem.query.all()
    formatted_list = TODO_ITEMS_SCHEMA.dump(all_todo_items)

    return jsonify(formatted_list)