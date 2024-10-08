import uuid
import bcrypt
from flask import Blueprint, jsonify, request, make_response

from model import User, Session
from factory import db

bp = Blueprint('auth-reg', __name__)


@bp.route('/', methods=['POST'])
def auth_user():
    data = request.get_json()
    # check data
    req_session_id = request.cookies.get('session_id')
    if data.get('session_id'):
        exist, resp_user_id = __check_user_authtorized(req_session_id)
        if exist:
            response = make_response(__jsonResponse({"success": "User already authorized"}), 200)
            response.set_cookie("session_id", req_session_id, samesite="lax", httponly=True)

            return response

    email = data.get('email')
    password = data.get('password')

    if not data.get('email'):
        return __jsonResponse({"error": "Email is required"}, 400)

    if not data.get('password'):
        return __jsonResponse({"error": "Password is required"}, 400)
    try:
        user = db.session.execute(
            db.select(User).filter_by(email=email)).scalar_one()  # вот тут нам надо чтобы мы чекали хэши!!! TODO
    except:
        return __jsonResponse({"error": "user with this email does not exist"}, 403)
    correct = bcrypt.checkpw(password.encode(), user.hashed_password.encode())

    if not correct:
        return __jsonResponse({"error": "Password or Email is wrong"}, 403)
    session_id = str(uuid.uuid1())

    db.session.add(Session(user_id=user.id, session_id=session_id))
    db.session.commit()
    # Логика создания нового пользователя

    response = make_response(jsonify({"success": "User authorized"}), 200)
    response.set_cookie("session_id", session_id, samesite="lax", httponly=True)

    return response


@bp.route('/register', methods=['POST'])
def create_user():
    data = request.get_json()
    # check data
    photo_url = ""
    first_name = data.get('first_name')
    mid_name = data.get('mid_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    phone = data.get('phone')
    role = "activist"

    if not data.get('mid_name'):
        mid_name = "нету"

    if not data.get('first_name'):
        return __jsonResponse("first_name is required", 400)

    if not data.get('last_name'):
        return __jsonResponse("last_name is required", 400)

    if not data.get('email'):
        return __jsonResponse("Email is required", 400)

    if not data.get('phone'):
        return __jsonResponse("Email is required", 400)

    if not data.get('password'):
        return __jsonResponse("Password is required", 400)

    try:
        user = db.session.execute(db.select(User).filter_by(email=email)).scalar_one()
    except:
        user = False
        print("полный газ")

    if user:
        return __jsonResponse("Email HAVE TO BE Unique", 409)

    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    user = User(first_name=first_name,
                mid_name=mid_name,
                last_name=last_name,
                email=email,
                hashed_password=(hashed_password.decode('utf-8')),
                role=role,
                info="",
                tags=[],
                photo_url=photo_url,
                phone=phone)
    db.session.add(user)
    db.session.commit()

    session_id = str(uuid.uuid1())

    db.session.add(Session(user_id=user.id, session_id=session_id))
    db.session.commit()
    # Логика создания нового пользователя

    response = make_response(jsonify({"success": "User registered"}), 200)
    response.set_cookie("session_id", session_id, samesite="lax", httponly=True)

    return response


@bp.route('/', methods=['DELETE'])
def logout_user():
    data = request.get_json()
    session_id = request.cookies.get('session_id')
    session = db.session.execute(db.select(Session).filter_by(session_id=session_id)).scalar_one()

    if not session:
        return __jsonResponse("Session does not exist", 400)

    db.session.delete(session)
    db.session.commit()

    response = make_response(jsonify({"success": "User is logout"}), 200)

    return response


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
