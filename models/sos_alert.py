from app import db
from datetime import datetime

class SOSAlert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    audio_url = db.Column(db.String(255))
    image_url = db.Column(db.String(255))

    def __repr__(self):
        return f'<SOSAlert {self.id}>'