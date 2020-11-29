import feedparser


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
    'ecowars': 'http://www.ecowars.ru/news/rss/'
}


class UpdateData:
    def __init__(self, db_service):
        self.db_service = db_service

    def update_fetch(self, website_name):
        url = url_by_name[website_name]
        feed = feedparser.parse(url)
        for entry in feed.entries:
            if not self.db_service.has(website_name, entry.title):
                self.db_service.insert(entry, website_name)
        pass
