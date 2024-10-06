#!/usr/bin/env python

from src.factory import app, Base, db

if __name__ == "__main__":

    with app.app_context():
        from src.model import User, Session

        db.create_all()

        db.session.commit()

        users = db.session.scalars(db.select(User))

        for user in users:
            print(user)