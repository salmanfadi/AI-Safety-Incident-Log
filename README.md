# AI Safety Incident Log API

A robust, production-ready REST API service for logging and managing hypothetical AI safety incidents.

![API Architecture](https://via.placeholder.com/800x400?text=AI+Safety+Incident+Log+API+Architecture)

## Features

- ✅ Complete CRUD operations for AI safety incidents
- ✅ Advanced filtering and pagination
- ✅ API authentication
- ✅ Data validation
- ✅ Rate limiting
- ✅ Comprehensive logging
- ✅ Documented API with Swagger/OpenAPI
- ✅ Health and metrics endpoints
- ✅ Unit and integration testing
- ✅ Docker support

## Technology Stack

- **Language**: Python 3.9+
- **Framework**: Flask
- **Database**: SQLite (can be easily switched to PostgreSQL/MySQL)
- **ORM**: SQLAlchemy (Flask-SQLAlchemy)
- **Authentication**: API Key
- **Validation**: Marshmallow
- **Documentation**: OpenAPI/Swagger
- **Testing**: Pytest
- **Containerization**: Docker

## Installation

### Method 1: Local Installation

1. Clone the repository:
```bash
git clone <repository-url>
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
python setup_db.py
```

5. Run the application:
```bash
python run.py
```

The API will be accessible at `http://localhost:5000`.

### Method 2: Docker Installation

1. Build and start using Docker Compose:
```bash
docker-compose up -d
```

The API will be accessible at `http://localhost:5000`.

## Configuration

The application can be configured using environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `DB_TYPE` | Database type (sqlite, postgresql, mysql) | sqlite |
| `DB_HOST` | Database host | - |
| `DB_PORT` | Database port | - |
| `DB_NAME` | Database name | incidents |
| `DB_USER` | Database username | - |
| `DB_PASSWORD` | Database password | - |
| `API_KEY` | API key for authentication | test_api_key |
| `LOG_LEVEL` | Logging level | INFO |

## Database Schema

Each incident has the following fields:

- `id`: A unique identifier (primary key)
- `title`: A short summary of the incident (string)
- `description`: A detailed description of the incident (text)
- `severity`: Severity level: Low, Medium, or High (string)
- `reported_at`: Timestamp when the incident was reported (datetime)

## API Endpoints

### Public Endpoints

#### GET /
- **Description**: Root endpoint displaying API information
- **Authentication**: None
- **Response**: 200 OK with API information and available endpoints

```bash
curl -X GET http://localhost:5000/
```

```json
{
  "message": "Welcome to AI Safety Incident Log API",
  "endpoints": {
    "GET /incidents": "Get all incidents",
    "POST /incidents": "Create a new incident",
    "GET /incidents/{id}": "Get a specific incident",
    "DELETE /incidents/{id}": "Delete an incident",
    "PATCH /incidents/{id}": "Update an incident"
  }
}
```

#### GET /health
- **Description**: Health check endpoint
- **Authentication**: None
- **Response**: 200 OK with health status

```bash
curl -X GET http://localhost:5000/health
```

```json
{
  "status": "healthy",
  "database": "connected"
}
```

### Protected Endpoints

#### GET /incidents
- **Description**: Retrieve all incidents with optional filtering and pagination
- **Authentication**: API Key
- **Parameters**:
  - `severity`: Filter by severity (Low, Medium, High)
  - `from`: Filter incidents reported after this date (ISO format)
  - `to`: Filter incidents reported before this date (ISO format)
  - `page`: Page number (default: 1)
  - `per_page`: Items per page (default: 10)
- **Response**: 200 OK with paginated incidents

```bash
curl -X GET "http://localhost:5000/incidents?severity=High&page=1&per_page=5" \
  -H "X-API-Key: test_api_key"
```

```json
{
  "items": [
    { "id": 1, "title": "...", "description": "...", "severity": "High", "reported_at": "..." },
    { "id": 3, "title": "...", "description": "...", "severity": "High", "reported_at": "..." }
  ],
  "total": 2,
  "page": 1,
  "pages": 1,
  "per_page": 5
}
```

#### POST /incidents
- **Description**: Create a new incident
- **Authentication**: API Key
- **Rate Limit**: 10 requests per minute
- **Request Body**: JSON object with incident details
- **Response**: 201 Created with the newly created incident

```bash
curl -X POST http://localhost:5000/incidents \
  -H "Content-Type: application/json" \
  -H "X-API-Key: test_api_key" \
  -d '{
    "title": "New Incident Title",
    "description": "Detailed description here.",
    "severity": "Medium"
  }'
```

```json
{
  "id": 4,
  "title": "New Incident Title",
  "description": "Detailed description here.",
  "severity": "Medium",
  "reported_at": "2025-04-26T15:30:00Z"
}
```

#### GET /incidents/{id}
- **Description**: Retrieve a specific incident by ID
- **Authentication**: API Key
- **Response**: 200 OK with the requested incident, or 404 Not Found

```bash
curl -X GET http://localhost:5000/incidents/1 \
  -H "X-API-Key: test_api_key"
```

```json
{
  "id": 1,
  "title": "Chatbot Producing Harmful Content",
  "description": "AI chatbot started generating unsafe content after a prompt injection attack.",
  "severity": "High",
  "reported_at": "2025-04-01T14:30:00Z"
}
```

#### PATCH /incidents/{id}
- **Description**: Update a specific incident by ID
- **Authentication**: API Key
- **Request Body**: JSON object with fields to update
- **Response**: 200 OK with the updated incident, or 404 Not Found

```bash
curl -X PATCH http://localhost:5000/incidents/1 \
  -H "Content-Type: application/json" \
  -H "X-API-Key: test_api_key" \
  -d '{
    "severity": "Medium",
    "description": "Updated description after investigation."
  }'
```

```json
{
  "id": 1,
  "title": "Chatbot Producing Harmful Content",
  "description": "Updated description after investigation.",
  "severity": "Medium",
  "reported_at": "2025-04-01T14:30:00Z"
}
```

#### DELETE /incidents/{id}
- **Description**: Delete an incident by ID
- **Authentication**: API Key
- **Response**: 200 OK with confirmation, or 404 Not Found

```bash
curl -X DELETE http://localhost:5000/incidents/1 \
  -H "X-API-Key: test_api_key"
```

```json
{
  "message": "Incident deleted successfully"
}
```

#### GET /metrics
- **Description**: Get API usage metrics
- **Authentication**: API Key
- **Response**: 200 OK with metrics data

```bash
curl -X GET http://localhost:5000/metrics \
  -H "X-API-Key: test_api_key"
```

```json
{
  "total_incidents": 3,
  "by_severity": {
    "Low": 0,
    "Medium": 1,
    "High": 2
  }
}
```

## API Documentation

Interactive API documentation is available at `/api/docs` when the application is running.

## Development

### Setting Up Development Environment

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements-dev.txt
```

3. Run tests:
```bash
pytest
```

4. Check code quality:
```bash
flake8
```

### Project Structure

```
ai-safety-incident-api/
├── app/
│   ├── __init__.py        # Application initialization
│   ├── models.py          # Database models
│   ├── routes/            # API routes
│   │   ├── __init__.py
│   │   ├── incidents.py   # Incident endpoints
│   │   └── system.py      # System endpoints (health, metrics)
│   ├── schemas.py         # Validation schemas
│   └── utils.py           # Utility functions
├── tests/
│   ├── __init__.py
│   ├── conftest.py        # Test fixtures
│   ├── test_incidents.py  # Tests for incident endpoints
│   └── test_system.py     # Tests for system endpoints
├── logs/                  # Log files
├── config.py              # Configuration
├── requirements.txt       # Production dependencies
├── requirements-dev.txt   # Development dependencies
├── setup_db.py            # Database setup script
├── run.py                 # Application entry point
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose configuration
└── README.md              # This file
```

## Testing

The project includes both unit tests and integration tests using pytest:

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_incidents.py

# Run with coverage report
pytest --cov=app tests/
```

## Security Considerations

- API Key authentication for all data-modifying endpoints
- Input validation to prevent injection attacks
- Rate limiting to prevent abuse
- No direct SQL queries (using ORM)
- Logging sensitive operations

## Performance Considerations

- Database indexing on frequently queried fields
- Pagination for large result sets
- Query optimization
- Connection pooling

## CI/CD Integration

The repository includes GitHub Actions workflow configurations for:
- Running tests on pull requests
- Code quality checks
- Building and publishing Docker images

## Deployment

### Production Considerations

When deploying to production:
1. Use a production-grade WSGI server like Gunicorn
2. Set up a reverse proxy like Nginx
3. Use a more robust database (PostgreSQL recommended)
4. Set environment variables securely
5. Use proper API key management

### Sample Docker Deployment

```bash
# Build the Docker image
docker build -t ai-safety-incidents-api .

# Run with production settings
docker run -p 5000:5000 -e FLASK_ENV=production -e API_KEY=your_secure_key ai-safety-incidents-api
```

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
