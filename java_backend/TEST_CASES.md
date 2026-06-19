# QA Test Cases

The quality assurance test cases for the Java backend are implemented using **JUnit 5** and **Spring Boot Test**.

## Where to find them
The test files are located in the `src/test/java/com/bankrecon/` directory:
1. `CompanyControllerTests.java`: Uses `MockMvc` to test REST endpoint creation and JSON serialization.
2. `TransactionServiceTests.java`: Uses an in-memory **H2 database** to seed mock transactions, execute the `autoMatchTransactions()` service layer logic, and assert that the database state reflects matched statuses and creates reconciliation groups.

## How to run them
To execute the test suite, ensure you have Maven installed and run the following command from the root of the `java_backend` directory:

```bash
mvn test
```
