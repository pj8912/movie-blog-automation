import json
import requests
import google.auth
from google.auth.transport.requests import Request
#from google.oauth2.credentials import Credentials
#from google.auth import credentials
#from google.oauth2.credentials import Credentials
from google.oauth2.credentials import Credentials



""" If you are running the script from your terminal, 
you will need a "Desktop App" client ID. 
This type of client ID is used for installed applications that run on a user's device """

# Replace YOUR_CLIENT_ID and YOUR_CLIENT_SECRET with the actual values
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
# Replace BLOG_ID with the ID of the blog you want to post to
BLOG_ID = '699514221187141208'

# Define the new post's title and content
post_title = 'Blog Post1'
post_content = 'This is the first blog post.'

# Create the OAuth client

#creds = Credentials.from_client_info(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
creds = Credentials.from_service_account_info(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET, scopes=['https://www.googleapis.com/auth/blogger']
)


# Create the post request body
post_data = {
    'kind': 'blogger#post',
    'blog': {'id': BLOG_ID},
    'title': post_title,
    'content': post_content,
    'status': 'live'
}

# Make the API request to insert the post
response = requests.post(
    f'https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts',
    headers={'Content-Type': 'application/json'},
    data=json.dumps(post_data),
    auth=creds.with_scopes(['https://www.googleapis.com/auth/blogger'])
)

# Print the response status code and content
print(response.status_code)
print(response.content)

