from urllib.parse import urlparse

# Default phishing patterns (expandable)
DEFAULT_PHISHING_PATTERNS = [
    "phishy-site.com",
    "malicious.co",
    "fake-bank.net",
    "paypal-login-security-alert.com",
    "verify-account-now.net",
    "secure-update-account.com",
    "update-your-password.net",
    "confirm-your-identity.co",
    "free-gift-card-offer.com",
    "trycloudflare.com"  # Catch all suspicious trycloudflare subdomains
]

def load_urls_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            urls = [line.strip() for line in file if line.strip()]
            return urls
    except FileNotFoundError:
        print(f"[INFO] File '{file_path}' not found. Skipping file check.")
        return []
    except Exception as e:
        print(f"[ERROR] Failed to load file: {e}")
        return []

def is_phishing_url(full_url, phishing_patterns):
    try:
        parsed = urlparse(full_url)
        hostname = parsed.hostname or ''
        full_link = full_url.lower()
        for pattern in phishing_patterns:
            if pattern.lower() in hostname or pattern.lower() in full_link:
                return True
    except Exception as e:
        print(f"[ERROR] Invalid URL '{full_url}': {e}")
    return False

def check_and_print(url, index=None):
    status = "⚠️ [SUSPICIOUS]" if is_phishing_url(url, DEFAULT_PHISHING_PATTERNS) else "✅ [SAFE]"
    if index:
        print(f"{index}. {status} {url}")
    else:
        print(f"{status} {url}")

def main():
    print("🔐 Phishing URL Scanner\n")

    # 1. Manual check
    user_url = input("Enter a URL to check manually: ").strip()
    if not user_url.startswith(("http://", "https://")):
        user_url = "https://" + user_url
    print("\nResult for entered URL:")
    check_and_print(user_url)

    # 2. File-based check
    file_path = "phishing_urls.txt"
    file_urls = load_urls_from_file(file_path)

    if file_urls:
        print(f"\n🔍 Scanning {len(file_urls)} URL(s) from '{file_path}':\n")
        for i, url in enumerate(file_urls, 1):
            check_and_print(url, i)
    else:
        print("\n[INFO] No URLs to scan from file.")

if __name__ == "__main__":
    main()
