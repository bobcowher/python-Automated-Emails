import yagmail
import pandas
from news import NewsFeed

df = pandas.read_excel('people.xlsx')


def send_email(row):
    print(row['email'])
    email = yagmail.SMTP(user="bobcowher@gmail.com", password="bdriglorsfixwmey")
    news_feed = NewsFeed(topic=row['interest'])
    email.send(to=row['email'],
               subject=f"Your {row['interest']} news for today!",
               contents=f"Hi {row['name']}, see what's happening in the world of {row['interest']}\n{news_feed.get()}",
               attachments="design.txt")


for index, row in df.iterrows():
    send_email(row=row)


