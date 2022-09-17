# 1. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 1 2 3 5

#вариант1
# def fun(num):
#     for i in range(0,len(num)):
#         if (num[i+1])-num[i] != 1:
#             return num[i]+1

# with open('numfile.txt', 'r') as data:
    
#     num = data.read()

# num = list(map(int,num.split(', ')))

# print(fun(num))

# вариант2
# my_list = [1, 2, 4, 5, 6, 8, 9, 11]

# res = [(my_list[i] - 1) for i in range(1, len(my_list)) if (my_list[i] - 1) != my_list[i - 1]]
# print(res)

# 2. Дан список чисел. Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.  
#     *Пример:* [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] и т.д.
    
# num = [1, 5, 2, 3, 4, 6, 1, 7]

# def nextmax(listt):    
#     max = listt[0]
#     res = [listt[0]]
#     for i in range(len(listt)):
#         if listt[i] > max:
#             max = listt[i]
#             res.append(max)       
#     return res
# print(nextmax(num))

# -------------------------

# my_list = [1, 5, 2, 3, 4, 6, 1, 7]

# res = [my_list[0]]
# [res.append(item) for item in my_list if item > res[-1]]
# print(res)

# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 'Мы неабв очень любим Питон иабв Джавуабв!'
# 'Мы очень любим Питон!'

# print (' '.join(filter(lambda x: not 'абв' in x,'Мы неабв очень любим Питон иабв Джавуабв!'.split())))

# -------------------------

my_str = 'Мы неабв очень любим Питон иабв Джавуабв!'.split()

print(' '.join([word for word in my_str if 'абв' not in word]))
