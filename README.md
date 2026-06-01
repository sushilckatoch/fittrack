# FitTrack 🏋️

A full-stack personal health & fitness tracking platform built with a microservices architecture.

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Vue.js 3 + TypeScript + Pinia |
| Auth & Core API | NestJS + Prisma + PostgreSQL |
| Admin Panel | Laravel + PostgreSQL |
| AI & ML | FastAPI + Ollama |
| Cache | Redis |
| Gateway | NGINX |
| Infrastructure | Docker + Kubernetes |

## Services

| Service | Port | Description |
|---|---|---|
| Vue Frontend | 5173 | User dashboard and UI |
| NestJS API | 3000 | Auth, workouts, meals |
| Laravel Admin | 8000 | Admin panel, reports |
| FastAPI ML | 8001 | AI meal planner |
| PostgreSQL | 5432 | Main database |
| Redis | 6379 | Cache and sessions |
| NGINX | 8080 | API Gateway |

## Features

- 🔐 JWT Authentication
- 🏋️ Workout Tracker
- 🥗 Diet & Calorie Tracker
- 🤖 AI Meal Planner
- 📊 Progress Analytics
- 👑 Admin Dashboard
- 🐳 Docker + Kubernetes ready

## Getting Started

### Prerequisites
- Docker Desktop
- WSL2 (Windows)
- Node.js 20+
- PHP 8.5+
- Python 3.11+

### Run Locally

```bash
# Clone the repo
git clone https://github.com/sushilckatoch/fittrack.git
cd fittrack

# Start all services
docker compose up --build
```

### Access the app
- Frontend: http://localhost:8080
- API Docs: http://localhost:8080/api/ml/docs

## Project Structure

fittrack/
├── frontend/          # Vue.js app
├── services/
│   ├── auth-api/      # NestJS
│   ├── admin-api/     # Laravel
│   └── ml-api/        # FastAPI
├── nginx/             # API Gateway
├── k8s/               # Kubernetes configs
└── docker-compose.yml
