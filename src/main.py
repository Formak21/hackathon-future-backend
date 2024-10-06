#!/usr/bin/env python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from src.factory import app, Base, db

if __name__ == "__main__":


    with app.app_context():
        from src.model.user import User
        from src.model.session import Session
        db.create_all()

        db.session.commit()

        users = db.session.scalars(db.select(User))

        for user in users:
            print(user)