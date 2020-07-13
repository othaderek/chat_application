from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import pdb

# Init App
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

pdb.set_trace()