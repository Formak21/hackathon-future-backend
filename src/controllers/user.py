from flask import Blueprint, jsonify

from ..models.models import User

bp = Blueprint('user', __name__)


@bp.route('/get-user-by-id', methods=['GET'])  # разные поля отдаются по-разному
def get_user_by_id(user_id):
    users = []
    u = User()
    users.append(u)
    # Логика получения пользователя по ID
    return jsonify({"user": users})


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
    users = []
    u = User()
    users.append(u)
    # Логика получения пользователя по ID
    return jsonify({"volonteers": users}), 200


@bp.route('/', methods=['POST'])
def create_user():
    # Логика создания нового пользователя
    return jsonify({"message": "User created"}), 201


@bp.route('/update-user', methods=['PUT'])
def update_user():
    # Логика создания нового пользователя
    return jsonify({"message": "User updated"}), 201

# Другие маршруты для пользователя (например, обновление, удаление и т.д.)
