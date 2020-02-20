'''
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное
значение. При вызове функции должен создаваться объект-генератор. Функция должна
вызываться следующим образом: for el in fibo_gen(). Функция отвечает за получение
факториала числа, а в цикле необходимо выводить только первые 15 чисел.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал
четырёх 4! = 1 * 2 * 3 * 4 = 24.
'''
from math import factorial
#import math
from itertools import count


def my_f():
    for i in count(1):
        yield factorial(i) #получается по смыслу return, только для генератора

x = 0
for i in my_f():
    print('Factorial {} - {}'.format(x + 1, i)) #print(f'Factorial {} - {}') пробовал записать по новому, пока не получилось
    if x == 14:
        break
    x += 1