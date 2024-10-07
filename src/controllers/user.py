from flask import Blueprint, jsonify, request, make_response

from model import User, Session
from factory import db
bp = Blueprint('user', __name__)


@bp.route('/', methods=['GET'])  # разные поля отдаются по-разному
def get_user():
    req_session_id = request.cookies.get('session_id')
    authorized, user_id = __check_user_authtorized(req_session_id)
    if not authorized:
        return __jsonResponse("user unauthorized", 401)
    user = db.session.execute(db.select(User).filter_by(id=user_id)).scalar_one()
    resp_user = {
        "id":user.id,
        "photo_url": user.photo_url,
        "first_name":user.first_name,
        "last_name":user.last_name,
        "mid_name":user.mid_name,
        "email":user.email,
        "role":user.role,
        "info":user.info,
        "tags":user.tags,
        "phone":user.phone
    }
    return __jsonResponse(resp_user, 200)

@bp.route('/get-user/<int:search_user_id>', methods=['GET'])  # разные поля отдаются по-разному
def get_user_by_id(search_user_id):
    req_session_id = request.cookies.get('session_id')
    authorized, user_id = __check_user_authtorized(req_session_id)
    if not authorized:
        return __jsonResponse("user authorized", 401)
    user = db.session.execute(db.select(User).filter_by(id=user_id)).scalar_one()

    resp_user = {
        "id": user.id,
        "photo_url": user.photo_url,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "mid_name": user.mid_name,
        "email": user.email,
        "role": user.role,
        "info": user.info,
        "tags": user.tags
    }
    return __jsonResponse(resp_user, 200)

@bp.route('/avatar', methods=['PUT'])
def set_user_avatar():
    data = request.get_json()
    req_session_id = request.cookies.get('session_id')
    authorized, user_id = __check_user_authtorized(req_session_id)
    if not authorized:
        return __jsonResponse("user unauthorized", 401)
    user = db.session.execute(db.select(User).filter_by(id=user_id)).scalar_one()

    if not data.get('photo_url'):
        return __jsonResponse("photo mne dai", 418)
    user.photo_url = data.get('photo_url')
    db.session.commit()
    return __jsonResponse("User updated", 200)


@bp.route('/', methods=['PUT'])
def update_user():
    data = request.get_json()
    req_session_id = request.cookies.get('session_id')
    authorized, user_id = __check_user_authtorized(req_session_id)
    if not authorized:
        return __jsonResponse("user unauthorized", 401)
    user = db.session.execute(db.select(User).filter_by(id=user_id)).scalar_one()

    if not data.get('photo_url'):
        return __jsonResponse("photo mne dai", 418)

    user.photo_url = data.get('photo_url') or user.photo_url
    user.first_name = data['first_name'] or user.first_name
    user.mid_name = data['mid_name'] or user.mid_name
    user.last_name = data['last_name'] or user.last_name
    user.tags = data['tags'] or user.tags
    user.email = data['email'] or user.email
    user.info = data['info'] or user.info

    db.session.commit()
    # Логика создания нового пользователя
    return __jsonResponse("User updated", 200)

# Другие маршруты для пользователя (например, обновление, удаление и т.д.)

def __check_user_authtorized(req_session_id):
    try:
        session = db.session.execute(db.select(Session).filter_by(session_id=req_session_id)).scalar_one()
    except:
        return False, None

    return True, session.user_id

def __jsonResponse(resp: dict or str, code: int):
    if isinstance(resp, str):
        resp = {"info": resp}

    return make_response(jsonify(resp), code)
