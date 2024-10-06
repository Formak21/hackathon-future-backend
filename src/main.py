#!/usr/bin/env python

from factory import app, Base, db
from controllers import user, auth


if __name__ == "__main__":

    with app.app_context():
        from model import User, Session

        db.create_all()

        db.session.commit()

    app.register_blueprint(auth.bp, url_prefix='/auth')
    app.register_blueprint(user.bp, url_prefix='/user')
    app.run(port=5000, host="0.0.0.0")