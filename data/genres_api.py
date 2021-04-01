import flask
from flask import jsonify, render_template
from . import db_session
from .genres import Genre
from flask import request

blueprint = flask.Blueprint(
    'genres_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/genres')
def get_genres():
    db_sess = db_session.create_session()
    demand = db_sess.query(Genre).all()
    genres = [item.to_dict(only=('id', 'title', 'categories')) for item in demand]
    return jsonify(genres)


@blueprint.route('/genre', methods=['POST'])
def create_genre():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'title', 'categories']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    for genre in db_sess.query(Genre).all():
        if genre.id == request.json['id']:
            return jsonify({'error': 'Id already exists'})
    genre = Genre(
        id=request.json['id'],
        title=request.json['title'],
        categories=request.json['categories']
    )
    db_sess.add(genre)
    db_sess.commit()
    return jsonify({'success': 'OK'})