from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
import os
from dotenv import load_dotenv
load_dotenv()

db_instance = SQLAlchemy()


DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///default.db')

def connect_db(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    db_instance.init_app(app)
    Migrate(app, db_instance)
    with app.app_context():
        db_instance.create_all()
        print("Conectado ao banco gerando tabelas...")    

def db_persist(func):
    def persist(*args, **kwargs):
        func(*args, **kwargs)
        try:
            db_instance.session.commit()
            return True
        except Exception as e:
            db_instance.session.rollback()
            print(f"Erro ao salvr dados: {e}")
            return False
    return persist
