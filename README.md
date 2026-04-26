# SkillSwap
SkillSWap is a peer skill-exchange platform built as a FastAPO microservices backend

## Services
- Identity & Profile Service
- Session Service
- Notification Service
- Nginx API Gateway
- PostgresSQL

### Sprint 1 - Foundations
- Repository scaffolded
- Dockerfiles added
- docker-compose added
- PostgreSQL configured
- Health endpoints created
- Core models and schemas started
- Base CRUD endpoints added

## Run
```bash
docker compose up --build
```

## Health Checks
Identity: http://localhost:8001/health
Session: http://localhost:8002/health
Notification: http://localhost:8003/health