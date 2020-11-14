import string2

# 1. 
# Вх: список чисел, Возвр: список чисел, где 
# повторяющиеся числа урезаны до одного 
# пример [0, 2, 2, 3] returns [0, 2, 3]. 

def rm_adj(nums):
  return sorted(list(set(nums)))

# 2. Вх: Два списка упорядоченных по возрастанию, Возвр: новый отсортированный объединенный список 
  # return
def double_list(list1, list2):
  return sorted(list1 + list2)


def test(expect , result):
  print(f'Expected result is {expect}, return value is {result} \nTest is {expect == result}')
  pass


def main():
  test([0, 2, 3], rm_adj ([0, 2, 2, 3]))
  test([0, 2, 3, 45], double_list ([0, 2, 2, 3],[2,3,45]) )
  test('meatingly', string2.v('meating'))
  test('This music is good!', string2.nb('This music is not so bad!'))
  pass

if __name__ == '__main__':
  main()

