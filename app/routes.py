from flask import request, jsonify
from app import app, db
from app.models import Incident
from app.utils import validate_incident_data
from datetime import datetime

@app.route('/', methods=['GET'])
def home():
    """
    Home route - provides basic API information.
    """
    return jsonify({
        'message': 'Welcome to AI Safety Incident Log API',
        'endpoints': {
            'GET /incidents': 'Get all incidents',
            'POST /incidents': 'Create a new incident',
            'GET /incidents/{id}': 'Get a specific incident',
            'DELETE /incidents/{id}': 'Delete an incident'
        }
    }), 200

@app.route('/incidents', methods=['GET'])
def get_all_incidents():
    """
    Retrieve all incidents from the database.
    """
    incidents = Incident.query.all()
    return jsonify([incident.to_dict() for incident in incidents]), 200

@app.route('/incidents', methods=['POST'])
def create_incident():
    """
    Create a new incident.
    """
    # Get JSON data from request
    data = request.get_json()
    
    # Validate input data
    validation_result = validate_incident_data(data)
    if not validation_result['valid']:
        return jsonify({'error': validation_result['message']}), 400
    
    # Create new incident
    new_incident = Incident(
        title=data['title'],
        description=data['description'],
        severity=data['severity']
    )
    
    # Add to database
    db.session.add(new_incident)
    db.session.commit()
    
    # Return created incident
    return jsonify(new_incident.to_dict()), 201

@app.route('/incidents/<int:incident_id>', methods=['GET'])
def get_incident(incident_id):
    """
    Retrieve a specific incident by ID.
    """
    incident = Incident.query.get(incident_id)
    
    if not incident:
        return jsonify({'error': 'Incident not found'}), 404
    
    return jsonify(incident.to_dict()), 200

@app.route('/incidents/<int:incident_id>', methods=['DELETE'])
def delete_incident(incident_id):
    """
    Delete an incident by ID.
    """
    incident = Incident.query.get(incident_id)
    
    if not incident:
        return jsonify({'error': 'Incident not found'}), 404
    
    db.session.delete(incident)
    db.session.commit()
    
    return jsonify({'message': 'Incident deleted successfully'}), 200