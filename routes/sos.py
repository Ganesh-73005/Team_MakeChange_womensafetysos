from flask import Blueprint, request, jsonify
from models.sos_alert import SOSAlert
from models.user import User
from app import db
from firebase_admin import auth, storage

bp = Blueprint('sos', __name__)

@bp.route('/alert', methods=['POST'])
def create_sos_alert():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'No token provided'}), 401

    try:
        decoded_token = auth.verify_id_token(token)
        uid = decoded_token['uid']
        user = User.query.filter_by(firebase_uid=uid).first()

        data = request.json
        new_alert = SOSAlert(
            user_id=user.id,
            latitude=data['latitude'],
            longitude=data['longitude'],
            audio_url=data.get('audio_url'),
            image_url=data.get('image_url')
        )
        db.session.add(new_alert)
        db.session.commit()

       

        return jsonify({'message': 'SOS alert created', 'alert_id': new_alert.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@bp.route('/upload', methods=['POST'])
def upload_sos_media():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        try:
            filename = f"sos_media/{file.filename}"
            bucket = storage.bucket()
            blob = bucket.blob(filename)
            blob.upload_from_string(
                file.read(),
                content_type=file.content_type
            )
            blob.make_public()
            return jsonify({'url': blob.public_url}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500