import requests
from send_email import send_email

topic = "tesla"
api_key = "d4e5768f3c82495d8a3601f9a0dec894"
url = "https://newsapi.org/v2/everything?" \
       f"q={topic}&" \
       "sortBy=publishedAt&" \
       "apiKey=d4e5768f3c82495d8a3601f9a0dec894&" \
       "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = ""
# Access the article titles and description
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" + "\n" + body + article["title"] + "\n" \
                + article["description"] + "\n" \
                + article["url"] + 2 * "\n"

body=body.encode("utf-8")
send_email(message=body)