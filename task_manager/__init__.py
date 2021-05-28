import os
from flask import Flask
from .main.routes import main
from .extensions import mongo
if os.path.exists("env.py"):
    import env

def create_app():
    app = Flask(__name__)

    app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
    app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
    app.secret_key = os.environ.get("SECRET_KEY")

    mongo.init_app(app)

    app.register_blueprint(main)

    return app