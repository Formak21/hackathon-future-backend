from flask import Blueprint, jsonify

from ..models.models import Project

bp = Blueprint('project', __name__)


@bp.route('/get-all', methods=['GET'])
def get_all_projects():
    p = Project()
    projects = []
    projects.append(p)
    # Логика получения пользователей
    return jsonify({"projects": projects})


@bp.route('/get-project-by-id', methods=['GET'])
def get_user():
    p = Project()
    # Логика получения пользователей
    return jsonify({"project": p})


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
