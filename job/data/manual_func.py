from . import jobs
from . import users
from .db_session import create_session
session = create_session()

def add_user(surname, name, age, position, speciality, address, email) -> None:
    user = users.User()
    user.surname = surname
    user.name = name
    user.age = age
    user.position = position
    user.speciality = speciality
    user.address = address
    user.email = email
    session.add(user)
    session.commit()

def create_job(team_leader, job_text, work_size, collaborators, is_finished) -> None:
    from datetime import datetime
    job = jobs.Jobs()
    job.team_leader = team_leader
    job.job = job_text
    job.work_size = work_size
    job.collaborators = collaborators
    job.start_date = datetime.now()
    job.is_finished = is_finished
    session.add(job)
    session.commit()