from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://user:pass@localhost:5434/dbtest"

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(app, model_class=Base)