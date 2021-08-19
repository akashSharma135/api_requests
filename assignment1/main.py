import requests

# Fetching data from API
posts = requests.get('https://my-json-server.typicode.com/typicode/demo/posts').json()
comments = requests.get('https://my-json-server.typicode.com/typicode/demo/comments').json()

# Initializing dictionary
combined_data = {}
# Initializing list for comments
comment_body = []
# Initializing some variables
check_id = id = 0

# Looping over the data and combining it
for post in posts:
    id += 1
    for comment in comments:
        if post['id'] == comment['postId']:
            if (check_id != post['id']):
                comment_body.clear()
            comment_body.append(comment['body'])
            combined_data = {id: {"postId": post['id'], "title": post['title'], "comment": comment_body}}
            check_id = post['id']

# Combined post and comment data
print(combined_data)