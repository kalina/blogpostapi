import logging
import json
import sqlite3
from flask import Flask, request

PORT = 8080

app = Flask(__name__)

app.config["DEBUG"] = True


@app.route('/posts', methods=['GET'])
def get_posts():
    """Returns all blog posts"""
    return '<h1>TEST GET</p>'


@app.route('/post', methods=[ 'POST'])
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
