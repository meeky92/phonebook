from datetime import datetime
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import UserMixin
from app import db


# Create a User class that inherits from the db.Model class
# CREATE TABLE user(id SERIAL PRIMARY KEY, email VARCHAR(50) UNIQUE NOT NULL, etc.)

# , UserMixin
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(10), nullable=False, unique = True)
    address = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     # Set the password to the hashed version of the password
    #     self.password = self.set_password(kwargs.get('password', ''))
    #     # Add and commit the new instance to the database
    #     db.session.add(self)
    #     db.session.commit()

    # def __str__(self):
    #     return self.username

    # def set_password(self, plain_password):
    #     return generate_password_hash(plain_password)

    # def check_password(self, password_guess):
    #     return check_password_hash(self.password, password_guess)


# @login.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)