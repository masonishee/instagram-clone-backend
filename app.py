from flask import Flask, request
import db

app = Flask(__user__)

@app.route('/')
def hello():
    return 'ITS A POSTS APP!'

@app.route("/posts/<id>.json")
def show(id):
    return db.posts_find_by_id(id)

@app.route("/posts.json")
def index():
    return db.posts_all()

@app.route("/posts/<id>.json", methods=["PATCH"])
def update(id):
    user = request.form.get("user")
    image_url = request.form.get("image_url")
    comment = request.form.get("comment")
    return db.posts_update_by_id(id, user, image_url, comment)

@app.route("/posts.json", methods=["POST"])
def create():
    user = request.form.get("user")
    image_url = request.form.get("image_url")
    comment = request.form.get("comment")
    return db.posts_create(user, image_url, comment)