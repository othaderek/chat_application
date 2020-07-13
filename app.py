from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import pdb

# Init App
app = Flask(__name__)
# Init SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# Databse Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/chat_app_api'

class UsersModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(13))

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"<User {self.name}>"

# get users
@app.route('/users', methods=["GET"])
def get_users():
    if request.method == 'GET':
        users = UsersModel.query.all()
        results = [
            {
                'name': user.name
            }for user in users]
    return jsonify(results)
        