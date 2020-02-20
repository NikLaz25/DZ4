'''Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в
порядке их следования в исходном списке. Для выполнения задания обязательно
использовать генератор.
'''

my_list = [1, 1, 2, 2, 3, 4, 5, 55, 55, 6, 8, 3, 1, 4, 10, 11, 1]
new_list = [x for x in my_list if my_list.count(x) == 1]
print (my_list, '\n', new_list)



#from random import random
#N = 10
#my_list = [0] * N
#list2 = []
#for i in range(N):
#    my_list[i] = int(random() * 50)
#print(my_list)
#for i in range(len(my_list)-1):
#    for j in range(i+1, len(my_list)):
#        if my_list[i] != my_list[j]:
#            list2.append(my_list[i])
#
#print(list2)



#from random import randrange
#my_list = [randrange(0, 10) for i in range(15)]
#print(my_list)

#list2 = combinations
#my_list1 = [55, 55, 55, 70, 80, 80, 80, 90, 100]
#from random import shuffle
#my_list1 = shuffle(my_list1)
#print(shuffle(my_list1))
#print(my_list1)