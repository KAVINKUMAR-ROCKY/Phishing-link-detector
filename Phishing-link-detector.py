import os

def load_phishing_urls(file_path):
    try:
        with open(file_path, 'r') as file:
            urls = [line.strip() for line in file if line.strip()]
            return urls
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def is_phishing_url(url, phishing_urls):
    for pattern in phishing_urls:
        if pattern in url:
            return True
    return False

def main():
    # Ask user for file path
    file_path = input("Enter the path to your phishing URL file (e.g., phishing_urls.txt): ").strip()
    phishing_urls = load_phishing_urls(file_path)

    if not phishing_urls:
        print("No phishing URLs loaded. Exiting.")
        return

    # Ask user for the URL to scan
    user_url = input("Enter the URL to scan: ").strip()

    # Check the URL
    if is_phishing_url(user_url, phishing_urls):
        print("WARNING: This URL matches a known phishing pattern.")
    else:
        print("This URL appears safe (not in phishing list).")

if __name__ == "__main__":
    main()
