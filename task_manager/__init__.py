from flask import Flask
from .main.routes import main
from .extensions import mongo

def create_app():
    app = Flask(__name__)

    app.config['MONGO_URI'] = 'mongodb+srv://oxymichael2:<password>@cluster0.xlavz.mongodb.net/task_manager?retryWrites=true&w=majority'
    mongo.init_app(app)

    app.register_blueprint(main)

    return app