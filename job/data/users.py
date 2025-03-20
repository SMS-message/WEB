from . import db_session
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin


class User(db_session.SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = db_session.sqlalchemy.Column(db_session.sqlalchemy.Integer, primary_key=True, autoincrement=True)
    surname = db_session.sqlalchemy.Column(db_session.sqlalchemy.String)
    name = db_session.sqlalchemy.Column(db_session.sqlalchemy.String)
    age = db_session.sqlalchemy.Column(db_session.sqlalchemy.Integer)
    position = db_session.sqlalchemy.Column(db_session.sqlalchemy.String)
    speciality = db_session.sqlalchemy.Column(db_session.sqlalchemy.String)
    address = db_session.sqlalchemy.Column(db_session.sqlalchemy.String)
    email = db_session.sqlalchemy.Column(db_session.sqlalchemy.String, unique=True)
    hashed_password = db_session.sqlalchemy.Column(db_session.sqlalchemy.String)
    modified_date = db_session.sqlalchemy.Column(db_session.sqlalchemy.DateTime)