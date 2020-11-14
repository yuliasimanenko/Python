import re
# 1. 
# Вх: строка. Если длина > 3, добавить в конец "ing", 
# если в конце нет уже "ing", иначе добавить "ly".
def v(s):
  if len(s) > 3 :
    s = s + 'ly' if s[-3:] == 'ing' else s + 'ing'
  return s


# 2. 
# Вх: строка. Заменить подстроку от 'not' до 'bad'. ('bad' после 'not')
# на 'good'.
# Пример: So 'This music is not so bad!' -> This music is good!

def nb(s): 
  return re.sub(r"not.+?bad", r"good", s, count =0)


