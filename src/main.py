#!/usr/bin/env python

from factory import app, db
from controllers import user, auth, project, feed, chat


if __name__ == "__main__":
    with app.app_context():
        from model import User, Session, Feed, Bid
        from model import Project, UserProjectAssociation
        from model import Chat, UserChatAssociation, Message

        db.create_all()
        db.session.commit()

    app.register_blueprint(auth.bp, url_prefix='/api/auth')
    app.register_blueprint(user.bp, url_prefix='/api/user')
    app.register_blueprint(project.bp, url_prefix='/api/project')
    app.register_blueprint(feed.bp, url_prefix='/api/feed')
    app.register_blueprint(chat.bp, url_prefix='/api/chat')
    app.run(port=5000, host="0.0.0.0")