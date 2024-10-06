import uuid
import bcrypt
from flask import Blueprint, jsonify, request, make_response

from model import User, Session
from factory import db
bp = Blueprint('project', __name__)


@bp.route('/get-all-projects-with-preview', methods=['GET'])
def get_all_projects():
    req_session_id = request.cookies.get('session_id')
    authorized, user_id = __check_user_authtorized(req_session_id)
    if not authorized:
        return jsonify({"error": "user authorized"}, 401)
    user = db.session.execute(db.select(User).filter_by(id=user_id)).scalar_one()

    projects = db.session.execute(db.select(Project).scalars())
    resp_projects = list(map(lambda proj: {
        "id":proj.id,
        "title":proj.title,
        "goals":proj.goals,
        "tags":proj.tags,
        "region":proj.region,
        "url_for_preview":proj.url_for_preview,
        "format":proj.format
        }, projects))

    return jsonify({"projects": projects}, 200)
    # Логика получения пользователей
    # return jsonify({"projects": projects})


@bp.route('/get-project-by-id<int:project_id>', methods=['GET'])
def get_project_by_id(project_id):
    req_session_id = request.cookies.get('session_id')
    authorized, user_id = __check_user_authtorized(req_session_id)
    if not authorized:
        return jsonify({"error": "user unauthorized"}, 401)
    user = db.session.execute(db.select(User).filter_by(id=user_id)).scalar_one()

    project = db.session.execute(db.select(Project).filter_by(id=project_id).scalar_one())

    user_role: str
    try:
        user_role = db.session.execute(db.select(UserProjectAssociation).filter_by(prokect_id=project_id, user_id=user.id).scalar_one()).role
    except:
        user_role = "guest"
    data = {}
    data["your_role"] = user_role

    if user_role == "org":
        return jsonify({"project": project}, 200)
    if user_role == "expert":
        return jsonify({"project": project}, 200)
    if user_role == "volonteer":
        return jsonify({"project": project}, 200)
    if user_role == "head":
        pr_role = ["head", "activist", "expert", "partners"]

        for role in pr_role:
            pr_user_role = db.session.execute(db.select(UserProjectAssociation).filter_by(prokect_id=project_id,
                                                                                       role=role).scalars())
            head_users = list(
                map(lambda user: db.session.execute(db.select(User).filter_by(id=user.id)).scalar_one(), pr_user_role))
            data[role]=head_users

        return jsonify({"project":project}, 200)


    # guest

    return jsonify({"project":project}, 200)


@bp.route('/update`', methods=['PUT'])
def update_poject(user_id):
    # Логика получения пользователя по ID
    return jsonify({"message": "Project updated"}), 201


@bp.route('/my', methods=['POST'])
def create_poject():
    # Логика создания нового пользователя
    return jsonify({"message": "User created"}), 201

# Другие маршруты для пользователя (например, обновление, удаление и т.д.)

def __check_user_authtorized(req_session_id):
    session = db.session.execute(db.select(Session).filter_by(session_id=req_session_id)).scalar_one()
    if session == None:
        return False, None
    return True, session.user_id

