import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Book(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'books'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    author = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    number_of_pages = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    age_limit = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    annotation = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    in_stock = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    cover_art = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    genre_id = sqlalchemy.Column(sqlalchemy.Integer,
                                 sqlalchemy.ForeignKey("genres.id"))
    genre = orm.relation('Genre')
    category_id = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("categories.id"))
    category = orm.relation('Category')