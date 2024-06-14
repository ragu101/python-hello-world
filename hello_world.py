import requests

def main():
    response = requests.get('https://api.github.com')
    if response.status_code == 200:
        print('Hello, World! GitHub API is reachable.')
    else:
        print('Hello, World! But could not reach GitHub API.')

if __name__ == "__main__":
    main()
