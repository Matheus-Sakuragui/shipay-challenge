from flask import Flask
from config.db_config import connect_db
from config.init_db import init_load_data

app = Flask(__name__)

connect_db(app)


app.config['BUNDLE_ERRORS'] = True

@app.cli.command('inicializar_db')
def initdb_command():
    init_load_data()
    print('Banco de dados inicializado.')

if __name__ == '__main__':
    app.run()
