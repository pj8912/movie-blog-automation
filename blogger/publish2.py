import json
import requests

from google.oauth2 import service_account


with open('client_secret.json', 'r') as json_key_file:
    json_key = json.load(json_key_file)


creds = service_account.Credentials.from_service_account_info(json_key, scopes=['https://www.googleapis.com/auth/blogger'])
access_token = creds.token

TOKEN = access_token
BLOG_ID = 699514221187141208
post_title = "First Blog Post"
post_content = "testing first blog post"

post_data = {

        'kind' : 'blogger#post',
        'blog' : {'id': BLOG_ID},
        'title': post_title,
        'content' : post_content,
        'status': 'live'
        
}




response = requests.post(
        
        f'https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts',
    
        headers={
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
        },
    
        data=json.dumps(post_data)
)


print(response.status_code)
print(response.content)
