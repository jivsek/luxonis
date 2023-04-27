from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Jelenovgreben123@localhost:5432/postgres'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Apartment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    images = db.Column(db.JSON)