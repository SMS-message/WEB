from flask import jsonify, make_response, request, Blueprint
from flask import make_response

from .db_session import create_session
from .jobs import Jobs

blueprint = Blueprint(
    "jobs_api",
    __name__,
    template_folder="templates"
)


@blueprint.route("/api/jobs")
def get_jobs():
    session = create_session()
    jobs = session.query(Jobs).all()

    return jsonify(
        {
            "jobs": [item.to_dict(only=("team_leader", "job", "work_size", "start_date")) for item in jobs]
        }
    )


@blueprint.route("/api/jobs/<int:job_id>", methods=["GET"])
def get_job(job_id):
    print("job_id")
    session = create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        return jsonify({"error": "Not found"})
    return jsonify(
        {
            "job": job.to_dict(only=("team_leader", "job", "work_size", "start_date"))
        }
    )


@blueprint.route("/api/jobs", methods=["POST"])
def post_job():
    if not request.json:
        return make_response(jsonify({"error": "Empty request"}), 400)
    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'work_size', 'collaborators', 'is_finished']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = create_session()
    job = Jobs(
        team_leader=request.json["team_leader"],
        job=request.json["job"],
        work_size=request.json["work_size"],
        collaborators=request.json["collaborators"],
        is_finished=request.json["is_finished"],
    )
    db_sess.add(job)
    db_sess.commit()

    return jsonify({"status": "OK"})
