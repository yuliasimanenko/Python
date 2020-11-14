
# 1. 
# Входящие параметры: int <count> , 
# Результат: string в форме
# "Number of: <count>", где <count> число из вход.парам.
#  Если число равно 10 или более, напечатать "many"
#  вместо <count>
#  Пример: (5) -> "Number of: 5"
#  (23) -> 'Number of: many'

def num_of_items(count):
    string = 'many' if count >= 10 else str(count)
    return "Number of: " + string


# 2. 
# Входящие параметры: string s, 
# Результат: string из 2х первых и 2х последних символов s
# Пример 'welcome' -> 'weme'.
def start_end_symbols(s):
  if len(s) > 3 : 
    return s[:2:] + s[-2:] 
  return s


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


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(res, expt):
  print(res == expt)
  pass

def main():
  test(start_end_symbols('welcome'), 'weme')
  test(replace_char('bibble'), 'bi**le')
  test(num_of_items(10), 'Number of: many')
  test(str_mix('dog', 'dinner'), 'dig donner')
  pass
  


if __name__ == '__main__':
  main()
