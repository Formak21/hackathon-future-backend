from flask import Blueprint, jsonify, request, make_response

from model import User, Session
from factory import db
bp = Blueprint('user', __name__)


@bp.route('/get', methods=['GET'])  # разные поля отдаются по-разному
def get_user():
    req_session_id = request.cookies.get('session_id')
    authorized, user_id = check_user_authtorized(req_session_id)
    if not authorized:
        return jsonify({"error": "user unauthorized"}, 401)
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
        "tags":user.tags
    }

    return make_response(jsonify(resp_user), 200)

    # project = user = db.session.execute(db.select(Project).filter_by(id=project_id)).scalar_one()

    # if user.id in project.head:
    #     if search_user_id
    #

@bp.route('/get-user/<int:search_user_id>', methods=['GET'])  # разные поля отдаются по-разному
def get_user_by_id(search_user_id):
    req_session_id = request.cookies.get('session_id')
    authorized, user_id = check_user_authtorized(req_session_id)
    if not authorized:
        return jsonify({"error": "user authorized"}, 401)
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

    if user.id == search_user_id:
        make_response(jsonify(resp_user), 200)

    return make_response(jsonify(resp_user), 200)

    # project = user = db.session.execute(db.select(Project).filter_by(id=project_id)).scalar_one()

    # if user.id in project.head:
    #     if search_user_id
    #

#
@bp.route('/avatar', methods=['PUT'])
def set_user_avatar():
    data = request.get_json()
    req_session_id = request.cookies.get('session_id')
    authorized, user_id = check_user_authtorized(req_session_id)
    if not authorized:
        return jsonify({"error": "user unauthorized"}, 401)
    user = db.session.execute(db.select(User).filter_by(id=user_id)).scalar_one()

    if not data.get('photo_url'):
        return jsonify({"error": "photo mne dai"}, 418)
    user.photo_url = data.get('photo_url')
    db.session.commit()
    return jsonify({"message": "User updated"}), 200

#
# @bp.route('/get-orgs-by-project-id`', methods=['GET'])
# def get_user(project_id):
#     users = []
#     u = User()
#     users.append(u)
#     # Логика получения пользователя по ID
#     return jsonify({"orgs": users}), 200

#
# @bp.route('/get-head-by-project-id`', methods=['GET'])
# def get_user(project_id):
#     users = []
#     u = User()
#     users.append(u)
#     # Логика получения пользователя по ID
#     return jsonify({"head": users}), 200

#
# @bp.route('/get-expert-by-project-id`', methods=['GET'])
# def get_user(project_id):
#     users = []
#     u = User()
#     users.append(u)
#     # Логика получения пользователя по ID
#     return jsonify({"experts": users}), 200


# @bp.route('/get-volonteers-by-project-id`', methods=['GET'])
# def get_user(project_id):
#     data = request.get_json()
#
#     authtorized, user_id = check_user_authtorized()
#     if not authtorized:
#         return jsonify({"error": "user unauthtorized"}, 401)
#
#     user = db.session.execute(db.select(User).filter_by(user_id=user_id)).scalar_one()
#
#
#
#     users = []
#     u = User()
#     users.append(u)
#     # Логика получения пользователя по ID
#     return jsonify({"volonteers": users}), 200
#

@bp.route('/update-user', methods=['PUT'])
def update_user():
    data = request.get_json()
    req_session_id = request.cookies.get('session_id')
    authorized, user_id = check_user_authtorized(req_session_id)
    if not authorized:
        return jsonify({"error": "user unauthorized"}, 401)
    user = db.session.execute(db.select(User).filter_by(id=user_id)).scalar_one()

    user.first_name = data['first_name']
    user.mid_name = data['mid_name']
    user.last_name = data['last_name']
    user.tags = data['tags']
    user.email = data['email']
    user.info = data['info']

    db.session.commit()
    # Логика создания нового пользователя
    return jsonify({"message": "User updated"}), 200

# Другие маршруты для пользователя (например, обновление, удаление и т.д.)

def check_user_authtorized(req_session_id):
    session = db.session.execute(db.select(Session).filter_by(session_id=req_session_id)).scalar_one()
    if session == None:
        return False, None
    return True, session.user_id