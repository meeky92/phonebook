from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_login import LoginManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# login = LoginManager(app)

app.config['SECRET_KEY'] = 'you-will-never-guess'

from . import routes, models

# if __name__ == "__main__":
#   app.run(debug=True)