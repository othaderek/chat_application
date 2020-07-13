from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import models
import controllers
import pdb

# Init App
app = Flask(__name__)
# Init SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# Databse Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/chat_app_api'


if __name__ == "__main__":
    app.run()