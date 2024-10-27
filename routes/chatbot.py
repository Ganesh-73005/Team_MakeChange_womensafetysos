from flask import Blueprint, request, jsonify
from services.gemini_ai import generate_chat_response

bp = Blueprint('chatbot', __name__)

@bp.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    try:
        response = generate_chat_response(user_message)
        return jsonify({'response': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500