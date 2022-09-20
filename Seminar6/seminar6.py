# 1. Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.    
#     *Пример:*     
#     2+2 => 4;    
#     1+2*3 => 7;    
#     1-2*3 => -5;   
#  - Добавьте возможность использования скобок, меняющих приоритет операций.       
#     *Пример:*        
#      1+2*3 => 7;      
#      (1+2)*3 => 9;
        
# string = '1+2*3'
# string = string.replace('+', ' ')
# string = string.replace('-', ' ')
# string = string.replace('*', ' ')
# string = string.replace('/', ' ')

# lst = list(map(int, string.split()))
# print(lst)

# or item in string:
#     if not item.isdigit():
#         a.append(item)


# actions = {
#   "^": lambda x, y: str(float(x)**float(y)),
#   "*": lambda x, y: str(float(x) * float(y)),
#   "/": lambda x, y: str(float(x) / float(y)),
#   "+": lambda x, y: str(float(x) + float(y)),
#   "-": lambda x, y: str(float(x) - float(y))
# }


# res = input('Что посчитать: ')
# print(eval(res))



# 2. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# *Пример:* 
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# import random
# list_0 = [random.randint(0,50) for i in range (15)]
# print('Исходный список ', list_0)
# new_list =[]
# [new_list.append(i) for i in list_0 if i not in new_list ]
# print('Список без повторных элементов ', new_list)

my_list = [1, 1, 2, 3, 4, 4, 5]

print(tuple(filter(lambda num: my_list.count(num) == 1, my_list))) #перевели в кортеж для меньшей памяти занимаемой
