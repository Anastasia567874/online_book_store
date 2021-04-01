from flask import Flask
from data import db_session, books_api, genres_api, categories_api


def main():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
    db_session.global_init("db/book_store.db")
    app.register_blueprint(books_api.blueprint)
    app.register_blueprint(genres_api.blueprint)
    app.register_blueprint(categories_api.blueprint)
    app.run()


if __name__ == '__main__':
    main()