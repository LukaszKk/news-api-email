import requests
from datetime import datetime
from send_email import send_email

topic = "tesla"
date = datetime.today().strftime('%Y-%m-%d')
api_key = "cd9657a739a043b0a6ba851b0d3431e0"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}" \
      f"&from={date}&sortBy=publishedAt" \
      "&apiKey=cd9657a739a043b0a6ba851b0d3431e0" \
      "&language=en"


def main():
    request = requests.get(url)
    content = request.json()
    if content["status"] == "error":
        print(content["message"])
        return
    body = ""
    for article in content["articles"][:20]:
        if article["title"] is not None:
            body = "Subject: Today's news" + body \
                   + article["title"] + "\n" \
                   + article["description"] + "\n" \
                   + article["url"] + 2 * "\n"

    send_email(message=body)


if __name__ == "__main__":
    main()
