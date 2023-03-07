import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Jobs(SqlAlchemyBase):
    __tablename__ = 'Jobs'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    job = sqlalchemy.Column(sqlalchemy.String)
    work_size = sqlalchemy.Column(sqlalchemy.String)
    collaborators = sqlalchemy.Column(sqlalchemy.String)
    start_data = sqlalchemy.Column(sqlalchemy.Date)
    end_data = sqlalchemy.Column(sqlalchemy.Date)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean)