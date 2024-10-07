from factory import db
from flask import Blueprint, jsonify, request, make_response
from model import User, Session, Chat

bp = Blueprint('chat', __name__)


@bp.route('/all', methods=['GET'])
def get_all_chats():
    user = __get_user(request.cookies['session_id'])

    if user is None:
        return __gen_response("User is not authorized.", 401)

    return __gen_response({"chats": user.chats}, 200)


def __get_user(session_id: str) -> User:
    try:
        return db.session.get(Session, session_id).user
    except:
        return None


def __gen_response(resp: dict or str, code: int):
    if isinstance(resp, str):
        return {"info": resp}

    return make_response(jsonify(resp, ), code)
