# Java Platform Design Specification

## Architecture
- **Language:** Java 17
- **Framework:** Spring Boot 3.2
- **Data Access:** Spring Data JPA / Hibernate
- **Database:** MySQL 8
- **Build Tool:** Maven

## Core Entities
The system uses JPA `@Entity` classes to map to MySQL tables:
- `Role`, `User`
- `Company`, `Branch`, `Department`
- `Bank`, `BankAccount`
- `ImportBatch`, `BankTransaction`, `SourceTransaction`
- `ReconciliationGroup`, `ReconciliationItem`, `ApprovalWorkflow`

## Core Services
- **TransactionService:** Contains business logic for auto-matching (`autoMatchTransactions`). It queries `BankTransactionRepository` for unmatched records and attempts to match them against `SourceTransactionRepository` using `amount` and `transactionType` and an exact match on `rrn` to `utr`.

## API Layer
- `@RestController` classes mapped to `/api/core/...` and `/api/transactions/...` handle HTTP requests and serialize responses to JSON.
