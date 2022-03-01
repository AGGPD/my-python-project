import requests

response = requests.get('https://api.github.com/orgs/octokit/repos')
my_projects = response.json()

for project in my_projects:
    print(f"Project name: {project['name']} \nProject Url:{project['url']}\n")