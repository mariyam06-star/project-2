📌 DevSecOps – Week 1 & Week 2 Implementation (SAST)
🔷 Project Overview

This project demonstrates the implementation of DevSecOps principles by integrating Static Application Security Testing (SAST) into the development lifecycle using SonarQube.

The objective was to:

Develop a simple Python application

Intentionally inject a security vulnerability

Detect it using automated static code analysis

Enforce security through Quality Gates

Fix the vulnerability

Re-validate secure code

🗓 Week 1 – Setup & Vulnerability Detection
✅ 1. Environment Setup

Installed and configured Docker

Deployed SonarQube using Docker container

Configured Sonar Scanner

Generated authentication token

✅ 2. Application Development

Created a simple Python login system using SQLite database.

❌ 3. Injected SQL Injection Vulnerability

Introduced a vulnerable query using string concatenation:

query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
cursor.execute(query)

This allowed SQL Injection attacks.
🔍 4. Static Code Analysis (SAST)

Executed sonar-scanner

SonarQube detected:

SQL Injection vulnerability

Security Rating downgraded

Vulnerability count increased

This demonstrated successful automated vulnerability detection.

🗓 Week 2 – Security Fix & Quality Gate Enforcement
🔒 1. Vulnerability Remediation

Replaced unsafe query with parameterized query:

query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))

This prevents SQL Injection by separating code from user input.
🚨 2. Quality Gate Configuration

Configured SonarQube Quality Gate policy:

Condition: Vulnerabilities > 0 → FAIL

This ensures insecure code cannot pass the pipeline.

🔁 3. Demonstration of Security Enforcement
Step A – Re-injected vulnerability

Result:

Quality Gate FAILED

Security issue detected

Step B – Fixed vulnerability

Result:

Vulnerabilities: 0

Security Rating: A

Quality Gate PASSED

This demonstrates automated security validation in a DevSecOps workflow.

🔄 DevSecOps Workflow Implemented
Code Development
↓
Vulnerability Injection
↓
SAST Scan (SonarQube)
↓
Quality Gate Decision
↓
Fix & Re-Scan
↓
Secure Approval

🎯 Key Outcomes

Implemented Static Application Security Testing (SAST)

Demonstrated SQL Injection detection

Configured automated Quality Gate enforcement

Applied secure coding best practices

Validated remediation through re-scanning
🛠 Tools Used

SonarQube

Docker

Python

SQLite

Sonar Scanner

📌 Conclusion

This two-week implementation successfully demonstrates how DevSecOps integrates security into the development lifecycle by detecting vulnerabilities early, blocking insecure builds, and ensuring only secure code progresses forward.
