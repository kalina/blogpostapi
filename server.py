import json
import os
from flask import Flask, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException, InternalServerError

PORT = 8080
# get the environment from environment variables if they're set
ENV = os.environ['APP_SETTINGS'] if os.environ.get('APP_SETTINGS', None) else 'config.DevConfig'

app = Flask(__name__)
app.config.from_object(ENV)

db = SQLAlchemy(app)


class Post(db.Model):
    """Class representation of blog posts stored in the database"""
    __tablename__ = 'posts'
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    body = db.Column(db.String())

    def to_dict(self):
        """Returns the Post object attributes in a dictionary"""
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
        post = Post(title=content['title'], body=content['body'])
        db.session.add(post)
        db.session.commit()
        location = {'Location': request.base_url + 's'}
        return jsonify(location), 201
    except KeyError as ke: 
        return jsonify({
            'code': 400,
            'name': 'Bad Request',
            'description': 'Could not process title and body'
        }), 400


@app.errorhandler(Exception)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    if not isinstance(e, HTTPException):
        return '', 500

    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


if __name__ == '__main__':
    app.run(port=PORT, host='0.0.0.0')
