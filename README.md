# SkillSwap
SkillSWap is a peer skill-exchange platform built as a FastAPO microservices backend

## Services
- Identity & Profile Service
- Session Service
- Notification Service
- Nginx API Gateway
- PostgresSQL

## Sprint 1 status
Sprint 1 sets up the service foundations:
- repository scaffold
- Dockerfiles
- docker-compose
- PostgresSQL
- helath endpoints
- intital service structure

## Run
```bash
docker compose up --build
```

## Health Checks
Identity: http://localhost:8001/health
Session: http://localhost:8002/health
Notification: http://localhost:8003/health