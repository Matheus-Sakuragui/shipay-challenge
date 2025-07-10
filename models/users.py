from config.db_config import db_instance, db_persist
from sqlalchemy.sql import func
from sqlalchemy.orm import configure_mappers
import random 
import string


class User(db_instance.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = db_instance.Column(db_instance.Integer, primary_key=True, index=True)
    name = db_instance.Column(db_instance.String(80))
    email = db_instance.Column(db_instance.String(80))
    password = db_instance.Column(db_instance.String(200))
    role_id = db_instance.Column(db_instance.Integer, db_instance.ForeignKey('roles.id'))
    created_at = db_instance.Column(db_instance.DateTime(timezone=True), default=func.now())
    updated_at = db_instance.Column(db_instance.DateTime(timezone=True), default=func.now(), onupdate=func.now())

    def __init__(self, name, role_id, email, password=None):
        self.name = name
        self.email = email
        self.role_id = role_id
        self.password = password if password is not None else self.generate_pass()
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
        return User.query.all
    
    @staticmethod
    def generate_pass():
        numbers = string.digits
        letters = string.ascii_letters
        password = ''.join(random.choice(letters + numbers) for i in range(8))
        return password

    
    @staticmethod
    def init_data():
        if db_instance.session.query(User.id).count() == 0:
            for count_user in range(1, 6):
                user = User(email=f'usuario{count_user}@shipay.com', name=f"usuario{count_user}", role_id=count_user)
                user.save()


    def get_user_role(self):
        from models.roles import Role
        role = Role.query.filter_by(id=self.role_id).first()
        return role.description if role else None
    
configure_mappers()