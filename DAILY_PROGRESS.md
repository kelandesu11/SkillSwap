
### `DAILY_PROGRESS.md`
## Date: 2026-04-24
### Goal for today
- Set up Sprint 1 foundations for SkillSwap
- Scaffold the repository, containers, and base services

### What I completed
- Created the monorepo structure
- Added Dockerfiles for all three services
- Added docker-compose with postgres and nginx
- Added initial FastAPI apps for identity, session, and notification services
- Added /health endpoint for each service

### Services touched
- identity-profile-service
- session-service
- notification-service
- nginx

### Endpoints completed
- GET /health in identity-profile-service
- GET /health in session-service
- GET /health in notification-service

### Gateway / auth / integration completed
- Added initial nginx scaffold
- Added base routing placeholders for api/v1 paths

### Testing / CI completed
- None yet

### Blockers
- Separate service databases are referenced but not yet created automatically

### Next step
- Add DB initialization and basic models for identity, notification, and session services


## Date: 2026-04-26

### Goal for today
- Complete Sprint 1 core models and endpoints
- Fix Docker and database startup issues

### What I completed
- Added profile, session, and notification models
- Added schemas and CRUD endpoints
- Added postgres init script for separate databases
- Fixed Docker dependency startup timing
- Fixed identity service database name mismatch
- Updated README documentation

### Services touched
- identity-profile-service
- session-service
- notification-service
- postgres
- nginx

### Endpoints completed
- POST /api/v1/profiles
- GET /api/v1/profiles
- GET /api/v1/profiles/{id}
- PATCH /api/v1/profiles/{id}

- POST /api/v1/sessions
- GET /api/v1/sessions
- GET /api/v1/sessions/{id}
- PATCH /api/v1/sessions/{id}/status

- POST /api/v1/notifications
- GET /api/v1/notifications
- GET /api/v1/notifications/profile/{profile_id}

### Gateway / auth / integration completed
- Nginx foundation added
- Service startup dependencies improved

### Testing / CI completed
- Manual container startup validation

### Blockers
- None currently

### Next step
- Begin Sprint 2 authentication and JWT setup


## Date: 2026-05-01

### Goal for today
- Start Sprint 3 testing and CI/CD work
- Add pytest coverage and GitHub Actions workflow

### What I completed
- Added pytest setup for services
- Added auth tests for register, login, and current user flow
- Added session route protection tests
- Added notification route protection tests
- Added GitHub Actions CI workflow
- Fixed PYTHONPATH issue in GitHub Actions
- Configured CI to use SQLite test database
- Fixed missing config defaults for session service tests
- Updated bcrypt dependency compatibility for auth tests

### Services touched
- identity-profile-service
- session-service
- notification-service
- GitHub Actions

### Endpoints completed
- Tested POST /api/v1/auth/register
- Tested POST /api/v1/auth/login
- Tested GET /api/v1/auth/me
- Tested protected session routes
- Tested protected notification routes

### Gateway / auth / integration completed
- No new gateway changes
- Auth test coverage added
- Protected route test coverage added

### Testing / CI completed
- Added pytest
- Added CI workflow
- Added service test matrix
- Added SQLite database override for CI tests
- Fixed CI dependency and import issues

### Blockers
- None currently

### Next step
- Confirm GitHub Actions passes
- Finish Sprint 3 PR review and merge