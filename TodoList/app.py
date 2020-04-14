from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from os import environ
import os
import pdb

# Configure the application's environment.
DEV_ENV     = 'DEVELOPMENT'
APP_ENV     = DEV_ENV if environ.get('APP_ENV') is None else environ.get('APP_ENV')
DB_FILENAME = 'db.sqlite'

# Initialize the Flask application.
app = Flask(__name__)

# Derive the base directory of the project.
basedir = os.path.abspath(os.path.dirname(__file__))

# Configure the database.
app.config['SQLALCHEMY_DATABASE_URI']        = f'sqlite:///{os.path.join(basedir, DB_FILENAME)}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database.
db = SQLAlchemy(app)

# Initialize Marshmallow.
ma = Marshmallow(app)

# Todo-item model-class.
class TodoItem(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200))

    def __init__(self, description):
        self.description = description

# Todo-item schema.
class TodoItemSchema(ma.Schema):
    class Meta:
        fields = ('id', 'description')

# Initialize the schemas.
todo_item_schema  = TodoItemSchema()
todo_items_schema = TodoItemSchema(many=True)

# Create a todo-item.
@app.route('/todo-item', methods=['POST'])
def create_todo_item():
    new_todo_item = TodoItem(request.json['description'])

    db.session.add(new_todo_item)
    db.session.commit()

    return todo_item_schema.jsonify(new_todo_item)

# Get all of the todo-items.
@app.route('/todo-items', methods=['GET'])
def read_todo_items():
    all_todo_items = TodoItem.query.all()
    formatted_list = todo_items_schema.dump(all_todo_items)

    return jsonify(formatted_list)

# Run the server.
if __name__ == '__main__':
    app.run(debug = APP_ENV is DEV_ENV)

