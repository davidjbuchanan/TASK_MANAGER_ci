from flask import (
    Blueprint, flash, render_template, 
    redirect, request, session, url_for)
from bson.objectid import ObjectId
from task_manager.extensions import mongo
main = Blueprint('main', __name__)

@main.route('/')
@main.route('/get_tasks')
def index():
    tasks = mongo.db.tasks.find()
    return render_template('tasks.html', tasks=tasks)