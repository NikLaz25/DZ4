'''Представлен список чисел. Необходимо вывести элементы исходного списка, значения
которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для
формирования списка использовать генератор'''

from random import randrange
my_list = [randrange(0, 100) for el in range(10)]
print(my_list)
list2 = []
for i in range(len(my_list)-1):
    if my_list[i] < my_list[i+1]:
        list2.append(my_list[i+1])
print(list2)


#for n, el in enumerate(my_list):
 #   if el[n] < el[n + 1]:
  #      list2 = list2.add[el(n)]
#print(list2)

#numbers = []
#for i in range(20):
  #  numbers.append(randint(-10, 10))
#print(numbers)