from flask import Blueprint, request, jsonify
from firebase_admin import auth
from models.user import User
from app import db

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    try:
        user = auth.create_user(
            email=data['email'],
            password=data['password']
        )
        new_user = User(firebase_uid=user.uid, email=data['email'], name=data.get('name'))
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@bp.route('/login', methods=['POST'])
def login():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'No token provided'}), 401
    try:
        decoded_token = auth.verify_id_token(token)
        uid = decoded_token['uid']
        user = User.query.filter_by(firebase_uid=uid).first()
        if not user:
            return jsonify({'error': 'User not found'}), 404
        return jsonify({'message': 'Login successful', 'user_id': user.id}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 401