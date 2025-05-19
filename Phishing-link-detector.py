import re
from urllib.parse import urlparse
import requests

# Custom phishing pattern (example: new-event.com.tr style)
CUSTOM_PHISHING_PATTERN = re.compile(
    r"https?://(?:www\.)?new-event\.com\.tr/\^.*\$/[a-zA-Z0-9]+/\?id=\d+",
    re.IGNORECASE
)

# Load known phishing domains from file or online source
def load_known_phishing_domains(file_path=None, url=None):
    domains = set()
    try:
        if file_path:
            with open(file_path, "r", encoding="utf-8") as f:
                domains = set(line.strip().lower() for line in f if line.strip())
        elif url:
            response = requests.get(url, timeout=10)
            if response.ok:
                domains = set(line.strip().lower() for line in response.text.splitlines() if line.strip())
    except Exception as e:
        print(f"[!] Failed to load phishing domains: {e}")
    return domains

# Check if a URL matches the custom phishing format
def is_custom_phishing(url):
    return CUSTOM_PHISHING_PATTERN.match(url) is not None

# Check if a URL’s domain is in the known phishing list
def is_known_phishing_domain(url, domain_list):
    domain = urlparse(url).netloc.lower()
    return domain in domain_list

def main():
    print("Enter a URL to scan for phishing:")
    user_url = input("URL: ").strip()

    if not user_url.startswith("http"):
        print("[!] Please enter a valid URL starting with http or https.")
        return

    # Load phishing domains from file (you can replace this with a live feed URL if needed)
    domain_list = load_known_phishing_domains(file_path="phishing_domains.txt")

    # Perform checks
    is_custom = is_custom_phishing(user_url)
    is_known = is_known_phishing_domain(user_url, domain_list)

    # Output result
    print("\nScan Results:")
    if is_custom:
        print("[!] URL matches known custom phishing pattern.")
    if is_known:
        print("[!] URL domain is listed in known phishing domains.")
    if not is_custom and not is_known:
        print("[✓] No phishing indicators found for this URL.")

if __name__ == "__main__":
    main()
