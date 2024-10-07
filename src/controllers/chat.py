from factory import db
from flask import Blueprint, jsonify, request, make_response
from model import User, Session, Chat, UserChatAssociation

bp = Blueprint('chat', __name__)


@bp.route('/all', methods=['GET'])
def get_all_chats():
    user = __get_user(request.cookies['session_id'])

    if user is None:
        return __gen_response("User is not authorized.", 401)

    return __gen_response({"chats": user.chats}, 200)


# update дописать

@bp.route('/', methods=['POST'])
def create_chat():
    data = request.get_json()

    this_user = __get_user(request.cookies['session_id'])

    if this_user is None:
        return __gen_response("User is not authorized.", 401)

    other_user = db.session.get(User, data["user_id"])

    if other_user is None:
        return __gen_response("User not found.", 400)

    # Добавить проверку на существование

    new_chat = Chat()
    this_association = UserChatAssociation(chat=new_chat, this_user=this_user)
    other_association = UserChatAssociation(chat=new_chat, this_user=other_user)

    db.session.add(new_chat)
    db.session.add(this_association)
    db.session.add(other_association)

    db.session.commit()

    return __gen_response("Chat created successfully.", 201)


def __get_user(session_id: str) -> User:
    try:
        return db.session.get(Session, session_id).user
    except:
        return None


def __gen_response(resp: dict or str, code: int):
    if isinstance(resp, str):
        return {"info": resp}

    return make_response(jsonify(resp, ), code)
