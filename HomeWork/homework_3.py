# 1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# list_0 = [2, 3, 5, 9, 3]
# print(list_0)
# sum = 0
# for i in range(len(list_0)):
#     if i %  2 != 0:
#         sum = sum + list_0[i]
# print(f'Сумма элементов, стоящих на нечётной позиции = ', sum)

# 2.Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# list_0 = [2,3,4,5,6]
# def mult(list_0):
#     mult = []
#     for i in range((len(list_0)+1)//2):
#         mult.append(list_0[i]*list_0[len(list_0)-1-i])
#     return mult
# print(list_0, ' -> ', mult(list_0))

# 3.Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# list_0 = [1.1, 1.2, 3.1, 5.1, 10.01]
# def dif(list_0):
#     dif_max_min =[]
#     for i in range(len(list_0)):
#         dif_max_min.append(list_0[i]%1)
#     return max(dif_max_min) - min(dif_max_min)
# print(list_0, ' -> ', round(dif(list_0),2))

# 4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# number = int(input('Введите число: '))
# str_0 = ''
# while number > 0:
#     str_0 = str(number % 2)+str_0
#     number = number//2
# print(str_0)

#5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# k = int(input('Введите число k: '))
# fib_list = [0]*(k*2+1)
# fib_list[k] = 0
# fib_list[k+1] = 1
# for i in range(k+2, len(fib_list)):
#     fib_list[i] = fib_list[i-2] + fib_list[i-1]

# for i in range(k, -1, -1):
#     fib_list[i] = fib_list[i+2] - fib_list[i+1]
# print(fib_list)