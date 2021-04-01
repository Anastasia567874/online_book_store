from flask import Flask
import os
from data import db_session, books_api, genres_api, categories_api


def main():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
    db_session.global_init("db/book_store.db")
    app.register_blueprint(books_api.blueprint)
    app.register_blueprint(genres_api.blueprint)
    app.register_blueprint(categories_api.blueprint)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()