
import requests
from datetime import date, timedelta

class NewsFeed:

    base_url = "https://newsapi.org/v2/everything?"
    apikey = "8bf91806e2b14e6d85cfdd17907f0d2f"

    def __init__(self, topic, days_of_news=3, language="en"):
        self.from_date = str(date.today() + timedelta(days=-days_of_news))
        self.to_date = str(date.today())
        self.topic = topic
        self.language = language

    def get(self):
        request_url = f"{self.base_url}" \
                      f"qInTitle={self.topic}&" \
                      f"from={self.from_date}&" \
                      f"to={self.to_date}&" \
                      f"language={self.language}&" \
                      f"apiKey={self.apikey}"

        response = requests.get(request_url)

        content = response.json()['articles']

        email_body = ""

        for article in content:
            email_body = email_body \
                         + article['title']\
                         + "\n" + '-  ' + article['content'][0:150] \
                         + "\n" + '-   ' \
                         + article['url'] + '\n\n'

        return email_body


newsfeed = NewsFeed("ukraine")

email_body = newsfeed.get()

print(email_body)