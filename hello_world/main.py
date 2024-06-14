import requests


def fetch_github_api_status():
    response = requests.get('https://api.github.com')
    if response.status_code == 200:
        return 'Hello, World! GitHub API is reachable.'
    else:
        return 'Hello, World! But could not reach GitHub API.'


def main():
    print(fetch_github_api_status())


if __name__ == "__main__":
    main()
