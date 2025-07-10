

from config.db_config import db_instance, db_persist
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Role(db_instance.Model):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(80))
    users = relationship('User', backref='user')

  
    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return f"<Role {self.description}>"

    @db_persist
    def save(self):
        db_instance.session.add(self)
    
    @staticmethod
    def get_by_id(user_id):
        return Role.query.filter_by(id=user_id).first()

    @staticmethod
    def get_rolels():
        return Role.query.all()
    
