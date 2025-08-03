import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

# Default phishing patterns
DEFAULT_PHISHING_PATTERNS = [
    "phishy-site.com",
    "malicious.co/login",
    "fake-bank.net",
    "paypal-login-security-alert.com",
    "verify-account-now.net",
    "secure-update-account.com",
    "update-your-password.net",
    "confirm-your-identity.co",
    "free-gift-card-offer.com"
]

# Default URLs to scan
DEFAULT_URLS = [
    "https://diverse-sequence-troubleshooting-unnecessary.trycloudflare.com",
    "https://individuals-depending-mba-tab.trycloudflare.com"
]

def fetch_links_from_page(url, timeout=10):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[ERROR] Could not access {url}: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    anchors = soup.find_all("a", href=True)
    links = set()

    for anchor in anchors:
        href = anchor['href'].strip()
        if not href:
            continue
        full_url = urljoin(url, href)
        parsed = urlparse(full_url)
        if parsed.scheme in ("http", "https"):
            links.add(full_url)
    return sorted(links)

def is_phishing_url(link, patterns):
    link = link.lower()
    for pattern in patterns:
        if pattern.lower() in link:
            return True
    return False

def scan_urls(url_list, phishing_patterns):
    for site_url in url_list:
        print(f"\n🔍 Scanning: {site_url}")
        links = fetch_links_from_page(site_url)

        if not links:
            print("⚠️ No links found or failed to load the page.")
            continue

        print(f"✅ Found {len(links)} link(s):\n")
        for i, link in enumerate(links, 1):
            if is_phishing_url(link, phishing_patterns):
                print(f"{i}. ⚠️ [SUSPICIOUS] {link}")
            else:
                print(f"{i}. ✅ {link}")

def main():
    print("🌐 Phishing Link Scanner - Default Mode")
    scan_urls(DEFAULT_URLS, DEFAULT_PHISHING_PATTERNS)

if __name__ == "__main__":
    main()
