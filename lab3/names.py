from bs4 import BeautifulSoup
from tabulate import tabulate
import sys


def top_names(html):
    file_html = None
    try:
        file_html = open(html, 'r')
    except FileNotFoundError:
        print(f"File not Found! --> {html}")
        return
    except Exception:
        raise Exception

    soup = BeautifulSoup(file_html, 'html.parser')
    items = soup.find_all("tr", attrs={"align": "right"})
    tr = [item.contents for item in items]
    name_collection = []
    for val in tr:
        name_collection.append({
            'id': int(val[0].text),
            'male': val[1].text,
            'female': val[2].text
        })
    print(tabulate(name_collection[:10:], headers='keys'))
    file_html.close()
    pass


def extr_name(filename):
    try:
        file_html = open(filename, 'r')
        soup = BeautifulSoup(file_html, 'html.parser')

        year_html = soup.find("input", attrs={"type": "text", "name": "year"})
        year = year_html.get('value')

        names_html = soup.find_all("tr", attrs={"align": "right"})
        tr = [name_html.contents for name_html in names_html]
        name_list_collection = []
        sorted_list = [year]
        for name in tr:
            name_list_collection.append((int(name[0].text), name[1].text))
            name_list_collection.append((int(name[0].text), name[2].text))
            sorted_list.append(name[1].text + " " + name[0].text)
            sorted_list.append(name[2].text + " " + name[0].text)
        name_list_collection.sort(key=lambda elem: elem[-1])
        sorted_list.sort()
        # print(list(filter(lambda elem: elem in male_list, female_list)))
        file_html.close()
        return sorted_list
    except FileNotFoundError:
        raise FileNotFoundError(f"File not Found! --> {filename}")
    except Exception:
        return 0


def main():
    args = sys.argv[1:]
    if not args:
        print('use: [--file] file [file ...]')
        sys.exit(1)
    for arg in args:
        sorted_list = extr_name(arg)
        for a in sorted_list:
            print(a)
    for arg in args:
        print(f"TOP FOR FILE {arg}")
        top_names(arg)
    pass


if __name__ == '__main__':
    main()
