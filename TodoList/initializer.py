from os import environ
from flask import Flask, request, jsonify

# Configure the application's environment.
DEV_ENV = 'DEVELOPMENT'
APP_ENV = DEV_ENV if environ.get('APP_ENV') is None else environ.get('APP_ENV')

# Initialize the Flask application.
app = Flask(__name__)
