# Phishing URL Detection Script

This Python script helps detect potentially suspicious or phishing URLs based on several simple heuristic rules. It checks for common phishing patterns and warns the user if any are found.

GitHub Repository:  
[https://github.com/KAVINKUMAR-ROCKY/Phishing-link-detector](https://github.com/KAVINKUMAR-ROCKY/Phishing-link-detector)

---

## Features

- Detects use of IP addresses in place of domain names.
- Flags URLs with too many subdomains.
- Scans for suspicious keywords like `login`, `verify`, `update`, etc.
- Detects presence of the `@` symbol (often used to obscure true URL destinations).
- Checks URLs against a blacklist of known phishing domains.

---

## Requirements

- Python 3.x
- `tldextract` package

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/KAVINKUMAR-ROCKY/Phishing-link-detector.git
cd Phishing-link-detector
