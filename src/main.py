#!/usr/bin/env python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from src.factory import app

db = SQLAlchemy(app, model_class=DeclarativeBase)
dbModel = db.Model


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":

    from src.model.user import User
    from src.model.session import Session

    with app.app_context():
        db.create_all()

        db.session.commit()

        users = db.session.scalars(db.select(User))

        for user in users:
            print(user)
