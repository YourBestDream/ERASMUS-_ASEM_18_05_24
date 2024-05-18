from . import db

from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import ARRAY

class Opportunity(db.Model):
    __tablename__ = 'opportunity'
    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text, nullable = False)
    content = db.Column(db.Text, nullable = False)
    university = db.Column(db.String(50),nullable = False)
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