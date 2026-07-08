# Setup Guide

## Prerequisites

- Docker & Docker Compose
- Python 3.11+ (for local development)
- Node.js 18+ (for frontend development)
- PostgreSQL 13+
- Redis 7+

## Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Woyz01/xdr-project.git
cd xdr-project
```

### 2. Setup Environment Variables

```bash
cp .env.example .env
cd frontend && cp .env.example .env && cd ..
```

Edit `.env` and `frontend/.env` as needed for your environment.

### 3. Install Dependencies

```bash
make install
```

Or manually:

```bash
cd backend && pip install -r requirements.txt
cd ../frontend && npm install
```

### 4. Start Services

```bash
make run
```

Or using Docker Compose:

```bash
docker-compose up -d
```

### 5. Access the Application

- Frontend: http://localhost:3000
- API Docs: http://localhost:8000/docs
- Database: localhost:5432
- Redis: localhost:6379

## Database Setup

### Create Tables

The tables are automatically created using SQLAlchemy models on first run.

```bash
cd backend
alembic upgrade head
```

### Seed Test Data

```bash
python -c "from core.database import Base, engine; Base.metadata.create_all(bind=engine)"
```

## Running Tests

### Backend Tests

```bash
cd backend
pytest
```

### Frontend Tests

```bash
cd frontend
npm test
```

### All Tests

```bash
make test
```

## Development Workflow

### Backend Development

```bash
cd backend
# Run with auto-reload
uvicorn main:app --reload

# Run linting
pylint core/ api/ models/ agents/

# Format code
black core/ api/ models/ agents/
```

### Frontend Development

```bash
cd frontend
# Start dev server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## Debugging

### View Logs

```bash
# All services
make logs

# Specific service
make logs-backend
make logs-frontend
```

### Database Connection

```bash
# Connect to PostgreSQL
psql -h localhost -U xdr_user -d xdr_db

# Connect to Redis
redis-cli -h localhost -p 6379
```

## Troubleshooting

### Port Already in Use

```bash
# Find and kill process using port
lsof -ti:8000 | xargs kill -9
lsof -ti:3000 | xargs kill -9
lsof -ti:5432 | xargs kill -9
```

### Database Connection Issues

```bash
# Check database is running
docker-compose ps

# View database logs
docker-compose logs postgres
```

### Build Issues

```bash
# Clean and rebuild
make clean
make install
make run
```

## Production Deployment

### Using Docker

```bash
# Build images
docker-compose build

# Start services
docker-compose up -d
```

### Using Kubernetes

See `k8s/` directory for Kubernetes manifests.

```bash
kubectl apply -f k8s/
```

## Next Steps

- Read [Architecture Documentation](./ARCHITECTURE.md)
- Explore [API Documentation](http://localhost:8000/docs)
- Check [Contributing Guide](../CONTRIBUTING.md)
