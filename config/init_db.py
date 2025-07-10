from sqlalchemy import inspect

from config.db_config import db_instance
from models.users import User
from models.roles import Role


def model_exists(model_class):
    engine = db_instance.get_engine()
    inspector = inspect(engine)
    return inspector.has_table(model_class.__tablename__)


def init_load_data():
    if model_exists(Role):
        Role.init_data()
    if model_exists(User):
        User.init_data()
