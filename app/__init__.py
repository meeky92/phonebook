from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config.from_object(Config)
from config import Config

from . import routes

# if __name__ == "__main__":
#   app.run(debug=True)