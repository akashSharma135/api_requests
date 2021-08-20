import requests

# Fetching the data from the API
posts = requests.get('https://my-json-server.typicode.com/typicode/demo/posts').json()
comments = requests.get('https://my-json-server.typicode.com/typicode/demo/comments').json()

# Initializing a list to store comments
comment_body = []
# Getting the length of comments
comments_length = len(comments)

# Iterating over the posts and comments to combine the data
for post in posts:
    for comment in comments:
        # checking if the comment is associated with the particular post
        if (post['id'] == comment['postId']):
            # Appending the comment
            comment_body.append(comment['body'])
    # Combining the posts and comments
    post.update({'comments': comment_body.copy()})

    # Clear the comment_body list
    comment_body.clear()

print(posts)
