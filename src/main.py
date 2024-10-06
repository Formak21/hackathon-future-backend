#!/usr/bin/env python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://user:pass@localhost:5434/dbtest"


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(app, model_class=Base)
dbModel = db.Model


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":

    from src.model import User, Session

    with app.app_context():
        db.create_all()

        db.session.commit()

        users = db.session.scalars(db.select(User))

        for user in users:
            print(user)
