from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import pdb

# Init App
app = Flask(__name__)
# Init SQLAlchemy
db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def index():
    return {"msg": "hello"}

# Databse Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/chat_app_api'
db.

pdb.set_trace()