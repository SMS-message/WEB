from . import db_session
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin

class Jobs(db_session.SqlAlchemyBase, SerializerMixin, UserMixin):
    __tablename__ = 'jobs'

    id = db_session.sqlalchemy.Column(db_session.sqlalchemy.Integer, primary_key=True, autoincrement=True)
    team_leader = db_session.sqlalchemy.Column(db_session.sqlalchemy.Integer, db_session.sqlalchemy.ForeignKey("users.id"))
    job = db_session.sqlalchemy.Column(db_session.sqlalchemy.String)
    work_size = db_session.sqlalchemy.Column(db_session.sqlalchemy.Integer)
    collaborators = db_session.sqlalchemy.Column(db_session.sqlalchemy.String)
    start_date = db_session.sqlalchemy.Column(db_session.sqlalchemy.DateTime)
    end_date = db_session.sqlalchemy.Column(db_session.sqlalchemy.DateTime)
    is_finished = db_session.sqlalchemy.Column(db_session.sqlalchemy.Boolean)

    def __repr__(self):
        string = "Jobs("
        for item in [self.id, self.team_leader, self.job, self.work_size, self.collaborators, self.start_date, self.end_date, self.is_finished]:
            string += f"{item}, "
        string += ")"
        return string