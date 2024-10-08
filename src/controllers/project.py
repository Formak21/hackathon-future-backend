from factory import db
from flask import Blueprint, jsonify, request, make_response
from model import User, Session, Project, UserProjectAssociation

bp = Blueprint('project', __name__)


@bp.route('/all', methods=['GET'])
def get_all_projects():
    req_session_id = request.cookies.get('session_id')
    authorized, user_id = __check_user_authtorized(req_session_id)
    user = db.session.execute(db.select(User).filter_by(id=user_id)).scalar_one()

    user_role = user.role

    projects = db.session.execute(db.select(Project).scalars())
    resp_projects = list(map(lambda proj: {
        "id": proj.id,
        "title": proj.title,
        "goals": proj.goals,
        "tags": proj.tags,
        "region": proj.region,
        "url_for_preview": proj.url_for_preview,
        "format": proj.format
    }, projects))
    return __jsonResponse({"projects": projects, "my_role": user_role}, 200)
    # Логика получения пользователей
    # return jsonify({"projects": projects})


@bp.route('/<int:project_id>', methods=['GET'])
def get_project_by_id(project_id):
    req_session_id = request.cookies.get('session_id')
    authorized, user_id = __check_user_authtorized(req_session_id)
    if not authorized:
        return __jsonResponse("user unauthorized", 401)
    user = db.session.execute(db.select(User).filter_by(id=user_id)).scalar_one()

    project = db.session.execute(db.select(Project).filter_by(id=project_id).scalar_one())

    user_role: str
    try:
        user_role = db.session.execute(
            db.select(UserProjectAssociation).filter_by(prokect_id=project_id, user_id=user.id).scalar_one()).role
    except:
        user_role = "guest"
    data = {}
    data["your_role"] = user_role

    if user_role == "org":
        pr_role = ["head", "activist", "volonteer", "org"]

        for role in pr_role:
            pr_user_role = db.session.execute(db.select(UserProjectAssociation).filter_by(prokect_id=project_id,
                                                                                          role=role).scalars())
            head_users = list(
                map(lambda user: db.session.execute(db.select(User).filter_by(id=user.id)).scalar_one(), pr_user_role))
            data[role] = head_users
        return __jsonResponse(data, 200)

    if user_role == "expert":
        pr_role = ["head", "activist", "expert", "partners", "volonteer"]

        for role in pr_role:
            pr_user_role = db.session.execute(db.select(UserProjectAssociation).filter_by(prokect_id=project_id,
                                                                                          role=role).scalars())
            head_users = list(
                map(lambda user: db.session.execute(db.select(User).filter_by(id=user.id)).scalar_one(), pr_user_role))
            data[role] = head_users

        resp_projects = list(map(lambda proj: {
            "id": proj.id,
            "title": proj.title,
            "goals": proj.goals,
            "tags": proj.tags,
            "region": proj.region,
            "url_for_preview": proj.url_for_preview,
            "format": proj.format
        }, project))
        data["project"] = resp_projects
        return __jsonResponse(data, 200)

    if user_role == "volonteer":
        resp_projects = list(map(lambda proj: {
            "id": proj.id,
            "title": proj.title,
            "goals": proj.goals,
            "tags": proj.tags,
            "region": proj.region,
            "url_for_preview": proj.url_for_preview,
            "format": proj.format
        }, project))
        data["project"] = resp_projects
        return __jsonResponse(data, 201)

    if user_role == "head":
        pr_role = pr_role = ["head", "activist", "expert", "partners", "volonteer"]

        for role in pr_role:
            pr_user_role = db.session.execute(db.select(UserProjectAssociation).filter_by(prokect_id=project_id,
                                                                                          role=role).scalars())
            head_users = list(
                map(lambda user: db.session.execute(db.select(User).filter_by(id=user.id)).scalar_one(), pr_user_role))
            data[role] = head_users
        return __jsonResponse(data, 200)

    resp_projects = list(map(lambda proj: {
        "id": proj.id,
        "title": proj.title,
        "goals": proj.goals,
        "tags": proj.tags,
        "region": proj.region,
        "url_for_preview": proj.url_for_preview,
        "format": proj.format
    }, project))
    data["project"] = resp_projects
    return __jsonResponse(data, 200)


@bp.route('/', methods=['PUT'])
def update_project():
    data = request.get_json()
    if not data.get("id"):
        return jsonify({"error": "id mne dai"}, 418)
    project_id = data.get("id")

    req_session_id = request.cookies.get('session_id')
    authorized, user_id = __check_user_authtorized(req_session_id)

    if not authorized:
        return __jsonResponse("user unauthorized", 401)
    user = db.session.execute(db.select(User).filter_by(id=user_id)).scalar_one()

    pr_user_role = db.session.execute(db.select(UserProjectAssociation).filter_by(prokect_id=project_id,
                                                                                  user_id=user.id).scalar_one())
    if pr_user_role.role != "head":
        return __jsonResponse("to update project you must ITS HEAD", 403)

    project = db.session.execute(db.select(Project).filter_by(id=project_id)).scalar_one()

    project.title = data.get("title") or project.title
    project.goals = data.get("goals") or project.goals
    project.region = data.get("region") or project.region
    project.short_info = data.get("short_info") or project.short_info
    project.contacts = data.get("contacts") or project.contacts
    project.requirements = data.get("requirements") or project.requirements
    project.format = data.get("format") or project.format
    project.contacts = data.get("contacts") or project.contacts
    project.url_for_preview = data.get("url_for_preview") or project.url_for_preview
    project.tags = data.get("tags") or project.tags
    project.docs = data.get("docs") or project.docs

    db.commit()
    return __jsonResponse("project updated", 200)


@bp.route('/', methods=['POST'])
def create_project():
    data = request.get_json()

    req_session_id = request.cookies.get('session_id')
    authorized, user_id = __check_user_authtorized(req_session_id)

    if not authorized:
        return __jsonResponse("user unauthorized", 401)
    user = db.session.execute(db.select(User).filter_by(id=user_id)).scalar_one()

    required = ["title", "goals", "region", "contacts", "docs", "tags"]
    for r in required:
        if not data.get(r):
            return __jsonResponse(f"field {data.get(r)} required", 400)

    project = Project()
    project.title = data.get("title")
    project.goals = data.get("goals")
    project.region = data.get("region")
    project.short_info = data.get("short_info") or ""
    project.contacts = data.get("contacts") or ""
    project.requirements = data.get("requirements") or ""
    project.format = data.get("format") or ""
    project.url_for_preview = data.get("url_for_preview") or ""
    project.tags = data.get("tags")
    project.docs = data.get("docs")

    db.session.add(project)
    db.session.commit()
    return __jsonResponse("project updated", 200)


@bp.route('/my', methods=['GET'])
def get_my_projects():
    data = request.get_json()

    req_session_id = request.cookies.get('session_id')
    authorized, user_id = __check_user_authtorized(req_session_id)

    if not authorized:
        return __jsonResponse("user unauthorized", 401)

    user = db.session.execute(db.select(User).filter_by(id=user_id)).scalar_one()

    try:
        pr_user_role = db.session.execute(db.select(UserProjectAssociation).filter_by(user_id=user.id)).scalars()
    except:
        pr_user_role = None

    if not pr_user_role:
        return __jsonResponse({"projects": []}, 200)
    data = {}
    projects = []

    for pr in pr_user_role:
        proj = db.session.execute(db.select(Project).filter_by(id=pr.project_id)).scalar_one()
        resp_proj = {
            "id": proj.id,
            "title": proj.title,
            "goals": proj.goals,
            "tags": proj.tags,
            "region": proj.region,
            "url_for_preview": proj.url_for_preview,
            "format": proj.format,
            "my_roll": pr.role
        }
        projects.append(resp_proj)
    data["project"] = projects
    return __jsonResponse(data, 200)


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
