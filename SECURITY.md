# Security Policy

## Supported Versions

We release patches for security vulnerabilities in the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 0.3.x   | :white_check_mark: |
| 0.2.x   | :white_check_mark: |
| < 0.2.0 | :x:                |

## Reporting a Vulnerability

We take security seriously. If you discover a security vulnerability, please follow these steps:

### 1. Do Not Open a Public Issue

Please do not report security vulnerabilities through public GitHub issues.

### 2. Report Privately

Include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

### 3. What to Expect

- **Initial Response**: Within 48 hours
- **Status Update**: Within 7 days with assessment
- **Fix Timeline**: Depends on severity (see below)

### Severity Levels

- **Critical**: Fix within 24-48 hours
- **High**: Fix within 7 days
- **Medium**: Fix within 30 days
- **Low**: Fix in next minor release

## Security Best Practices

When using pytoolkit:

### Configuration Files

- Never commit `.env` files with sensitive data
- Use environment variables for secrets
- Rotate credentials regularly

### HTTP Client

```python
# Good: Use environment variables for API keys
import os
from pytoolkit.http_client import HttpClient

api_key = os.getenv("API_KEY")
client = HttpClient(
    base_url="https://api.example.com",
    default_headers={"Authorization": f"Bearer {api_key}"}
)

# Bad: Hard-coded credentials
# client = HttpClient(default_headers={"Authorization": "Bearer secret123"})
```

### File Operations

```python
# Good: Validate file paths
from pathlib import Path
from pytoolkit.file_utils import read_text

def safe_read(filename: str, base_dir: str = "/safe/directory") -> str:
    path = Path(base_dir) / filename
    path = path.resolve()
    
    # Ensure path is within base_dir (prevent path traversal)
    if not str(path).startswith(str(Path(base_dir).resolve())):
        raise ValueError("Invalid path")
    
    return read_text(str(path))
```

### Cryptographic Functions

```python
# Use appropriate hash algorithms
from pytoolkit.crypto_utils import hash_text, random_token

# For passwords, use a dedicated password hashing library (e.g., bcrypt)
# pytoolkit's hash functions are for general hashing, not password storage

# Good for tokens
token = random_token(length=32)

# Good for file integrity
file_hash = hash_text(content, algorithm="sha256")
```

## Known Security Considerations

### 1. Cache Decorator

The `@cached` decorator uses pickle for serialization. Be aware:
- Only cache trusted data
- Avoid caching user input directly
- Consider custom `key_func` for sensitive data

### 2. HTTP Client

- Always use HTTPS in production
- Verify SSL certificates (default behavior)
- Set appropriate timeouts
- Implement rate limiting for external APIs

### 3. Task Scheduler

- Validate task functions before scheduling
- Catch exceptions in scheduled tasks
- Monitor task execution for anomalies

## Third-Party Dependencies

We regularly update dependencies to patch security vulnerabilities:

- Dependabot monitors our dependencies
- Security updates are prioritized
- Check `CHANGELOG.md` for security-related updates

## Responsible Disclosure

We appreciate security researchers who:
- Give us reasonable time to fix issues before disclosure
- Provide detailed information to help us reproduce and fix
- Do not exploit vulnerabilities maliciously

### Hall of Thanks

We will recognize security researchers who responsibly disclose vulnerabilities (with their permission):

- (Your name could be here!)

## Additional Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Python Security Best Practices](https://python.readthedocs.io/en/stable/library/security_warnings.html)
- [CWE Top 25](https://cwe.mitre.org/top25/)

---

Last updated: December 2025

