from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    phonenumber = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(128), nullable=False)

class house(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    location = db.Column(db.String(100), nullable=False)

    price = db.Column(db.Integer, nullable=False)

    area = db.Column(db.String(50), nullable=False)

    type = db.Column(db.String(50), nullable=False)

    image = db.Column(db.String(255), nullable=False)

    owner = db.Column(db.String(50), nullable=False)

    landmark = db.Column(db.String(100), nullable=False)

    description = db.Column(db.Text, nullable=False)