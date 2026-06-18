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
- **Database Layer:** MySQL 8

## Installation Prerequisites (Docker)
This application uses Docker and Docker Compose to containerize the development and production environments.

### 1. Install Docker
Before starting the application, you must install Docker on your machine.
- **Windows:** Download and install [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/). Ensure WSL2 is enabled if prompted.
- **macOS:** Download and install [Docker Desktop for Mac](https://docs.docker.com/desktop/install/mac-install/).
- **Linux (Ubuntu/Debian):** Run the following commands:
  ```bash
  sudo apt-get update
  sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
  ```
  *(For other Linux distributions, refer to the [official Docker documentation](https://docs.docker.com/engine/install/))*

### 2. Install Docker Compose
If you installed Docker Desktop (Windows/Mac), Docker Compose is already included.
For Linux users, verify installation by running:
```bash
docker compose version
```
If it is not installed, follow the [Docker Compose installation guide](https://docs.docker.com/compose/install/).

## Quickstart Setup
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd bank-recon-platform
   ```
2. Set up your environment variables by copying the example file:
   ```bash
   cp .env.example .env
   ```
3. Build and start the Docker containers:
   ```bash
   docker-compose up --build -d
   ```
4. Run the database migrations inside the web container:
   ```bash
   docker-compose exec web python manage.py migrate
   ```
5. Access the application:
   - Web Dashboard: `http://localhost:8000`
   - API Endpoints: `http://localhost:8000/api/...`

## Architecture Details
- `/accounts`: Custom User, Roles, Permissions.
- `/core`: Company, Bank, Bank Account, Department branches setup.
- `/transactions`: Bank transactions, source transactions, and reconciliation tracking.
- `/workflows`: Manages the state and transition of reconciliation approval queues.
- `/reports`: Generating reports, system settings, auditing, and interest calculation entries.
