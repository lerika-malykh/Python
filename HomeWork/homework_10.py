# 1. Даны два списка. Найдите все числа, которые входят как в первый, так и во второй список.
# Выведите их в порядке возрастания.
# Пример: 
# ввод - 1 2 3
#        4 3 2
# вывод - 2 3
# ввод - 1 2 6 4 5 7
#        10 2 3 4 8
# вывод - 2 4

# print(*sorted(set(input().split()) & set(input().split()), key=int))

# 2. Во входной строке записана последовательность чисел через пробел. Для каждого числа выведите слово YES (в отдельной строке), 
# если оно ранее встречалось в последовательности или NO, если не встречалось.

# numbers = [int(s) for s in input().split()]
# words = set()
# for num in numbers:
#     if num in words:
#         print('YES')
#     else:
#         print('NO')
#         words.add(num)

# 3. Дан текст: в первой строке записано число строк, далее идут сами строки.
# Определите, сколько различных словсодержится в этом тексте.
# Словом считается последовательность непробельных символов, идущих подряд, 
# слова разделены одним или большим числом пробелов или символами конца строки.
# Пример: Ввод - 4
#             She sells sea shells on the sea shore;
#             The shells that she sells are sea shells I’m sure.
#             So if she sells sea shells on the sea shore,
#             I’m sure that the shells are sea shore shells.
#         Вывод - 19

n = int(input('Введите количество строк: '))
words = set()
for i in range(n):
    words.update(input('Введите текст: ').split(' '))
if '' in words:
    words.remove('')
print(f'Количество слов в тексте: ', len(words))

