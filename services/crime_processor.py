import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from geopy.distance import geodesic

class CrimeDataProcessor:
    def __init__(self, csv_file_path):
        self.crime_data = self.load_crime_data(csv_file_path)
        self.crime_clusters = None

    def load_crime_data(self, csv_file_path):
        df = pd.read_csv(csv_file_path)
        return df

    def preprocess_data(self):
        scaler = StandardScaler()
        features = self.crime_data[['latitude', 'longitude', 'severity']]
        scaled_features = scaler.fit_transform(features)
        return scaled_features

    def cluster_crime_data(self, n_clusters=10):
        scaled_features = self.preprocess_data()
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        self.crime_data['cluster'] = kmeans.fit_predict(scaled_features)
        self.crime_clusters = self.crime_data.groupby('cluster').agg({
            'latitude': 'mean',
            'longitude': 'mean',
            'severity': 'mean'
        }).reset_index()

    def calculate_safety_score(self, route):
        if self.crime_clusters is None:
            self.cluster_crime_data()

        safety_scores = []
        for i in range(len(route) - 1):
            start = route[i]
            end = route[i + 1]
            midpoint = ((start['lat'] + end['lat']) / 2, (start['lng'] + end['lng']) / 2)
            
            segment_score = self._calculate_segment_safety(midpoint)
            safety_scores.append(segment_score)

        return np.mean(safety_scores)

    def _calculate_segment_safety(self, point, max_distance=1):
        nearby_clusters = self._get_nearby_clusters(point, max_distance)
        if not nearby_clusters.empty:
            weighted_severity = np.sum(nearby_clusters['severity'] * nearby_clusters['weight'])
            return 100 - min(weighted_severity, 100) 
        return 100  

    def _get_nearby_clusters(self, point, max_distance):
        distances = self.crime_clusters.apply(
            lambda row: geodesic(point, (row['latitude'], row['longitude'])).km,
            axis=1
        )
        nearby = self.crime_clusters[distances <= max_distance].copy()
        if not nearby.empty:
            nearby['distance'] = distances[distances <= max_distance]
            nearby['weight'] = 1 / (nearby['distance'] ** 2)  # Inverse square weight
            return nearby
        return pd.DataFrame()

def process_crime_data(csv_file_path='path/to/your/crime_data.csv'):
    processor = CrimeDataProcessor(csv_file_path)
    processor.cluster_crime_data()
    return processor

def calculate_safety_score(route, processor):
    return processor.calculate_safety_score(route)