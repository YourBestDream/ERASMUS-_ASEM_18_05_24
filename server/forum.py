from flask import Blueprint,jsonify, request
from .models import PersonsHistory
from . import db
from sqlalchemy import select

forum = Blueprint('forum', __name__)

@forum.route('/histories', methods = ['GET'])
def histories():
    histories = db.session.execute(select(PersonsHistory)).scalars().all()
    history_list = []
    for history in histories:
        history_list.append({
            'id':history.id,
            'name':history.name,
            'content': history.content,
            'from':history.university_from,
            'to':history.university_to,
            'country':history.country
        })

    return jsonify(history_list),200

@forum.route('/histories/add', methods = ['POST'])
def history_add():
    
    name = request.json.get('name')
    content = request.json.get('content')
    university_from = request.json.get('from')
    university_to = request.json.get('to')
    country = request.json.get('country')
    
    new_history = PersonsHistory(name = name, content = content, university_from = university_from, university_to = university_to, country = country)
    
    db.session.add(new_history)
    db.session.commit()
    
    return jsonify({'message':'Success'}),201