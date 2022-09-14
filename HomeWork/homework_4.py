# 1. Вычислить число c заданной точностью d
# Пример: - при d = 0.001, π = 3.141.    10^{-1} ≤ d ≤10^{-10}

# from math import pi

# d =  int(input("Введите число для заданной точности числа Пи:\n"))
# print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# def check_number_simple(n: int):
#     i = 2
#     while n % i != 0 or i == n - 1:
#         i += 1
#     if i == n:
#         return n

# def fill_simple_list(n: int) -> list:
#     simple_list = [1]
#     for i in range(2, n+1):
#         if n % i == 0:
#             if check_number_simple(i) != None:
#                 simple_list.append(check_number_simple(i))
#             else:
#                 continue
#     return simple_list

# N = int(input('Введите число N: '))
# simple_list = fill_simple_list(N)
# print(simple_list)

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# import random
# list_0 = [random.randint(0,50) for i in range (15)]
# print('Исходный список ', list_0)
# new_list =[]
# [new_list.append(i) for i in list_0 if i not in new_list ]
# print('Список без повторных элементов ', new_list)

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Введите коэффициент: '))
a = int(random.randint(0,100))
b = int(random.randint(0,100))
c = int(random.randint(0,100))

if a != 0:
    first = (str(a) + "x^" + str(k) + " + ")
else:
    first = (str())

if b != 0:
    second = (str(b) + "x" + " + ")
else:
    second = (str())

if c != 0:
    third = (str(c) + " = 0")
else:
    third = (str())

print(f'{first}{second}{third}')
