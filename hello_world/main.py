""" Module Providing methods to interact with http url"""
import requests


def fetch_github_api_status():
    """Function that feches github api status"""
    response = requests.get("https://api.github.com", timeout=10)
    if response.status_code == 200:
        return 'Hello, World! GitHub API is reachable.'
    else:
        return 'Hello, World! But could not reach GitHub API.'


def main():
    """Main function of the script"""
    print(fetch_github_api_status())


if __name__ == "__main__":
    main()
