import os

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

db=SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = f'{os.environ.get("SECRET_KEY")}'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{os.environ.get("POSTGRES_USERNAME")}:{os.environ.get("POSTGRES_PASSWORD")}@{os.environ.get("POSTGRES_URL")}/{os.environ.get("POSTGRES_DATABASE")}'

    CORS(app, resources={r"/*": {"origins": "*"}})
    db.init_app(app)

    from . import models
    
    from .assistant import assistant
    from .feed import feed
    from .forum import forum

    app.register_blueprint(assistant, url_prefix = '/')
    app.register_blueprint(feed, url_prefix = '/')
    app.register_blueprint(forum, url_prefix = '/')
    
    return app