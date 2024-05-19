from flask import Blueprint,jsonify,request
from .models import Opportunity
from sqlalchemy import select
from . import db

feed = Blueprint('feed', __name__)

@feed.route('/retrieve', methods=['GET'])
def get_opportunities():
    
    opportunities = db.session.execute(select(Opportunity)).scalars().all()
    opportunity_list = []
    for opportunity in opportunities:
        opportunity_list.append(
            {
                'id': opportunity.id,
                'title':opportunity.title,
                'content':opportunity.content,
                'deadline':opportunity.deadline,
                'category':opportunity.category,
                'duration':opportunity.duration,
                'requirements':opportunity.requirements,
                'degree':opportunity.degree,
                'country':opportunity.country,
                'image':opportunity.image
            }
        )
    
    return jsonify({'opportunities':opportunity_list}), 200

@feed.route('/add', methods=['POST'])
def add_opportunity():
    title = request.json.get('title')
    content = request.json.get('content')
    university = request.json.get('university')
    deadline = request.json.get('deadline')
    category = request.json.get('category')
    duration = request.json.get('duration')
    requirements = request.json.get('requirements')
    degree = request.json.get('degree')
    country = request.json.get('country')
    image = request.json.get('image')
    
    new_opportunity = Opportunity(title = title, content = content, university = university, deadline = deadline, category = category, duration = duration, requirements = requirements, degree = degree, country = country, image = image)
    
    db.session.add(new_opportunity)
    db.session.commit()
    
    return jsonify({'message':'Success'}), 201