from flask import Flask
from config.db_config import connect_db

app = Flask(__name__)

connect_db(app)


app.config['BUNDLE_ERRORS'] = True



if __name__ == '__main__':
    app.run()
