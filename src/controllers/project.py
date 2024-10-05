from flask import Blueprint, jsonify

from ..models_.models import Project, ProjectShort

bp = Blueprint('project', __name__)


@bp.route('/get-all-projects-with-preview', methods=['GET'])
def get_all_projects():
    p = ProjectShort()
    projects = []
    projects.append(p)
    # Логика получения пользователей
    return jsonify({"projects": projects})


@bp.route('/get-project-by-id', methods=['GET'])
def get_project_by_id():
    p = Project()
    # Логика получения пользователей
    return jsonify({"project": p})


@bp.route('/update`', methods=['PUT'])
def update_poject(user_id):
    # Логика получения пользователя по ID
    return jsonify({"message": "Project updated"}), 201


@bp.route('/', methods=['POST'])
def create_poject():
    # Логика создания нового пользователя
    return jsonify({"message": "User created"}), 201

# Другие маршруты для пользователя (например, обновление, удаление и т.д.)
