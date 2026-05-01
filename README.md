# SkillSwap

SkillSwap is a microservices-based platform where users exchange skills by creating profiles, requesting sessions, and receiving notifications.

---

## Architecture

* Identity & Profile Service → auth, users, profiles, MFA
* Session Service → session requests and status
* Notification Service → notifications
* Nginx → API gateway
* PostgreSQL → separate DB per service

---

## Tech Stack

* FastAPI, SQLAlchemy, PostgreSQL
* Docker & Docker Compose
* Nginx
* JWT Authentication
* TOTP MFA (pyotp)
* httpx (service communication)

---

## Run Project

```bash
docker compose down -v
docker compose up --build
```

Gateway:

```bash
http://localhost:8080
```

---

## Main Endpoints

**Auth / Identity**

```
POST /api/v1/auth/register
POST /api/v1/auth/login
GET  /api/v1/auth/me
```

**Profiles**

```
POST /api/v1/profiles
GET  /api/v1/profiles
```

**Sessions**

```
POST /api/v1/sessions
GET  /api/v1/sessions
PATCH /api/v1/sessions/{id}/status
```

**Notifications**

```
GET /api/v1/notifications/profile/{id}
```

---

## Key Features

* JWT-based authentication
* TOTP MFA support
* Protected service routes
* Service-to-service communication
* Timeout handling
* Request ID propagation across services
* Centralized API gateway

---

## End-to-End Flow

1. User registers and logs in
2. JWT token is issued
3. User creates profiles
4. Session is created
5. Session Service validates profiles
6. Notification is created
7. Same request ID flows across services

---

## Health Checks

```
/health/identity
/health/session
/health/notification
```

---

## Status

* Sprint 1: Complete (setup + core APIs)
* Sprint 2: Complete (auth + integration + gateway)
* Sprint 3: Pending (tests + CI/CD)
