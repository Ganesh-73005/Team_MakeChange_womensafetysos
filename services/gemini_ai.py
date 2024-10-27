import google.generativeai as genai
from config import Config

genai.configure(api_key=Config.GEMINI_API_KEY)

def generate_chat_response(message):
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[
        {
            "role": "user",
            "parts": "You are Safeher, an AI assistant focused on providing safety advice and support. Please keep your responses concise and relevant to safety topics."
        },
        {
            "role": "model",
            "parts": "Understood. I am Safeher, an AI assistant dedicated to providing safety advice and support. I'll keep my responses concise and focused on safety-related topics. How can I assist you with your safety concerns today?"
        }
    ])
    
    response = chat.send_message(message)
    return response.text