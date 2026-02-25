📘 DevSecOps Project Report
👩‍💻 Name: Mariyam Sidat
🏢 Company: Infotect Solution
📂 Project Title: Secure Flask Application with DevSecOps CI/CD Pipeline
🛠 Technologies Used: Python, Flask, GitHub Actions, OWASP ZAP
Duration: 4 Weeks

WEEK 1 – Project Setup & Environment Configuration

🎯 Objective
To understand DevOps fundamentals and set up the development environment for building a secure web application.

🛠 Work Completed
Installed Python and required dependencies
Installed Flask framework
Created basic project structure
Initialized Git repository
Created GitHub repository
Pushed initial project code to GitHub

📂 Project Structure
project-2/
│
├── app.py
└── README.md

📚 Learning Outcomes
Basics of DevOps lifecycle
Git & GitHub version control
Python virtual environment setup
Project structuring best practices

WEEK 2 – Application Development & Basic Security

🎯 Objective
To develop a working Flask application and understand common web vulnerabilities.

🛠 Work Completed
Developed a simple Flask web application
Implemented dynamic routing with query parameters
Tested application locally
Studied common web vulnerabilities:
SQL Injection
Cross-Site Scripting (XSS)
Clickjacking

💻 Sample Application Code
from flask import Flask, request
app = Flask(__name__)
@app.route("/")
def home():
    name = request.args.get("name", "Guest")
    return f"<h1>Hello {name}</h1>"
 if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

    🔐 SQL Injection Understanding
SQL Injection occurs when user input is directly inserted into SQL queries without validation.

Example of vulnerable query:
SELECT * FROM users WHERE username = 'admin' OR '1'='1';

Impact:
Unauthorized data access
Data leakage
Authentication bypass

📚 Learning Outcomes
Web application fundamentals
Security vulnerability awareness
Importance of input validation
Secure coding basics

WEEK 3 – CI Pipeline Implementation (DevOps)

🎯 Objective
To implement Continuous Integration using GitHub Actions.

🛠 Work Completed
Created GitHub Actions workflow
Automated dependency installation
Automated application startup
Triggered workflow on push events
Debugged YAML configuration errors

📄 Workflow File Location :
.github/workflows/security.yml

 ⚙ CI Workflow Example :
 name: DevSecOps Security Pipeline
 on:
  push:
    branches: [ main ]
  jobs:
   security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: pip install flask
      - run: nohup python app.py &

🚀 Achievements
  Automatic pipeline execution on every push
  Hands-on experience with YAML configuration
  Understood CI automation process

📚 Learning Outcomes
Continuous Integration (CI)
GitHub Actions
Workflow debugging
Build automation

WEEK 4 – DevSecOps & Security Automation

🎯 Objective
To integrate security into the CI pipeline (DevSecOps approach).

🛠 Work Completed
Added security headers to Flask application
Integrated OWASP ZAP for automated DAST scanning
Removed deprecated Docker-based scanning
Resolved pipeline conflicts
Achieved successful green security pipeline

🔐 Security Headers Implemented :
@app.after_request
def set_security_headers(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['Strict-Transport-Security'] = 'max-age=63072000; includeSubDomains'
    return response

Security Improvements:
 Prevents XSS attacks
 Prevents MIME-type sniffing
 Prevents Clickjacking
 Enforces HTTPS policy

🔎 DAST Implementation
Used OWASP ZAP GitHub Action:
- name: OWASP ZAP Baseline Scan
  uses: zaproxy/action-baseline@v0.10.0
  with:
    target: 'http://localhost:5000'
    fail_action: false

  🚨 Issues Faced & Solutions
        Issue	                              Solution
     Exit code 125	                     Removed outdated Docker image
     Port mismatch	                     Corrected to port 5000
     Multiple workflow files             Deleted duplicate main.yml
     Pipeline failure                    Simplified workflow

🏆 Final Outcome
✅ Fully automated CI/CD pipeline
✅ Security scanning integrated
✅ Secure Flask application
✅ Successful DevSecOps implementation
✅ Green GitHub Actions pipeline

🎯 Conclusion

This project demonstrates the successful implementation of DevOps and DevSecOps practices in a real-world development environment, 
By integrating automated security testing within the CI pipeline, vulnerabilities can be detected early, ensuring secure and reliable software delivery.

The project reflects practical understanding of:
Continuous Integration
Security Automation
Web Application Security
Secure Development Lifecycle
