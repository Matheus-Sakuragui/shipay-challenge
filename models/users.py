from config.db_config import db_instance, db_persist
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

class User(db_instance.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80))
    email = Column(String(80))
    password = Column(String(200))
    role_id = Column(Integer, ForeignKey('roles.id'))
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

    def __init__(self, name, role_id, email):
        self.name = name
        self.email = email
        self.role_id = role_id
    def __repr__(self):
        return f"<User {self.name}>"

    @db_persist
    def save(self):
        db_instance.session.add(self)
    
    @db_persist
    def delete(self):
        db_instance.session.delete(self)

    @staticmethod
    def get_by_id(user_id):
        return User.query.filter_by(id=user_id).first()
    @staticmethod
    def get_users():
        return User.query.all()

    # def get_user_role(self):
    #     from models.roles import Role
    #     role = Role.query.filter_by(id=self.role_id).first()
    #     return role.name if role else None
    
