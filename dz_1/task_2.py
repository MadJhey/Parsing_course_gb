import requests
from pprint import pprint
import json

def auth_vk_token():
    try:
        file = open("auth_vk.ini", 'r')
    except IOError as e:
        print('error file')
    else:
        access_token = file.readline()
    return access_token

def main():
    id: int = 51549877    # id app
    api_url = f'https://api.vk.com/method/groups.get?user_id={id}&access_token={auth_vk_token()}&extended=1&v=5.131'
    response = requests.get(api_url)
    data = response.json()
    pprint(data)
    with open(r"response.txt", "w") as file:
        json.dump(data, file)
    file.close()


if __name__ == "__main__":
    main()


