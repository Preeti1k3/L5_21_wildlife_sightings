# Static Code Analysis – Issue Documentation

## Project
Wildlife Sightings

## Tools Used
- Pylint
- Bandit
- Flake8

## Issues Identified

| Issue | Type | Original Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Mutable default argument | Code quality / Bug risk | 8 | The default dictionary `{}` may be shared across function calls. | Replace with `None` and initialize a new dictionary inside the function. |
| Potential SQL injection | Security | 9 | User-provided values are inserted directly into the SQL query. | Use parameterized SQL queries with placeholders. |
| Weak MD5 hash | Security | 15 | MD5 is unsuitable for security-sensitive hashing. | Replace MD5 with SHA-256, while retaining the required identifier behavior where appropriate. |
| Assert statement | Code quality / Security finding | 36 | Assertions can be disabled when Python runs with optimization. | Replace the assertion with an explicit conditional check. |
| Incorrect function naming | Code style | 8, 14, 18 | Function names do not follow Python's snake_case convention. | Rename functions using snake_case. |
| Long lines | Formatting | 5, 9, 19, 27 | Several lines exceed the recommended line length. | Split long expressions across multiple lines. |
| Ambiguous variable name | Formatting / Readability | 28 | The variable `l` is difficult to distinguish from the number `1`. | Rename it to a descriptive name such as `rarest_sighting`. |
| Missing docstrings | Code quality | 1, 8, 14, 18, 26, 32 | The module and functions lack descriptive documentation. | Add module and function docstrings. |

## Conclusion

Pylint, Bandit, and Flake8 identified code quality, security, and formatting issues in the original program. The identified issues will be addressed, and the tools will be run again to verify the improvements.