import feedparser
from win10toast import Toastnotifier
n=ToastNotifier()
f=feedparser.parse("https://zeenews.india.com/rss/sports-news.xml")
for news in f['item']:
    n.show_toast(news['title'],news['summary'],duration=5)
