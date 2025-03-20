from flask import jsonify
from flask_restful import abort, Resource
from . import db_session  # Здесь может быть ошибка
from .news import News
from .reqparse import parser


def abort_if_news_not_found(news_id: int):
    db_sess = db_session.create_session()
    news = db_sess.query(News).get(news_id)
    if not news:
        abort(404, message=f"News {news_id} not found.")


class NewsResource(Resource):
    @staticmethod
    def get(news_id: int):
        abort_if_news_not_found(news_id)
        db_sess = db_session.create_session()
        news = db_sess.query(News).get(news_id)
        return jsonify(
            {
                'news':
                    news.to_dict(only=('title',
                                       'content',
                                       'user_id',
                                       'is_private'))

            }
        )

    @staticmethod
    def delete(news_id: int):
        abort_if_news_not_found(news_id)
        db_sess = db_session.create_session()
        news = db_sess.query(News).get(news_id)
        db_sess.delete(news)
        db_sess.commit()
        return jsonify({"success": "OK"})


class NewsListResource(Resource):
    @staticmethod
    def get():
        db_sess = db_session.create_session()
        news = db_sess.query(News).all()
        return jsonify(
            {
                "news": [item.to_dict(only=("title", "content", "user.name")) for item in news]
            }
        )

    @staticmethod
    def post():
        args = parser.parse_args()
        db_sess = db_session.create_session()
        news = News(
            title=args['title'],
            content=args['content'],
            user_id=args['user_id'],
            is_private=args['is_private']
        )
        db_sess.add(news)
        db_sess.commit()
        return jsonify({'success': 'OK', 'id': news.id})