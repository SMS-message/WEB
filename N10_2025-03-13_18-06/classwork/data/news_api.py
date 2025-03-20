import flask

from .news import News
from .users import User
from . import db_session

blueprint = flask.Blueprint(
    "news_api",
    __name__,
    template_folder="templates"
)

@blueprint.route("/api/news")
def get_news():
    db_sess = db_session.create_session()
    news = db_sess.query(News).all()
    return flask.jsonify(
        {
            "news": [item.to_dict(only=("title", "content", "user.name")) for item in news]
        }
    )

@blueprint.route("/api/news/<int:news_id>", methods=["GET"])
def get_one_news(news_id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).get(news_id)
    if not news:
        return flask.jsonify({"error": "not found"})
    return flask.jsonify(
        {
            "news": news.to_dict(only=("title", "content", "user.name", "is_private"))
        }
    )

@blueprint.route("/api/users")
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return flask.jsonify(
        {
            "users": [item.to_dict(only=("name", "hashed_password", "email")) for item in users]
        }
    )