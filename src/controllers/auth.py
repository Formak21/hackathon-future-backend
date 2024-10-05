import uuid
import bcrypt
from flask import Blueprint, jsonify, request, make_response

from ..models.db import DB as db
from ..models.models import session

bp = Blueprint('auth-reg', __name__)


@bp.route('/auth', methods=['POST'])
def auth_user():
    data = request.get_json()
    # check data
    req_session_id = data.get('session_id')
    if data.get('session_id'):
        user = db.session.execute(db.select(Session).filter_by(session_id=req_session_id)).scalar_one()
        if user:
            response = make_response(jsonify({"success": "User auth"}), 200)
            response.headers.add("session_id", req_session_id)

            return response

    email = data.get('email')
    password = data.get('password')

    if not data.get('email'):
        return jsonify({"error": "Email is required"}, 400)

    if not data.get('password'):
        return jsonify({"error": "Password is required"}, 400)

    user = db.session.execute(db.select(User).filter_by(email=email)).scalar_one()  # вот тут нам надо чтобы мы чекали хэши!!! TODO

    correct = bcrypt.checkpw(password, user.hashed_password)

    if not correct:
        return jsonify({"error": "Password or Email is wrong"}, 400)
    session_id = str(uuid.UUID)

    db.session.add(Session(user_id=user.id, session_id=session_id))
    db.session.commit()
    # Логика создания нового пользователя

    response = make_response(jsonify({"success": "User auth"}), 200)
    response.headers.add("session_id", session_id)

    return response


@bp.route('/register', methods=['POST'])
def create_user():
    data = request.get_json()
    # check data
    first_name = data.get('first_name')
    mid_name = data.get('mid_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')

    if not data.get('mid_name'):
        mid_name = "нету"

    if not data.get('first_name'):
        return jsonify({"error": "first_name is required"}, 400)

    if not data.get('last_name'):
        return jsonify({"error": "last_name is required"}, 400)

    if not data.get('email'):
        return jsonify({"error": "Email is required"}, 400)

    if not data.get('password'):
        return jsonify({"error": "Password is required"}, 400)

    user = db.session.execute(db.select(User).filter_by(email=email)).scalar_one()

    if user:
        return jsonify({"error": "Email HAVE TO BE Unique"}, 400)

    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    db.session.add(User(first_name=first_name, mid_name=mid_name,
                        last_name=last_name, email=email,
                        hashed_password=hashed_password))
    db.session.commit()

    session_id = str(uuid.UUID)

    db.session.add(Session(user_id=user_id, session_id=session_id))
    db.session.commit()
    # Логика создания нового пользователя

    response = make_response(jsonify({"success": "User auth"}), 200)
    response.headers.add("session_id", session_id)

    return response


@bp.route('/logout', methods=['POST'])
def logout_user():
    data = request.get_json()
    session_id = data['session_id']
    session = db.session.execute(db.select(Session).filter_by(session_id=session_id)).scalar_one()

    if session:
        return jsonify({"error": "Session does not exist"}, 400)

    db.session.delete(Session(session_id=session_id))
    db.session.commit()

    response = make_response(jsonify({"success": "User is logout"}), 200)

    return response
