from flask import Blueprint, request, jsonify
from services.crime_processor import process_crime_data, calculate_safety_score
import requests
from config import Config

bp = Blueprint('safe_route', __name__)

@bp.route('/calculate', methods=['POST'])
def get_safe_route():
    data = request.json
    origin = data['origin']
    destination = data['destination']

   
    routes = get_routes(origin, destination)

    
    crime_data_processor = process_crime_data()
    safe_routes = []
    for route in routes:
        safety_score = calculate_safety_score(route, crime_data_processor)
        safe_routes.append({
            'route': route,
            'safety_score': safety_score
        })

    safe_routes.sort(key=lambda x: x['safety_score'], reverse=True)

    return jsonify(safe_routes)

def get_routes(origin, destination):
    url = f'https://maps.googleapis.com/maps/api/directions/json'
    params = {
        'origin': origin,
        'destination': destination,
        'alternatives': 'true',
        'key': Config.GOOGLE_MAPS_API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['routes']