import requests
from prettytable import PrettyTable

def main():

    table = PrettyTable()
    table.field_names = ["Repository Name", "Created Date"]

    github_username = "MadJhey"
    api_url = f"https://api.github.com/users/{github_username}/repos"
    response = requests.get(api_url)
    data = response.json()

    for repository in data:
        table.add_row([repository["name"], repository["created_at"]])

    print(table)


if __name__ == "__main__":
    main()
