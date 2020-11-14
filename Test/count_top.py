import collections
import re


def read_file():
    with open("input", 'r', encoding='utf-8') as text_file:
        words_list = text_file.read().split()
    new_list = []
    for word in words_list:
        word = word.replace('.', '')
        word = word.replace(',', '')
        new_list.append(word)
    print(new_list)
    return words_list


def count_top():
    words = read_file()
    counter = collections.Counter(words)
    counter_dict = dict.fromkeys(words)
    for key in counter_dict:
        counter_dict[key] = []

    for word in words:
        if re.fullmatch(r'\\u[\dabcdef]{4}', word):
            print(word)


count_top()
