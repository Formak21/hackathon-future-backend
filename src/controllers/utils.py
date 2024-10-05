from ..models_.db import DB as db


def check_user_authtorized(req_session_id):
    user = db.session.execute(db.select(Session).filter_by(session_id=req_session_id)).scalar_one()
    if user == None:
        return False
    return True
