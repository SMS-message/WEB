from data.db_session import *
from data import jobs_api
from data.user_resources import UserResource, UserListResource
import flask
from flask_restful import Api

app = flask.Flask(__name__)
app.config["SECRET_KEY"] = "123k1231f238i1gu23"
api = Api(app)



@app.route("/")
def root():
    return flask.render_template("index.html")

@app.errorhandler(404)
def not_found(error):
    return flask.make_response(flask.jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return flask.make_response(flask.jsonify({'error': 'Bad Request'}), 400)

global_init(f"db/mars_explorer.db")

app.register_blueprint(jobs_api.blueprint)
api.add_resource(UserResource, "/api/v2/users/<int:user_id>")
api.add_resource(UserListResource, "/api/v2/users")
app.run(host="127.0.0.1", port=8080)