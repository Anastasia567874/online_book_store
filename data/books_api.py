import flask
from flask import jsonify, render_template
from . import db_session
from .books import Book
from flask import request

blueprint = flask.Blueprint(
    'books_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/')
def get_books():
    db_sess = db_session.create_session()
    demand = db_sess.query(Book).all()
    books = [item.to_dict(only=('id', 'title', 'author', 'price', 'number_of_pages', 'age_limit',
                                'annotation', 'in_stock', 'cover_art')) for item in demand]
    return render_template('books.html', books_list=books)


@blueprint.route('/book', methods=['POST'])
def create_book():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'title', 'author', 'price', 'number_of_pages', 'age_limit',
                  'annotation', 'in_stock', 'cover_art', 'genre_id', 'category_id']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    for book in db_sess.query(Book).all():
        if book.id == request.json['id']:
            return jsonify({'error': 'Id already exists'})
    book = Book(
        id=request.json['id'],
        title=request.json['title'],
        author=request.json['author'],
        price=request.json['price'],
        number_of_pages=request.json['number_of_pages'],
        age_limit=request.json['age_limit'],
        annotation=request.json['annotation'],
        in_stock=request.json['in_stock'],
        cover_art=request.json['cover_art'],
        genre_id=request.json['genre_id'],
        category_id=request.json['category_id']
    )
    db_sess.add(book)
    db_sess.commit()
    return jsonify({'success': 'OK'})
