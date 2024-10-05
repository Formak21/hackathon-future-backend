from flask import Blueprint, jsonify

bp = Blueprint('auth-reg', __name__)

@bp.route('/auth', methods=['POST'])
def create_user():
    # Логика создания нового пользователя
    return jsonify({"message": "User created"}), 201

@bp.route('/register', methods=['POST'])
def create_user():
    # Логика создания нового пользователя
    return jsonify({"message": "User created"}), 201

@bp.route('/logout', methods=['POST'])
def create_user():
    # Логика создания нового пользователя
    return jsonify({"message": "User created"}), 201

