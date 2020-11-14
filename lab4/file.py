"""
Прочитать из файла (имя - параметр командной строки)
все слова (разделитель пробел)

Создать "Похожий" словарь который отображает каждое слово из файла
на список всех слов, которые следуют за ним (все варианты).


Список слов может быть в любом порядке и включать повторения.
например "and" ['best", "then", "after", "then", ...] 

Считаем , что пустая строка предшествует всем словам в файле.

С помощью "Похожего" словаря сгенерировать новый текст
похожий на оригинал.
Т.е. напечатать слово - посмотреть какое может быть следующим 
и выбрать случайное.

В качестве теста можно использовать вывод программы как вход.парам. для следующей копии
(для первой вход.парам. - файл)

Файл:
He is not what he should be
He is not what he need to be
But at least he is not what he used to be
  (c) Team Coach


"""

import random
import sys


def read_word_list_from_file(file_name):
    if not isinstance(file_name, str):
        raise ValueError("Incorrect argument type")
    try:
        with open(file_name, 'r') as file_open:
            list_of_words = file_open.read().split()
        return list_of_words
    except FileNotFoundError:
        # raise FileNotFoundError("Can't open the file. File not found")
        print("Can't open the file. File not found")
        exit(-1)
    except PermissionError as e:
        print(f"Permission denied. You have no rights. {e}")
        exit(-1)
    except Exception as e:
        print(f"Can't open the file with {e}.")
        exit(-1)


def mem_dict(filename):
    if not isinstance(filename, list):
        list_of_words = read_word_list_from_file(filename)
    else:
        list_of_words = filename
    dictionary = dict.fromkeys(list_of_words)
    for key in dictionary:
        dictionary[key] = []
    stop = len(list_of_words) - 1
    for index, word in enumerate(list_of_words):
        if index != stop:
            dictionary[word].append(list_of_words[index + 1])
        else:
            dictionary[word].append("")
    dictionary[""] = list_of_words
    return dictionary


def create_text_from_dict(dictionary, length_of_text, list_of_text):
    if length_of_text == 0:
        return list_of_text
    next_word = random.choice(dictionary[list_of_text[-1]])
    length_of_text -= 1
    list_of_text.append(next_word)
    create_text_from_dict(dictionary, length_of_text, list_of_text)
    return list_of_text


def make_new_story(file_or_list):
    dictionary = mem_dict(file_or_list)
    text_list = [random.choice(list(dictionary.keys()))]
    list_of_story = create_text_from_dict(dictionary, 20, text_list)
    print_the_story(list_of_story)
    return list_of_story


def print_the_story(word_list):
    for word in word_list:
        print(word, end='  ')
    print("\n")
    pass


def main():
    args = sys.argv[1:]
    if not args:
        print('use: [--file] file [file ...]')
        sys.exit(1)
    story1 = make_new_story(args[0])
    make_new_story(story1)
    pass


if __name__ == '__main__':
    main()
