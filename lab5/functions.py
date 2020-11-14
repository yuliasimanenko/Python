import requests
import random
from lxml import html


def get_names(count):
    try:
        with open('names/names.txt', 'r', encoding="utf-8") as file_open:
            list_of_words = file_open.read().split("\n")
            random.shuffle(list_of_words)
        return list_of_words[:count]
    except FileNotFoundError:
        print("Can't open the file. File not found")
        return -1
    except PermissionError as e:
        print(f"Permission denied. You have no rights. {e}")
        return -1
    except Exception as e:
        print(f"Can't open the file with {e}.")
        return -1


def choose_name(list_names):
    return random.choice(list_names)


def get_img_link(name):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}
    url = f'https://yandex.ru/images/search?text={name}'
    r = requests.get(url, headers=headers)
    tree = html.fromstring(r.text.encode('utf-8'))
    list_of_img = ['http:' + a for a in tree.xpath("//img[@class='serp-item__thumb justifier__thumb']/@src")]
    return random.choice(list_of_img)

