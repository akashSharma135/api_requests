import requests

# Fetching the data from api
req = requests.get('https://reqres.in/api/users').json()

# Total number of pages
total_pages = req['total_pages']

total_users = 0

# Getting total users
for page in range(0, total_pages):
    total_users += len(requests.get(f'https://reqres.in/api/users?page={page + 1}').json()['data'])

print(total_users)
