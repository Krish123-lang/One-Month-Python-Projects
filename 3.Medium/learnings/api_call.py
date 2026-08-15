import requests
# url = "https://jsonplaceholder.typicode.com/posts"
url = "https://jsonplaceholder.typicode.com/users/1"
r = requests.get(url)

if r.status_code == 200:
    data = r.json()
    # print(data)
    print(data["name"], data["username"], data["address"]["suite"])
else:
    print(f"Failed to retrieve data. Status code: {r.status_code}")
