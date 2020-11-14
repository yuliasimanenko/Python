# 1. 
# Вх: список строк, Возвр: кол-во строк
# где строка > 2 символов и первый символ == последнему

def me(words):
  count = 0
  for string in words:
    if len(string) > 2 and string[0] == string[-1]:
      count += 1
  return count


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


# 3. 
# Вх: список непустых кортежей, 
# Возвр: список сортир по возрастанию последнего элемента в каждом корт.
# [(1, 7), (1, 3), (3, 4, 5), (2, 2)] -> [(2, 2), (1, 3), (3, 4, 5), (1, 7)]

def meth(kort):
  return sorted(kort, key=lambda val: val[-1])

def test(res, expt):
  print(res == expt)
  pass

def main():
  test(me(['AsdA', 'SddS', 's']), 2)
  test(meth([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
  test(fx(['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc']), ['xacadu', 'xyz', 'aabbbccc', 'apple', 'tix'])
  pass


if __name__ == '__main__':
  main()
