# 14.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# number = input("Введите вещественное число: ")
# summa = 0
# for i in number:
#     if i!=".":
#         summa += i
# # print(f"Сумма цифр числа {number} = ", summa)

# 15.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# N = int (input('Введите число N: '))
# fact = 1
# for i in range(1,N):
#     fact *= i
#     print(f'{fact}', end = ', ')
# print(fact*N)

# 16.Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# n = int (input('Введите число n: '))
# list = []
# summa = 0
# for i in range(1, n+1):
#     list.append(round((1+1/i)**i, 2))
# print(*list, sep=', ')
# for i in range(1, n+1):
#     result = round((1+1/i)**i, 2)
#     summa += result
# print(f"Сумма членов последовательности =", summa)

# 17.Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# (Позиции хранятся в файле file.txt в одной строке одно число.)

from unittest import result
list = [-7, 1, 2, 3, 4, 5, 7]
x = int(input('Введите 1 позицию элемента от 0 до 6: '))
y = int(input('Введите 2 позицию элемента от 0 до 6: '))
z = int(input('Введите 3 позицию элемента от 0 до 6: '))

for i in range(len(list)):
    result = list[x -1]*list[y - 1]*list[z -1]
print(f'Произведение элементов {list[x -1]} * {list[y -1]} * {list[z -1]} =', result)

# 18.Реализуйте алгоритм перемешивания списка.

# Вариант встроенной функции:

# import random
# list = [2, 8, 4, 3, 1, 5]
# random.shuffle(list)
# print(list)

# Алгоритм:

# import random
# def mix_list(list_original):
#     list = list_original[:]
#     list_length = len(list)
#     for i in range(list_length):
#         index_aleatory = random.randint(0, list_length - 1)
#         temp = list[i]
#         list[i] = list[index_aleatory]
#         list[index_aleatory] = temp
#     return list
# list = [2, 8, 4, 3, 1, 5]
# mixed_list = mix_list(list)
# print("Исходный список: ")
# print(list)
# print("Перемешанный список: ")
# print(mixed_list)
