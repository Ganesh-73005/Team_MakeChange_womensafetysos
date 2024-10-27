import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import googlemaps
from datetime import datetime
import folium
from geopy.distance import geodesic
import polyline
import warnings
warnings.filterwarnings('ignore')

class SafeRouteGenerator:
    def __init__(self, google_maps_api_key, risk_radius_km=0.5):
        """
        Initialize SafeRouteGenerator with Google Maps API key and risk radius
        risk_radius_km: radius around TASMAC shops considered risky (in kilometers)
        """
        self.gmaps = googlemaps.Client(key=google_maps_api_key)
        self.risk_radius = risk_radius_km
        self.scaler = StandardScaler()
        self.tasmac_locations = None
        self.clusters = None
        self.risk_areas = None
        
    def load_tasmac_data(self, csv_path):
        """Load TASMAC location data from CSV."""
        try:
            df = pd.read_csv(csv_path)
            required_columns = ['City', 'Location Name', 'Latitude', 'Longitude', 'Address']
            
           
            if not all(col in df.columns for col in required_columns):
                missing = [col for col in required_columns if col not in df.columns]
                raise ValueError(f"Missing required columns: {missing}")
            
            self.tasmac_locations = df
           
            self._create_risk_clusters()
            return True
            
        except Exception as e:
            raise Exception(f"Error loading TASMAC data: {str(e)}")
    
    def _create_risk_clusters(self, n_clusters=10):
        """Create clusters of TASMAC locations to identify high-risk areas."""
        X = self.tasmac_locations[['Latitude', 'Longitude']].values
        X_scaled = self.scaler.fit_transform(X)
        
       
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        self.clusters = kmeans.fit(X_scaled)
        
        cluster_counts = np.bincount(self.clusters.labels_)
        max_count = np.max(cluster_counts)
        risk_scores = cluster_counts / max_count
        
        self.risk_areas = {
            'centers': self.scaler.inverse_transform(kmeans.cluster_centers_),
            'risk_scores': risk_scores
        }
    
    def _calculate_point_risk(self, lat, lng):
        """Calculate risk score for a specific point based on proximity to TASMAC shops."""
        point = np.array([lat, lng])
        risk_score = 0
        
        for _, row in self.tasmac_locations.iterrows():
            distance = geodesic(
                (lat, lng),
                (row['Latitude'], row['Longitude'])
            ).kilometers
            
            if distance <= self.risk_radius:
           
                risk_score += 1 - (distance / self.risk_radius)
        
        return min(risk_score, 1.0) 
    def _calculate_route_risk(self, route_points):
        """Calculate overall risk score for a route."""
        risk_scores = []
        for point in route_points:
            risk = self._calculate_point_risk(point[0], point[1])
            risk_scores.append(risk)
        return np.mean(risk_scores)
    
    def get_safe_route(self, origin, destination, alternatives=True):
        """
        Find the safest route between origin and destination.
        
        Parameters:
        origin: tuple of (latitude, longitude) or string address
        destination: tuple of (latitude, longitude) or string address
        alternatives: boolean to request alternative routes
        
        Returns:
        Dictionary containing route information and safety scores
        """
        try:
          
            routes = self.gmaps.directions(
                origin,
                destination,
                alternatives=alternatives,
                mode='walking'
            )
            
            if not routes:
                raise Exception("No routes found")
            
            analyzed_routes = []
            
            for route in routes:
             
                points = polyline.decode(route['overview_polyline']['points'])
                
                risk_score = self._calculate_route_risk(points)
                
                
                analyzed_routes.append({
                    'route': route,
                    'points': points,
                    'risk_score': risk_score,
                    'duration': route['legs'][0]['duration']['text'],
                    'distance': route['legs'][0]['distance']['text']
                })
            
          
            analyzed_routes.sort(key=lambda x: x['risk_score'])
            
            return analyzed_routes
            
        except Exception as e:
            raise Exception(f"Error generating safe route: {str(e)}")
    
    def visualize_routes(self, analyzed_routes, origin, destination):
        """Create an interactive map showing routes and risk areas."""
    
        center_lat = (origin[0] + destination[0]) / 2
        center_lng = (origin[1] + destination[1]) / 2
        m = folium.Map(location=[center_lat, center_lng], zoom_start=13)
        
        for _, row in self.tasmac_locations.iterrows():
            folium.CircleMarker(
                location=[row['Latitude'], row['Longitude']],
                radius=5,
                color='red',
                fill=True,
                popup=f"TASMAC: {row['Location Name']}"
            ).add_to(m)
        
     
        colors = ['green', 'blue', 'purple'] 
        for i, route in enumerate(analyzed_routes):
            points = route['points']
            folium.PolyLine(
                points,
                weight=4,
                color=colors[i] if i < len(colors) else 'gray',
                popup=f"Route {i+1}<br>Risk Score: {route['risk_score']:.2f}<br>"
                      f"Duration: {route['duration']}<br>"
                      f"Distance: {route['distance']}"
            ).add_to(m)
      
        folium.Marker(
            origin,
            popup='Start',
            icon=folium.Icon(color='green', icon='info-sign')
        ).add_to(m)
        folium.Marker(
            destination,
            popup='End',
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)
        
        return m

def main1():
    """Example usage of SafeRouteGenerator"""
   
    API_KEY = ""
    route_generator = SafeRouteGenerator(API_KEY)
    
    try:
       
        route_generator.load_tasmac_data('tasmac_locations_tamilnadu.csv')
        
        
        origin = (13.0827, 80.2707) 
        destination = (13.0500, 80.2121)  
        
        routes = route_generator.get_safe_route(origin, destination)
        
        print("\nAnalyzed Routes:")
        for i, route in enumerate(routes):
            print(f"\nRoute {i+1}:")
            print(f"Risk Score: {route['risk_score']:.2f}")
            print(f"Duration: {route['duration']}")
            print(f"Distance: {route['distance']}")
        
        map_viz = route_generator.visualize_routes(routes, origin, destination)
        map_viz.save('safe_routes_map.html')
        print("\nMap has been saved as 'safe_routes_map.html'")
        
    except Exception as e:
        print(f"Error: {str(e)}")

