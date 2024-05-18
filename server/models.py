from . import db

from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import ARRAY

class Opportunity(db.Model):
    __tablename__ = 'opportunity'
    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text, nullable = False)
    content = db.Column(db.Text, nullable = False)
    university = db.Column(db.String(512),nullable = False)
    deadline = db.Column(db.DateTime(timezone = True), nullable = False)
    category = db.Column(db.String(256), nullable = False)
    duration = db.Column(db.Integer, nullable=False)
    requirements = db.Column(ARRAY(db.String), nullable=False)
    degree = db.Column(db.String(128),nullable = False)
    country = db.Column(db.String(256), nullable = False)
    image = db.Column(db.String(4096), nullable = False)
    created_at = db.Column(db.DateTime(timezone = True), default = func.now(), nullable = False)
    updated_at = db.Column(db.DateTime(timezone = True), default = func.now())

class University(db.Model):
    __tablename__ = 'universities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(128), nullable=False)
    
    universities = db.relationship('University', secondary='category_university', backref='categories')

#M2M
class Category_University(db.Model):
    __tablename__ = 'category_university'
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), primary_key=True)
    university_id = db.Column(db.Integer, db.ForeignKey('universities.id'), primary_key=True)

class Degree(db.Model):
    __tablename__ = 'degree'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

class PersonsHistory(db.Model):
    __tablename__ = 'persons_history'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text)
    university_from = db.Column(db.String(512))
    university_to = db.Column(db.String(512))
    country = db.Column(db.String(256))
    
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128), nullable = False)
    surname = db.Column(db.String(128), nullable = False)
    email = db.Column(db.String(256), unique = True)
    password_hash = db.Column(db.String(256), unique = True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class TokenBlacklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, unique=True)  # JWT ID
    created_at = db.Column(db.DateTime(timezone = True), default = func.now(), nullable = False)
    
    def __init__(self, jti):
        self.jti = jti
    