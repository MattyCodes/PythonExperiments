from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from initializer import app
import os

# The name of the database-file.
DB_FILENAME = 'db.sqlite'

# Derive the base directory of the project.
basedir = os.path.abspath(os.path.dirname(__file__))

# Configure the database.
app.config['SQLALCHEMY_DATABASE_URI']        = f'sqlite:///{os.path.join(basedir, DB_FILENAME)}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database.
db = SQLAlchemy(app)

# Initialize Marshmallow.
ma = Marshmallow(app)
