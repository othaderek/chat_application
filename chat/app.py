from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from controllers import main
import pdb

def create_app():
    # Init App
    app = Flask(__name__)
    # Init SQLAlchemy
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    # Databse Config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/chat_app_api'
    app.register_blueprint(main)
    return app