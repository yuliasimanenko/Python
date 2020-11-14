
#name = input()
#A = 'Yes' if name != "Test" else 'No'
#print (A)
# list_chars = [a + b for a in 'Jam' for b in 'Meat' if b != a]
# print (list_chars)

# list_chars.extend(list_chars)
# print(list_chars)
# v = 0
# for i in list_chars :
#     if v < len(list_chars)/2 :
#         print (i, "\t", end='')
#         v += 1
#     else:
#         break
# word1 = 'First'
# word2 = 'Second'
# list_chars.clear()
# list_chars = ['A1', 'S2', 'D3']
# list_chars[0] = 'Start'


# print(word1[-1], list_chars)




def func (arg_1):
    print ("function works")
    def innner_func(arg_2):
        return arg_1 + arg_2
    return innner_func


#1
def num_of_items(count):
    string = 'many' if count >= 10 else str(count)
    return "Number of: " + string

print (num_of_items(9))


# 2. 
# Входящие параметры: string s, 
# Результат: string из 2х первых и 2х последних символов s
# Пример 'welcome' -> 'weme'.
def start_end_symbols(s):
    if len(s) > 3 : 
        return s[:2:] + s[-2:] 
    return s
print(start_end_symbols("welcome"))


# 3. 
# Входящие параметры: string s,
# Результат: string где все вхождения 1го символа заменяются на '*'
# (кроме самого 1го символа)
# Пример: 'bibble' -> 'bi**le'
# s.replace(stra, strb) 

def replace_char(s):
    string = ''
    for i, char in enumerate(s) :
        if char == s[0] and i != 0:
            string += '*'
        else:
            string += s[i]
    return string

print(replace_char('bibble'))


# 4
# Входящие параметры: string a и b, 
# Результат: string где <a> и <b> разделены пробелом 
# а превые 2 симв обоих строк заменены друг на друга
# Т.е. 'max', pid' -> 'pix mad'
# 'dog', 'dinner' -> 'dig donner'
def str_mix(a, b):
    if len(a) < 2 or len(b) < 2:
        return a + " " + b
    return b[:2]+a[2:] + " " + a[:2]+b[2:]

print (str_mix('max','pid'))

def test(res, exp):
    print(res == exp)
    pass





# 1. 
# Вх: список строк, Возвр: кол-во строк
# где строка > 2 символов и первый символ == последнему

def me(words):
    count = 0
    for string in words:
        if len(string) > 2 and string[0] == string[-1]:
            count += 1
    return count
inp = ['AfgA', 'SoffsS','AA','sdsdg']
print (me(inp))

# 2. 
# Вх: список строк, Возвр: список со строками (упорядочено)
# за искл всех строк начинающихся с 'x', которые попадают в начало списка.
# ['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc'] -> ['xacadu', 'xyz', 'aabbbccc', 'apple', 'tix']
def fx(words):
    x_list = []
    for element in words:
        if element[0] == 'x':
            x_list.append(element)
            words.remove(element)
    words.sort()
    x_list.sort()
    x_list.extend(words)
    return x_list
w =  ['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc']
print(fx(w))
#return sorted(words, key = lambda x: (x[0] != 'x', x))


# 3. 
# Вх: список непустых кортежей, 
# Возвр: список сортир по возрастанию последнего элемента в каждом корт.
# [(1, 7), (1, 3), (3, 4, 5), (2, 2)] -> [(2, 2), (1, 3), (3, 4, 5), (1, 7)]

def meth(kort):
    new_kort = sorted(kort, key=lambda val: val[-1])
    return new_kort
ex = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]

print(meth(ex))

