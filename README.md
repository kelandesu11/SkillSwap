# SkillSwap

SkillSwap is a microservices-based platform where users can create profiles, request skill-sharing sessions, and receive notifications.

The project was built using FastAPI, PostgreSQL, Docker Compose, Nginx, JWT authentication, TOTP MFA, pytest, and GitHub Actions.

---

# Project Overview

The platform allows users to:

- register and authenticate
- enable MFA using TOTP
- create public skill profiles
- request mentoring or skill-sharing sessions
- receive notifications related to sessions

The system is split into multiple services to simulate a production-style backend architecture.

---

# Architecture Summary

The system uses a microservices architecture.

Services:

- Identity & Profile Service
- Session Service
- Notification Service
- Nginx API Gateway
- PostgreSQL databases

Each service has its own database and responsibilities.

Communication happens over REST APIs inside the Docker network.

---

# Service Boundaries

## Identity & Profile Service

Responsible for:

- authentication
- JWT generation
- MFA
- user accounts
- skill profiles

Database:

- identity_db

---

## Session Service

Responsible for:

- session requests
- session status updates
- mentor/student session management

Database:

- sessions_db

---

## Notification Service

Responsible for:

- storing notifications
- retrieving notifications

Database:

- notifications_db

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