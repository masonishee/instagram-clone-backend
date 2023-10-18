from flask import Flask, request
import db
app = Flask(__name__)


@app.route('/')
def hello():
    return 'ITS A POSTS APP!'


@app.route("/posts.json")
def index():
    return db.posts_all()