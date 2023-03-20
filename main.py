import requests
from send_email import send_email

topic = "tesla"
api_key = "cd9657a739a043b0a6ba851b0d3431e0"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}" \
      "&from=2023-02-20&sortBy=publishedAt" \
      "&apiKey=cd9657a739a043b0a6ba851b0d3431e0" \
      "&language=en"


def main():
    request = requests.get(url)
    content = request.json()
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
