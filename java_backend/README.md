# Java Spring Boot Bank Reconciliation Platform

This is the Java/Spring Boot translation of the Bank Reconciliation Platform.

## Features
- **Transaction Matching:** API logic to automatically match Bank Transactions against Source Transactions.
- **REST APIs:** Spring Web REST controllers for Company and Transaction management.
- **Data Persistence:** Spring Data JPA with MySQL 8.

## Installation & Running (Docker)

1. Make sure you have Docker and Docker Compose installed.
2. Navigate to the `java_backend` directory:
   ```bash
   cd java_backend
   ```
3. Run docker compose to build the Java app and spin up MySQL:
   ```bash
   docker-compose up --build -d
   ```
4. Access the REST APIs at `http://localhost:8080/api/...`

## Documentation
- Read `DESIGN.md` for architectural specifications.
- Read `TEST_CASES.md` for QA testing details.
