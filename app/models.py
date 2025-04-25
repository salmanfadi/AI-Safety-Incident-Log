from app import db
from datetime import datetime

class Incident(db.Model):
    """
    Model representing an AI safety incident.
    """
    __tablename__ = 'incidents'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    severity = db.Column(db.String(10), nullable=False)
    reported_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Incident {self.id}: {self.title}>"
    
    def to_dict(self):
        """Convert incident to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'severity': self.severity,
            'reported_at': self.reported_at.strftime('%Y-%m-%dT%H:%M:%SZ')
        }