# Lab 5 - Static Code Analysis

## Objective
To enhance Python code quality, security, and style using static analysis tools (Pylint, Bandit, and Flake8).

---

## Known Issues Table

| Issue | Type | Line(s) | Description | Fix Approach |
|--------|------|---------|--------------|---------------|
| Mutable default arg `logs=[]` | Bug | 8 | Shared list across function calls | Use `logs=None` and initialize inside function |
| Bare `except:` | Bad practice | 19 | Exception caught silently | Replace with `except KeyError as e:` |
| Insecure `eval()` | Security | 59 | Allows code execution | Removed `eval`, no unsafe code |
| Open file without `with` | Resource handling | 26, 32 | File not safely closed | Used `with open(..., encoding='utf-8') as f:` |
| Missing docstrings | Style | Multiple | Functions lacked documentation | Added docstrings for all functions |
| Function naming not `snake_case` | Style | Multiple | Used CamelCase | Renamed to follow PEP 8 (e.g., `add_item`) |

---

## Reflection

**1. Which issues were easiest/hardest to fix?**  
Easiest were adding docstrings and formatting fixes. Hardest were removing mutable default arguments and refactoring functions while keeping behavior consistent.

**2. Did the tools show any false positives?**  
Flake8 sometimes flagged harmless blank-line issues that didn’t affect logic.

**3. How could static analysis be integrated into workflow?**  
These tools can be added as part of CI/CD (e.g., GitHub Actions or pre-commit hooks) to automatically analyze code on every commit.

**4. What improvements were observed?**  
- Code became cleaner and consistent with PEP 8  
- Security issues (like `eval`) were eliminated  
- File handling became safer  
- Pylint score improved from **4.6/10** → **9.83/10**

---

## Deliverables
The repository includes:
- `inventory_system.py` (original code)
- `cleaned_inventory_system.py` (fixed version)
- `pylint_report.txt`, `bandit_report.txt`, `flake8_report.txt`
- `README.md`
