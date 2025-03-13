import flask

from .news import News
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