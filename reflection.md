# Lab 5: Static Code Analysis Reflection

## 1. What is static code analysis?

Static code analysis examines source code without executing the program. It helps identify potential bugs, security vulnerabilities, and style violations.

## 2. What issues were identified?

Pylint identified issues including a mutable default argument, missing docstrings, naming violations, and long lines. Bandit identified a potential SQL injection vulnerability, weak MD5 hashing, and an assert statement. Flake8 identified long lines, an ambiguous variable name, spacing problems, and a missing final newline.

## 3. How were the issues fixed?

The code was updated to use a safe default argument, parameterized SQL queries, SHA-256 hashing, descriptive function and variable names, docstrings, and consistent formatting. The assert statement was replaced with an explicit conditional check.

## 4. How does static analysis improve code quality?

Static analysis helps developers find potential problems early, improve readability, reduce security risks, and maintain consistent coding standards.