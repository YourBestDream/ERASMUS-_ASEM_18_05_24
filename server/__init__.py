import os

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = f'{os.environ.get("SECRET_KEY")}'
    CORS(app)

    from .assistant import assistant
    from .feed import feed
    from .forum import forum

    app.register_blueprint(assistant, url_prefix = '/')
    app.register_blueprint(feed, url_prefix = '/')
    app.register_blueprint(forum, url_prefix = '/')

    return app