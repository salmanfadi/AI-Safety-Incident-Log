# AI Safety Incident Log API

A RESTful API service for logging and managing hypothetical AI safety incidents.

## Technology Stack

- **Language**: Python 3.9+
- **Framework**: Flask
- **Database**: SQLite
- **ORM**: SQLAlchemy (Flask-SQLAlchemy)

## Project Structure

```
ai-safety-incident-api/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── utils.py
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

## Installation & Setup

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Steps

1. Clone the repository or extract the ZIP file:

```bash
git clone <repository-url>
# OR
unzip ai-safety-incident-api.zip
cd ai-safety-incident-api
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Initialize the database:

```bash
python -c "from app import db; db.create_all()"
```

5. (Optional) Populate the database with sample incidents:

```bash
python -c "from app.utils import populate_sample_data; populate_sample_data()"
```

6. Run the application:

```bash
python run.py
```

The API will be accessible at `http://localhost:5000`.

## Database Configuration

The application uses SQLite by default, with the database file located at `app/incidents.db`. This requires no additional configuration.

For production use, you can modify the database connection in `config.py` by setting the following environment variables:

- `DB_TYPE`: Database type (sqlite, postgresql, mysql)
- `DB_HOST`: Database host (if not using SQLite)
- `DB_PORT`: Database port
- `DB_NAME`: Database name
- `DB_USER`: Database username
- `DB_PASSWORD`: Database password

## API Endpoints

### 1. GET /incidents

Retrieves all incidents from the database.

**Request:**
```bash
curl -X GET http://localhost:5000/incidents
```

**Response:**
```json
[
  {
    "id": 1,
    "title": "Chatbot Producing Harmful Content",
    "description": "AI chatbot started generating unsafe content after a prompt injection attack.",
    "severity": "High",
    "reported_at": "2025-04-01T14:30:00Z"
  },
  {
    "id": 2,
    "title": "Bias in Job Recommendation Algorithm",
    "description": "AI system showing gender bias in software engineering job recommendations.",
    "severity": "Medium",
    "reported_at": "2025-04-02T09:15:00Z"
  }
]
```

### 2. POST /incidents

Creates a new incident in the database.

**Request:**
```bash
curl -X POST http://localhost:5000/incidents \
  -H "Content-Type: application/json" \
  -d '{
    "title": "New Incident Title",
    "description": "Detailed description here.",
    "severity": "Medium"
  }'
```

**Response:**
```json
{
  "id": 3,
  "title": "New Incident Title",
  "description": "Detailed description here.",
  "severity": "Medium",
  "reported_at": "2025-04-03T12:00:00Z"
}
```

### 3. GET /incidents/{id}

Retrieves a specific incident by ID.

**Request:**
```bash
curl -X GET http://localhost:5000/incidents/1
```

**Response:**
```json
{
  "id": 1,
  "title": "Chatbot Producing Harmful Content",
  "description": "AI chatbot started generating unsafe content after a prompt injection attack.",
  "severity": "High",
  "reported_at": "2025-04-01T14:30:00Z"
}
```

### 4. DELETE /incidents/{id}

Deletes an incident by ID.

**Request:**
```bash
curl -X DELETE http://localhost:5000/incidents/1
```

**Response:**
```json
{
  "message": "Incident deleted successfully"
}
```

## Error Handling

The API returns appropriate HTTP status codes and error messages:

- `400 Bad Request`: For invalid input data
- `404 Not Found`: When an incident with the specified ID doesn't exist
- `500 Internal Server Error`: For unexpected server errors

## Design Decisions

1. **Flask + SQLAlchemy**: Chosen for simplicity, rapid development, and ease of use for a small-scale API
2. **SQLite**: Selected for its zero-configuration nature, making the project easy to set up and run
3. **Input Validation**: Implemented custom validation to ensure severity values are restricted to "Low", "Medium", or "High"
4. **Automatic Timestamps**: The API automatically sets the `reported_at` field when creating new incidents
5. **Error Handling**: Comprehensive error handling ensures appropriate responses for various error scenarios
