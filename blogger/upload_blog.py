import json
import requests
import os
from dotenv import load_dotenv

# Replace these with your own values

load_dotenv()

def uploadblog(mytitle, mycontent):

    # access_token = "ya29.a0AVvZVsrTBIfa2QEkI_gfmI8-nne70F_op8iAu_i4oPrz_yHc2jNAt80Loa18HJELYCViHq03LLQlW7aKZB2ZYDcpHczzy17ryDJzRTnKkN5R5jf8c-oLt0f6maQeUF4KAXmgUZqaGgXnTwUgh5YPYQif2d-baCgYKATwSARISFQGbdwaIy9POPJHJmhueYXH809seXQ0163"

    access_token = os.environ.get("ACCESS_TOKEN")
    blog_id = "699514221187141208"

    # Build the API endpoint URL
    url = f"https://www.googleapis.com/blogger/v3/blogs/{blog_id}/posts"

    # Build the request payload
    data = {

        "kind": "blogger#post",
        "blog": {
            "id": blog_id
        },
    
        "title": mytitle,
        "content": mycontent,
        
        "labels": [
            "film", "movies", "automation", "project", "python", "imdb", "top250"
        ],

    }


    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # Make the API request
    response = requests.post(url, data=json.dumps(data), headers=headers)

    # Check the response status
    if response.status_code != 200:
        print(f"Error: {response.content}")
    else:
        print(f"\nPost {mytitle} added successfully!\n")

