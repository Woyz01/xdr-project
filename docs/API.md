# API Documentation

## Base URL

```
http://localhost:8000/api/v1
```

## Authentication

Currently, the API uses no authentication for development. In production, JWT authentication is recommended.

## Threats

### List Threats

```http
GET /threats?skip=0&limit=10
```

**Response:**
```json
[
  {
    "id": 1,
    "threat_id": "uuid-123",
    "title": "Suspicious Process Detected",
    "description": "Detected suspicious process behavior",
    "severity": "HIGH",
    "threat_type": "malware",
    "source": "endpoint",
    "indicators": {
      "process_name": "suspicious.exe",
      "hash": "abc123"
    },
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z"
  }
]
```

### Get Threat

```http
GET /threats/{threat_id}
```

### Create Threat

```http
POST /threats
Content-Type: application/json

{
  "title": "New Threat",
  "description": "Threat description",
  "severity": "HIGH",
  "threat_type": "malware",
  "source": "endpoint",
  "indicators": {}
}
```

### Update Threat

```http
PUT /threats/{threat_id}
Content-Type: application/json

{
  "severity": "CRITICAL"
}
```

### Delete Threat

```http
DELETE /threats/{threat_id}
```

## Alerts

### List Alerts

```http
GET /alerts?skip=0&limit=10
```

### Get Alert

```http
GET /alerts/{alert_id}
```

### Create Alert

```http
POST /alerts
Content-Type: application/json

{
  "title": "Alert Title",
  "description": "Alert description",
  "severity": "HIGH",
  "threat_id": "threat-123",
  "source": "detection",
  "data": {}
}
```

### Update Alert

```http
PUT /alerts/{alert_id}
Content-Type: application/json

{
  "status": "investigating"
}
```

### Delete Alert

```http
DELETE /alerts/{alert_id}
```

## Incidents

### List Incidents

```http
GET /incidents?skip=0&limit=10
```

### Get Incident

```http
GET /incidents/{incident_id}
```

### Create Incident

```http
POST /incidents
Content-Type: application/json

{
  "title": "Incident Title",
  "description": "Incident description",
  "severity": "CRITICAL",
  "affected_assets": ["server1", "server2"]
}
```

### Update Incident

```http
PUT /incidents/{incident_id}
Content-Type: application/json

{
  "status": "investigating"
}
```

### Delete Incident

```http
DELETE /incidents/{incident_id}
```

## Error Responses

### 404 Not Found

```json
{
  "detail": "Threat not found"
}
```

### 422 Validation Error

```json
{
  "detail": [
    {
      "loc": ["body", "title"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

### 500 Server Error

```json
{
  "detail": "Internal server error"
}
```

## Rate Limiting

Rate limiting can be configured in production. Default limits:
- 100 requests per minute per IP
- 1000 requests per hour per IP

## Pagination

All list endpoints support pagination:

- `skip`: Number of items to skip (default: 0)
- `limit`: Number of items to return (default: 10, max: 100)

## Severity Levels

- `CRITICAL`: Immediate action required
- `HIGH`: Urgent action required
- `MEDIUM`: Action required soon
- `LOW`: Action can be deferred

## Status Values

### Alerts
- `open`: New alert, not yet investigated
- `investigating`: Alert being investigated
- `resolved`: Alert has been resolved

### Incidents
- `open`: New incident, not yet investigated
- `investigating`: Incident being investigated
- `resolved`: Incident has been contained
- `closed`: Incident is closed
