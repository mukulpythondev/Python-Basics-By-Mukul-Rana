import requests
import json

query=input("Enter the topic the news you interested in ?\n")
url=f"https://newsapi.org/v2/everything?q={query}&from=2023-04-22&sortBy=publishedAt&apiKey=9e9163e3bad24e12aa75bbde170124d7"
apkey="9e9163e3bad24e12aa75bbde170124d7"
request=requests.get(url)

news=json.loads(request.text)
for article in news["articles"]:
    print(article["title"])
    print(article['description']) 
    print("**-------------*******---------------**")