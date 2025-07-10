from flask_marshmallow import Marshmallow

ma = Marshmallow()


def config_marshmallow(app):
    ma.init_app(app)
