# SkillSwap

SkillSwap is a microservices-based platform where users can create profiles, request skill-sharing sessions, and receive notifications.

The project was built using FastAPI, PostgreSQL, Docker Compose, Nginx, JWT authentication, TOTP MFA, pytest, and GitHub Actions.

---

# Project Overview

The platform allows users to:

* register and authenticate
* enable MFA using TOTP
* create public skill profiles
* request mentoring or skill-sharing sessions
* receive notifications related to sessions

The system is split into multiple services to simulate a production-style backend architecture.

---

# Architecture Summary

The system uses a microservices architecture.

Services:

* Identity & Profile Service
* Session Service
* Notification Service
* Nginx API Gateway
* PostgreSQL databases

Each service has its own database and responsibilities.

Communication happens over REST APIs inside the Docker network.

---

# Service Boundaries

## Identity & Profile Service

Responsible for:

* authentication
* JWT generation
* MFA
* user accounts
* skill profiles

Database:

* identity_db

---

## Session Service

Responsible for:

* session requests
* session status updates
* mentor/student session management

Database:

* sessions_db

---

## Notification Service

Responsible for:

* storing notifications
* retrieving notifications

Database:

* notifications_db

---

# Authentication Flow

Authentication uses JWT tokens.

Flow:

1. User registers
2. Password is hashed using bcrypt
3. User logs in
4. JWT access token is generated
5. Frontend sends JWT in Authorization header
6. Protected routes validate the token

Example header:

```text
Authorization: Bearer <token>
```

---

# How TOTP MFA Works

TOTP MFA is implemented using pyotp.

Flow:

1. User requests MFA setup
2. Secret key is generated
3. QR code / secret is provided
4. User scans with authenticator app
5. User submits verification code
6. MFA becomes enabled

Supported apps:

* Google Authenticator
* Authy
* Microsoft Authenticator

---

# Request ID Propagation

Each request can include a request ID header for tracing across services.

Example:

```text
X-Request-ID
```

This allows easier debugging and request tracking across microservices.

---

# Running With Docker Compose

## Start project

```bash
docker compose down -v
docker compose up --build
```

## Stop project

```bash
docker compose down
```

---

# API Route Summary

## Identity & Profile Service

```text
POST /api/v1/auth/register
POST /api/v1/auth/login
GET  /api/v1/auth/me

POST /api/v1/mfa/setup
POST /api/v1/mfa/verify
POST /api/v1/mfa/disable

POST /api/v1/profiles
GET  /api/v1/profiles
```

---

## Session Service

```text
POST  /api/v1/sessions
GET   /api/v1/sessions
PATCH /api/v1/sessions/{id}/status
```

---

## Notification Service

```text
GET /api/v1/notifications/profile/{profile_id}
```

---

# Nginx Routing Summary

Nginx acts as the API gateway.

Routing:

```text
/api/v1/auth/*           -> identity-profile-service
/api/v1/profiles/*       -> identity-profile-service
/api/v1/mfa/*            -> identity-profile-service

/api/v1/sessions/*       -> session-service

/api/v1/notifications/*  -> notification-service
```

Gateway URL:

```text
http://localhost:8080
```

---

# Testing Instructions

Tests use pytest.

Run tests from inside each service directory.

Example:

```bash
PYTHONPATH=. DATABASE_URL=sqlite:///./test.db python -m pytest
```

Services tested:

* authentication
* protected routes
* session routes
* notification routes

---

# CI/CD Summary

GitHub Actions is used for CI.

Pipeline automatically:

* installs dependencies
* runs pytest
* validates pull requests
* validates pushes to feature branches and main

Workflow file:

```text
.github/workflows/ci.yml
```

---

# Known Limitations

* No frontend application yet
* No async message broker
* No distributed tracing system
* No production deployment configuration
* No refresh token flow
* Limited test coverage
* No Kubernetes deployment
