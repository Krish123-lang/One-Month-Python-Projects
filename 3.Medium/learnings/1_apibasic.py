import requests
r = requests.get("https://api.github.com/events")

# Passing value to the url
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get("https://catfact.ninja/facts", params=payload)


# print(r.url)
# print(r.text)

# with open('apitext.json', 'w') as f:
#     f.write(r.text)

# print(r.encoding)
# print(r.content)

# print(r.json())
# print(r.raise_for_status())
# print(r.status_code)
