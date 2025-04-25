from app import db
from app.models import Incident
from datetime import datetime

def validate_incident_data(data):
    """
    Validate incident data.
    
    Args:
        data (dict): The incident data to validate.
        
    Returns:
        dict: Dictionary with validation result.
    """
    # Check for required fields
    required_fields = ['title', 'description', 'severity']
    for field in required_fields:
        if field not in data:
            return {
                'valid': False,
                'message': f"Missing required field: {field}"
            }
    
    # Validate severity
    valid_severities = ['Low', 'Medium', 'High']
    if data['severity'] not in valid_severities:
        return {
            'valid': False,
            'message': f"Invalid severity. Must be one of: {', '.join(valid_severities)}"
        }
    
    return {'valid': True}

def populate_sample_data():
    """
    Populate the database with sample incidents.
    """
    # Check if database already has data
    if Incident.query.count() > 0:
        print("Database already has data. Skipping sample data population.")
        return
    
    # Sample incidents
    sample_incidents = [
        {
            'title': 'Chatbot Producing Harmful Content',
            'description': 'AI chatbot started generating unsafe content after a prompt injection attack.',
            'severity': 'High',
            'reported_at': datetime(2025, 4, 1, 14, 30, 0)
        },
        {
            'title': 'Bias in Job Recommendation Algorithm',
            'description': 'AI system showing gender bias in software engineering job recommendations.',
            'severity': 'Medium',
            'reported_at': datetime(2025, 4, 2, 9, 15, 0)
        },
        {
            'title': 'Data Privacy Breach',
            'description': 'AI system accidentally included private user data in its training dataset.',
            'severity': 'High',
            'reported_at': datetime(2025, 4, 3, 11, 45, 0)
        }
    ]
    
    # Add sample incidents to database
    for incident_data in sample_incidents:
        incident = Incident(
            title=incident_data['title'],
            description=incident_data['description'],
            severity=incident_data['severity'],
            reported_at=incident_data['reported_at']
        )
        db.session.add(incident)
    
    # Commit changes
    db.session.commit()
    print("Sample data populated successfully.")