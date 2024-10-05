from flask import Blueprint, jsonify

bp = Blueprint('project', __name__)


@bp.route('/get-all', methods=['GET'])
def get_user():
    # Логика получения пользователей
    return jsonify({"projects": []})

@bp.route('/get', methods=['GET'])
def get_user():
    # Логика получения пользователей
    return jsonify({"project": []})


@bp.route('/get-user-by-id', methods=['GET'])
def get_user(user_id):
    # Логика получения пользователя по ID
    return jsonify({"user_id": user_id})

@bp.route('/get`', methods=['GET'])
def get_user(user_id):
    # Логика получения пользователя по ID
    return jsonify({"user_id": user_id})


@bp.route('/', methods=['POST'])
def create_user():
    # Логика создания нового пользователя
    return jsonify({"message": "User created"}), 201

# Другие маршруты для пользователя (например, обновление, удаление и т.д.)
