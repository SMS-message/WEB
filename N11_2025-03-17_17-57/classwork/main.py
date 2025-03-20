from flask import Flask
from flask_restful import Api
from data import db_session
from data.news_resources import NewsListResource, NewsResource

# Создадим вторую версию нашего REST-сервиса.
# После создания flask-приложения в файле main.py
# создадим объект RESTful-API:
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app, catch_all_404s=True)

def main():
    db_session.global_init("db/blogs.db")
    api.add_resource(NewsListResource, "/api/v2/news")
    api.add_resource(NewsResource, "/api/v2/news/<int:news_id>")
    app.run(port=8080, host='127.0.0.1')

if __name__ == '__main__':
    main()
