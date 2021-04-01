import flask
from flask import jsonify, render_template
from . import db_session
from .categories import Category
from flask import request

blueprint = flask.Blueprint(
    'categories_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/categories')
def get_categories():
    db_sess = db_session.create_session()
    demand = db_sess.query(Category).all()
    categories = [item.to_dict(only=('id', 'title')) for item in demand]
    return jsonify(categories)


@blueprint.route('/category', methods=['POST'])
def create_category():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'title']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    for category in db_sess.query(Category).all():
        if category.id == request.json['id']:
            return jsonify({'error': 'Id already exists'})
    category = Category(
        id=request.json['id'],
        title=request.json['title']
    )
    db_sess.add(category)
    db_sess.commit()
    return jsonify({'success': 'OK'})