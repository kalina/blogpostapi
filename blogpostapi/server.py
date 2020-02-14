import logging
import json
import os
import sqlite3
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

PORT = 8080
DB_FILE = 'blog.db'
ENV = os.environ['APP_SETTINGS'] if os.environ.get('APP_SETTINGS', None) else 'config.DevConfig'

app = Flask(__name__)
app.config.from_object(ENV)

db = SQLAlchemy(app)


class Post(db.Model):
    __tablename__ = 'posts'
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    body = db.Column(db.String())

    def to_dict(self):
        return {
            'post_id': self.post_id,
            'title': self.title,
            'body': self.body
        }

@app.route('/posts', methods=['GET'])
def get_posts():
    """Returns all blog posts"""
    posts = Post.query.all()
    posts_out = []
    for post in posts:
        posts_out.append(post.to_dict())

    return jsonify(posts_out)


@app.route('/post', methods=['POST'])
def new_post():
    """Adds a new post to the blog database"""
    content = request.json
    try:
        title = content['title']
        body = content['body']
        print(title, body)
        return '', 201
    except KeyError as ke:
        return 'Could not process title and body', 400


if __name__ == '__main__':
    app.run(port=PORT)
