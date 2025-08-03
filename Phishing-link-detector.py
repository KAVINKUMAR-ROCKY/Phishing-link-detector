from urllib.parse import urlparse

def load_urls_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            urls = [line.strip() for line in file if line.strip()]
            return urls
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return []
    except Exception as e:
        print(f"[ERROR] Failed to load file: {e}")
        return []

# Extended phishing patterns list — you can add full domains too
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
    "trycloudflare.com"  # <== NEW: Includes suspicious cloudflare test domains
]

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

def main():
    file_path = "phishing_urls.txt"
    urls = load_urls_from_file(file_path)

    if not urls:
        print("[INFO] No URLs to scan. Make sure the file is not empty.")
        return

    print(f"\n🔍 Scanning {len(urls)} URL(s) from '{file_path}'...\n")
    for i, url in enumerate(urls, 1):
        if is_phishing_url(url, DEFAULT_PHISHING_PATTERNS):
            print(f"{i}. ⚠️ [SUSPICIOUS] {url}")
        else:
            print(f"{i}. ✅ [SAFE] {url}")

if __name__ == "__main__":
    main()
