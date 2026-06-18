# Bank Reconciliation Platform

A highly configurable bank reconciliation platform designed to automate and streamline financial matching.

## Features
- **Multi-Source Reconciliation:** Reconcile bank statements, UPI, NEFT/RTGS, cards, and payment gateway settlements.
- **Matching Engine:** Supports 1-to-1, 1-to-M, M-to-1, and M-to-M transaction matching.
- **Approval Workflows:** Role-based access control with multi-step approval queues (Draft, Prepared, Reviewed, Approved).
- **Audit Trails:** Comprehensive logging of system events and transaction changes.
- **REST API:** Fully featured API built on Django REST Framework for seamless integrations.

## Tech Stack
- **Frontend Layer:** Django Templates, HTMX, Bootstrap 5
- **Backend Layer:** Python 3.12, Django 4.2, Django REST Framework
- **Processing Layer:** Celery, Redis
- **Database Layer:** PostgreSQL

## Quickstart (Docker)
1. Ensure you have Docker and Docker Compose installed.
2. Clone the repository and navigate into it.
3. Run `docker-compose up --build -d` to build and start the containers.
4. Run migrations inside the web container: `docker-compose exec web python manage.py migrate`
5. Access the app at `http://localhost:8000`.

## Architecture Details
- `/accounts`: Custom User, Roles, Permissions.
- `/core`: Company, Bank, Bank Account, Department branches setup.
- `/transactions`: Bank transactions, source transactions, and reconciliation tracking.
- `/workflows`: Manages the state and transition of reconciliation approval queues.
- `/reports`: Generating reports, system settings, auditing, and interest calculation entries.
