# Bank Reconciliation Platform

A highly configurable bank reconciliation platform designed to automate and streamline financial matching.

## Two Implementations
This repository contains **two complete backend implementations**:
1. **Python/Django Backend:** Located in the root directory.
2. **Java/Spring Boot Backend:** Located in the `java_backend/` directory.

---

## 1. Java / Spring Boot Backend (New)
The Java backend aims to replicate the functionality of the Python implementation.

### Tech Stack
- **Frontend Layer:** Thymeleaf Templates, HTMX, Bootstrap 5
- **Backend Layer:** Java 17, Spring Boot 3, Spring Web, Spring Data JPA, Spring Security
- **Processing Layer:** Spring Async, Spring Scheduled Tasks
- **Database Layer:** MySQL 8

### Quickstart Setup (Java)
1. Navigate to the java directory:
   ```bash
   cd java_backend
   ```
2. Build and start the Docker containers:
   ```bash
   docker-compose up --build -d
   ```
3. Run the automated QA tests:
   ```bash
   mvn test
   ```

---

## 2. Python / Django Backend (Legacy)

### Tech Stack
- **Frontend Layer:** Django Templates, HTMX, Bootstrap 5
- **Backend Layer:** Python 3.12, Django 4.2, Django REST Framework
- **Processing Layer:** Celery, Redis
- **Database Layer:** MySQL 8

### Quickstart Setup (Python)
1. Set up your environment variables by copying the example file:
   ```bash
   cp .env.example .env
   ```
2. Build and start the Docker containers:
   ```bash
   docker-compose up --build -d
   ```
3. Run the database migrations inside the web container:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

## Installation Prerequisites (Docker)
This application uses Docker and Docker Compose to containerize both development environments.

### 1. Install Docker
Before starting either application, you must install Docker on your machine.
- **Windows:** Download and install [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/). Ensure WSL2 is enabled if prompted.
- **macOS:** Download and install [Docker Desktop for Mac](https://docs.docker.com/desktop/install/mac-install/).
- **Linux (Ubuntu/Debian):** Run the following commands:
  ```bash
  sudo apt-get update
  sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
  ```

### 2. Install Docker Compose
For Linux users, verify installation by running:
```bash
docker compose version
```
If it is not installed, follow the [Docker Compose installation guide](https://docs.docker.com/compose/install/).
