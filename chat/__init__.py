from flask import Flask

def create_app():
    from . import models, controllers
    app = Flask(__name__)
    models.init_app(app)
    controllers.init_app(app)
    return app