from flask import Blueprint, jsonify, request

from .utils import check_user_authtorized
from ..models_.models import User

bp = Blueprint('user', __name__)


@bp.route('/get-user-by-id', methods=['GET'])  # разные поля отдаются по-разному
def get_user_by_id():
    data = request.get_json()
    search_user_id = data['user_id']

    authtorized, user_id = check_user_authtorized()
    if not authtorized:
        return jsonify({"error": "user unauthtorized"}, 401)
    user = db.session.execute(db.select(User).filter_by(user_id=user_id)).scalar_one()

    if user.id == search_user_id:
        return jsonify({"user": user}, 200)
    
    # project = user = db.session.execute(db.select(Project).filter_by(id=project_id)).scalar_one()
    
    # if user.id in project.head:
    #     if search_user_id
    #


@bp.route('/get-users-by-project-id`', methods=['GET'])
def get_user(project_id):
    users = []
    u = User()
    users.append(u)
    # Логика получения пользователя по ID

    return jsonify({"users": users}), 200


@bp.route('/get-orgs-by-project-id`', methods=['GET'])
def get_user(project_id):
    users = []
    u = User()
    users.append(u)
    # Логика получения пользователя по ID
    return jsonify({"orgs": users}), 200


@bp.route('/get-head-by-project-id`', methods=['GET'])
def get_user(project_id):
    users = []
    u = User()
    users.append(u)
    # Логика получения пользователя по ID
    return jsonify({"head": users}), 200


@bp.route('/get-expert-by-project-id`', methods=['GET'])
def get_user(project_id):
    users = []
    u = User()
    users.append(u)
    # Логика получения пользователя по ID
    return jsonify({"experts": users}), 200


@bp.route('/get-volonteers-by-project-id`', methods=['GET'])
def get_user(project_id):
    data = request.get_json()

    authtorized, user_id = check_user_authtorized()
    if not authtorized:
        return jsonify({"error": "user unauthtorized"}, 401)

    user = db.session.execute(db.select(User).filter_by(user_id=user_id)).scalar_one()



    users = []
    u = User()
    users.append(u)
    # Логика получения пользователя по ID
    return jsonify({"volonteers": users}), 200


@bp.route('/update-user', methods=['PUT'])
def update_user():
    data = request.get_json()

    authtorized, user_id = check_user_authtorized()
    if not authtorized:
        return jsonify({"error": "user unauthtorized"}, 401)

    user = db.session.execute(db.select(User).filter_by(user_id=user_id)).scalar_one()

    user.first_name = data[user]['first_name']
    user.mid_name = data[user]['mid_name']
    user.last_name = data[user]['last_name']
    user.tags = data[user]['tags']
    user.email = data[user]['email']
    user.info = data[user]['info']

    db.session.commit()
    # Логика создания нового пользователя
    return jsonify({"message": "User updated"}), 201

# Другие маршруты для пользователя (например, обновление, удаление и т.д.)
