import requests
from send_email import send_email

api_key = "d4e5768f3c82495d8a3601f9a0dec894"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2024-07-29&sortBy=publishedAt&apiKey="
       "d4e5768f3c82495d8a3601f9a0dec894")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = ""
# Access the article titles and description
for article in content['articles']:
    if article['title'] is not None:
        body = body + article["title"] + "\n" +  article["description"] + 2 * "\n"

body=body.encode("utf-8")
send_email(message=body)