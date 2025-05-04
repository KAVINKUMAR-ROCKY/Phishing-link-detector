import re
import tldextract

# List of suspicious keywords
suspicious_keywords = ['login', 'verify', 'update', 'banking', 'free', 'secure', 'account', 'password']

# Simple blacklist of phishing domains (can be expanded)
blacklist = ['phishy-domain.com', 'malicious-site.net']

def check_url(url):
    reasons = []

    # Extract domain and subdomain
    extracted = tldextract.extract(url)
    domain = extracted.domain + '.' + extracted.suffix
    subdomain = extracted.subdomain

    # Rule 1: Check for IP address in the URL
    if re.search(r'https?://\d{1,3}(\.\d{1,3}){3}', url):
        reasons.append("Uses IP address instead of domain")

    # Rule 2: Too many subdomains
    if subdomain.count('.') >= 2:
        reasons.append("Too many subdomains")

    # Rule 3: Suspicious keywords
    for word in suspicious_keywords:
        if word in url.lower():
            reasons.append(f"Suspicious keyword detected: {word}")
            break

    # Rule 4: '@' symbol in URL
    if '@' in url:
        reasons.append("Contains '@' symbol")

    # Rule 5: Check against blacklist
    if domain in blacklist:
        reasons.append("Domain is blacklisted")

    # Final verdict
    if reasons:
        print(f"\nURL: {url}\nResult: **Suspicious**")
        print("Reasons:")
        for r in reasons:
            print(f"- {r}")
    else:
        print(f"\nURL: {url}\nResult: Looks Safe (No common phishing patterns found)")

# Example use
url_input = input("Enter a URL to check: ")
check_url(url_input)
