from flask import Blueprint, jsonify

from ..models_.models import Project, ProjectShort

bp = Blueprint('feed', __name__)


@bp.route('/get-all-feed', methods=['GET'])
def get_all_feed():
    p = ProjectShort()
    projects = []
    projects.append(p)
    # Логика получения пользователей
    return jsonify({"projects": projects})


@bp.route('/get-all-feed-by-project', methods=['GET'])
def get_all_feed():
    p = ProjectShort()
    projects = []
    projects.append(p)
    # Логика получения пользователей
    return jsonify({"projects": projects})


@bp.route('/get-feed-by-id', methods=['GET'])
def get_feed_by_id():
    p = Project()
    # Логика получения пользователей
    return jsonify({"project": p})


@bp.route('/update`', methods=['PUT'])
def update_feed(user_id):
    # Логика получения пользователя по ID
    return jsonify({"message": "Project updated"}), 201


@bp.route('/', methods=['POST'])
def create_feed():
    # Логика создания нового пользователя
    return jsonify({"message": "User created"}), 201

# Другие маршруты для пользователя (например, обновление, удаление и т.д.)
