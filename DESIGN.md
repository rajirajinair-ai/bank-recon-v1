# Bank Reconciliation Platform - Architecture Document

This platform features two distinct backend implementations located in this repository.

## 1. Java Architecture (Located in `java_backend/`)

**Backend Layer**
- **Technology:** Java 17, Spring Boot 3, Spring Web, Spring Security
- **Responsibilities:** Authentication, Reconciliation processing, Business rules, Workflow management, Reporting

**Processing Layer**
- **Technology:** Spring Async, Spring Scheduled Tasks
- **Responsibilities:** File processing, Matching jobs, Scheduled jobs, Report generation

**Database Layer**
- **Technology:** MySQL 8, Spring Data JPA, Hibernate
- **Responsibilities:** Transaction storage, Audit trail, Workflow state, Reporting

---

## 2. Python Architecture (Located in root `/`)

**Frontend Layer**
- **Technology:** Django Templates, HTMX, Bootstrap 5
- **Responsibilities:** Dashboard, Import screens, Reconciliation screens, Reports, Administration

**Backend Layer**
- **Technology:** Python 3.12, Django 4.2, Django REST Framework
- **Responsibilities:** Authentication, Reconciliation processing, Business rules, Workflow management, Reporting

**Processing Layer**
- **Technology:** Celery, Redis
- **Responsibilities:** File processing, Matching jobs, Scheduled jobs, Report generation

**Database Layer**
- **Technology:** MySQL 8
- **Responsibilities:** Transaction storage, Audit trail, Workflow state, Reporting

---

## Functional Modules (Shared Across Implementations)

**Matching Engine**
- **Supported Matching:**
  - *One-to-One:* Invoice <-> Receipt
  - *One-to-Many:* Single Bank Entry <-> Multiple Ledger Entries
  - *Many-to-One:* Multiple Receipts <-> Single Settlement
  - *Many-to-Many:* Settlement Group <-> Ledger Group
- **Matching Criteria:** Reference Number, UTR, RRN, Amount, Date, Settlement ID

**Approval Workflow & Audit Trail**
- **States:** Draft, Prepared, Reviewed, Approved
- **Actions:** Approve, Reject, Send Back
- **Audit Track:** Login, Imports, Matches, Reversals, Approvals, Configuration Changes (Immutable records).
