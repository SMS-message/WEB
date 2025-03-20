from flask import jsonify
from flask_restful import abort, Resource
from . import db_session  # Здесь может быть ошибка
from .users import User
from .reqparse import parser


def abort_if_news_not_found(user_id: int):
    db_sess = db_session.create_session()
    news = db_sess.query(User).get(user_id)
    if not news:
        abort(404, message=f"User {user_id} not found.")


class UserResource(Resource):
    @staticmethod
    def get(user_id: int):
        abort_if_news_not_found(user_id)
        db_sess = db_session.create_session()
        user = db_sess.query(User).get(user_id)
        return jsonify(
            {
                'user':
                    user.to_dict(only=("name", "age", "position"))

            }
        )

    @staticmethod
    def delete(user_id: int):
        abort_if_news_not_found(user_id)
        db_sess = db_session.create_session()
        news = db_sess.query(User).get(user_id)
        db_sess.delete(news)
        db_sess.commit()
        return jsonify({"success": "OK"})


class UserListResource(Resource):
    @staticmethod
    def get():
        db_sess = db_session.create_session()
        users = db_sess.query(User).all()
        return jsonify(
            {
                "users": [item.to_dict(only=("name", "age", "position")) for item in users]
            }
        )

    @staticmethod
    def post():
        args = parser.parse_args()
        user = User(
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args["speciality"],
            address=args["address"],
            email=args["email"],
            modified_date=args["modified_date"]
        )
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()
        return jsonify({'success': 'OK', 'id': user.id})