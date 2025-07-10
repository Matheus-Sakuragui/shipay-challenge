

from config.db_config import db_instance, db_persist

from sqlalchemy.orm import relationship, configure_mappers

class Role(db_instance.Model):
    __tablename__ = 'roles'

    __table_args__ = {'extend_existing': True}

    id = db_instance.Column(db_instance.Integer, primary_key=True, index=True)
    description = db_instance.Column(db_instance.String(80))
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
    
    @staticmethod
    def init_data():
        if db_instance.session.query(Role.id).count() == 0:
            for count_role in range(1, 5):
                user = Role(description=f'PAPEL{count_role}')
                user.save()
    

configure_mappers()