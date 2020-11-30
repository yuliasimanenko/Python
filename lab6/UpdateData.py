import feedparser
from validator_collection import checkers
import re


def get_rss_items(url):
    feed = feedparser.parse(url)
    items_list = feed["items"]
    items = []
    for item in items_list:
        items.append({
            "link": item["link"],
            "title": item["title"],
            "description": item["summary"]
        })
    return items


url_by_name = {
    'habr': 'https://habr.com/ru/rss/interesting/',
    'ecowars': 'http://www.ecowars.ru/news/rss/',
    'sport': 'https://www.sport-express.ru/services/materials/news/se/'
}
# https://bash.im/rss/


class UpdateData:
    def __init__(self, db_service):
        self.db_service = db_service

    def update_fetch(self, website_name):
        if not isinstance(website_name, str):
            raise TypeError
        try:
            url = url_by_name[website_name]
        except NameError:
            return -1
        feed = feedparser.parse(url)
        for ent in feed.entries:
            print(ent.title)
        for entry in feed.entries:
            if not self.db_service.has(entry.title):
                self.db_service.insert(entry)
                print(f"web update {website_name}")
        pass

    @staticmethod
    def add_url(url):
        if not isinstance(url, str):
            raise TypeError
        if not checkers.is_url(url):
            return -1
        name = url.replace("https://", "").replace("www.", "").replace("http://", "")
        name = name[:name.index('.')]
        element = {
            name: url
        }
        url_by_name.update(element)
        return name

