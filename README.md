# FitTrack 🏋️

### Full-Stack Personal Health & Fitness Tracking Platform

A scalable, cloud-ready health and fitness tracking platform built using **microservices architecture**, designed for workout management, nutrition tracking, analytics, and AI-powered meal planning.

---

## 🚀 Overview

FitTrack helps users monitor fitness progress through personalized workouts, calorie tracking, analytics dashboards, and AI-driven recommendations.

### Key Highlights

* Microservices Architecture
* Containerized Deployment
* AI-Powered Recommendations
* Kubernetes Ready
* Role-Based Admin System
* Scalable API Gateway Architecture

---

# 🛠 Tech Stack

| Layer            | Technology                  |
| ---------------- | --------------------------- |
| Frontend         | Vue.js 3, TypeScript, Pinia |
| Backend APIs     | NestJS, Prisma              |
| Admin Panel      | Laravel                     |
| AI / ML Services | FastAPI, Ollama             |
| Database         | PostgreSQL                  |
| Cache Layer      | Redis                       |
| API Gateway      | NGINX                       |
| Infrastructure   | Docker, Kubernetes          |

---

# ⚙️ Microservices

| Service         | Port | Responsibility                  |
| --------------- | ---- | ------------------------------- |
| Frontend App    | 5173 | User Dashboard & UI             |
| Auth/Core API   | 3000 | Authentication, Workouts, Meals |
| Admin Dashboard | 8000 | Reports, Management             |
| AI Service      | 8001 | Meal Planning & Predictions     |
| PostgreSQL      | 5432 | Persistent Storage              |
| Redis           | 6379 | Cache & Session Store           |
| NGINX Gateway   | 8080 | Reverse Proxy & Routing         |

---

# ✨ Features

## Authentication & Security

* JWT Authentication
* Secure API Gateway
* Role-Based Access Control

## Fitness Management

* Workout Tracking
* Exercise Logging
* Progress Monitoring

## Nutrition

* Diet Tracking
* Calorie Management
* AI Meal Recommendations

## Analytics

* Progress Charts
* Performance Metrics
* Historical Reports

## Infrastructure

* Dockerized Services
* Kubernetes Ready
* Horizontal Scaling Support

---

# 📦 Project Structure

```text
fittrack/
│
├── frontend/                 # Vue.js Frontend
│
├── services/
│   ├── auth-api/             # NestJS API
│   ├── admin-api/            # Laravel Admin
│   └── ml-api/               # FastAPI ML Service
│
├── nginx/                    # API Gateway Config
├── k8s/                      # Kubernetes Manifests
├── docs/                     # Documentation
├── docker-compose.yml
└── README.md
```

---

# 🚀 Quick Start

## Prerequisites

* Docker Desktop
* WSL2 (Windows)
* Node.js 20+
* PHP 8.5+
* Python 3.11+

## Installation

```bash
git clone https://github.com/sushilckatoch/fittrack.git

cd fittrack

docker compose up --build
```

---

# 🌐 Access Services

| Service     | URL                               |
| ----------- | --------------------------------- |
| Frontend    | http://localhost:8080             |
| API Docs    | http://localhost:8080/api/ml/docs |
| Admin Panel | http://localhost:8000             |

---

# 🐳 Deployment

Supports:

* Docker Compose (Local Development)
* Kubernetes Deployment
* NGINX Reverse Proxy
* Cloud Deployments (AWS / Azure / GCP)

---

# 📈 Future Improvements

* Wearable Device Integration
* Mobile App
* Push Notifications
* Social Features
* Advanced AI Coaching

---

Built with ❤️ using modern microservices architecture.
