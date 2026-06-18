# Bank Reconciliation Platform - Complete Design Document (V1)

## 1. Objective

Develop a configurable bank reconciliation platform capable of reconciling:
- Bank statements
- UPI transactions
- NEFT/RTGS/IMPS transactions
- Debit card transactions
- Credit card transactions
- Payment gateway settlements
- Payroll payments
- Vendor payments
- Customer receipts
- Bank interest
- TDS deductions
- Bank charges

The platform should support:
- Automated matching
- Manual reconciliation
- Approval workflows
- Audit trails
- Multi-company support
- Multi-bank support
- Multi-currency support

## 2. Architecture

**Frontend Layer**
- **Technology:** Django Templates, HTMX, Bootstrap 5
- **Responsibilities:** Dashboard, Import screens, Reconciliation screens, Reports, Administration

**Backend Layer**
- **Technology:** Django, Django REST Framework
- **Responsibilities:** Authentication, Reconciliation processing, Business rules, Workflow management, Reporting

**Processing Layer**
- **Technology:** Celery, Redis
- **Responsibilities:** File processing, Matching jobs, Scheduled jobs, Report generation

**Database Layer**
- **Technology:** MySQL 8
- **Responsibilities:** Transaction storage, Audit trail, Workflow state, Reporting

## 3. Functional Modules

**Authentication & Security**
- **Features:** Login, Logout, Password reset, Session management
- **Roles:** Administrator, Reconciliation User, Reviewer, Approver, Auditor

**Company Management**
- **Manage:** Companies, Branches, Departments
- **Fields:** Company Code, Company Name, GST Number, PAN Number, Currency

**Bank Management**
- **Manage:** Banks, Bank Accounts
- **Fields:** Account Number, Account Type, Currency, Opening Balance

**Statement Import**
- **Supported Formats:** CSV, XLSX, MT940
- **Validation:** Duplicate file detection, Mandatory field validation, Format validation
- **Process:** Upload -> Validation -> Staging -> Transaction Creation -> Audit Logging

**Transaction Repository**
- Store all normalized transactions.
- **Sources:** BANK, UPI, CARD, PAYROLL, AP, AR, TAX, GATEWAY

**Matching Engine**
- **Supported Matching:**
  - *One-to-One:* Invoice <-> Receipt
  - *One-to-Many:* Single Bank Entry <-> Multiple Ledger Entries
  - *Many-to-One:* Multiple Receipts <-> Single Settlement
  - *Many-to-Many:* Settlement Group <-> Ledger Group
- **Matching Criteria:** Reference Number, UTR, RRN, Amount, Date, Settlement ID

**UPI & Gateway Reconciliation**
- **Capture:** UPI ID, RRN, Payer Name, Amount
- **Gateway Supported:** Razorpay, Cashfree, Stripe, PayU (Gross Amount, Gateway Fee, GST, Net Settlement)

**Payroll & Vendor Payment Reconciliation**
- **Support:** Salary Batch, Salary Payment File, Bank Debit Matching, Bulk Vendor Payments, NEFT/RTGS Runs

**Interest, TDS & GST Reconciliation**
- **Support:** Savings/FD Interest, TDS on Interest, Customer TDS, GST on Gateway/Bank Charges.

**Approval Workflow & Audit Trail**
- **States:** Draft, Prepared, Reviewed, Approved
- **Actions:** Approve, Reject, Send Back
- **Audit Track:** Login, Imports, Matches, Reversals, Approvals, Configuration Changes (Immutable records).

## 4. Database Design (Core Tables)

- `users`, `roles`, `permissions`, `role_permissions`
- `companies`, `branches`, `departments`
- `banks`, `bank_accounts`
- `import_batches`
- `bank_transactions`, `source_transactions`
- `reconciliation_groups`, `reconciliation_items`
- `approval_workflows`, `approval_actions`
- `tds_entries`, `interest_entries`
- `audit_logs`, `report_requests`, `system_settings`

## 5. Frontend Screens

- **Dashboard:** Widgets for Total/Matched/Pending Transactions, Match %, Imports Today.
- **Maintenance:** Company and Bank Account creation/editing.
- **Statement Upload:** Upload files, view import status and history.
- **Transaction Browser:** Filters (Date, Bank, Amount, Status, Source), Actions (View, Export).
- **Auto/Manual Match Screen:** Run matching, View results, Grid layouts for Bank vs Source transactions (Match, Split, Merge, Unmatch).
- **Approval Queue:** Pending Approvals, Review, Approve, Reject.
- **Reports:** Bank Recon Statement, Interest/TDS/Charges/Pending Reports.

## 6. REST APIs

- Authentication APIs
- Company APIs
- Bank APIs
- Import APIs
- Transaction APIs
- Matching APIs
- Approval APIs
- Report APIs
- Audit APIs

## 7. Background Jobs

- Import Job
- Auto Matching Job
- Report Generation Job
- Cleanup Job
- Notification Job

## 8. Deployment

- Docker & Docker Compose
- Gunicorn
- Redis
- Celery Workers
- MySQL 8

## 9. Future Roadmap

- **Phase 2:** Exception Management, AI Match Suggestions, Auto Journal Entries
- **Phase 3:** Intercompany Reconciliation, Treasury Management, Advanced Analytics
- **Phase 4:** ML Matching Engine, Predictive Reconciliation, Real-Time Bank APIs
