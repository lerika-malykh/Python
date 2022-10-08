# class Auto:
#     # атрибуты класса
#     auto_name = 'Lexus'
#     auto_model = 'RX 350L'
#     auto_year = 2019

#     # Методы класса
#     def on_auto_start(self):
#         print(f'Заводим авто')

#     def on_auto_stop(self):
#         print(f'Останавливаем работу двигателя')

# a = Auto()
# print(a)
# print(type(a))
# print(a.auto_name)
# a.on_auto_start()
# a.on_auto_stop()

# --------------------------------

# class Auto:
# #     # атрибуты класса
#     auto_count = 0

# #     # Методы класса
#     def on_auto_start(self, auto_name, auto_model, auto_year):
#         self.auto_name = auto_name
#         self.auto_model = auto_model
#         self.auto_year = auto_year
#         print(f'Заводим авто')
#         Auto.auto_count += 1

# a = Auto()
# print(a)
# a.on_auto_start('Lexus', 'RX 350L', 2019)
# print(a.auto_name)
# print(a.auto_count)
# a_2 = Auto()
# a_2.on_auto_start('Audi', 'A4', 2014)
# print(a_2.auto_name)
# print(a_2.auto_count)

# class Auto:
#     auto_count = 0

#     def __init__(self, auto_name, auto_model, auto_year):
#         self.auto_name = auto_name
#         self.auto_model = auto_model
#         self.auto_year = auto_year
#         Auto.auto_count += 1
#         print(Auto.auto_count)

# a_1 = Auto('Lexus', 'RX 350L', 2019)
# a_2 = Auto('Audi', 'A4', 2014)       

# Задача 1. Напишите класс LittleBell, который при вызове метода sound печатает слово "ding" 

# Задача 2.
# class Button:
#     count = 0

#     def click(self):
#         Button.count += 1

#     def click_count(self):
#         return Button.count

#     def reset(self):
#         Button.count = 0

# button = Button()
# button.click()
# button.click()
# print(button.click_count())
# button.reset()
# print(button.click_count())

# class Big_bell:
#     def __init__(self):
#         self.count = 1

#     def sound(self):
#         self.count += 1
#         if not self.count % 2:
#             print('ding')
#         else:
#             print('dong')

# bell = Big_bell()
# bell.sound()
# bell.sound()
# bell.sound()

# bell_2 = Big_bell()
# bell_2.sound()

# Напишите класс Balance для описания весов с двумя чашами. 
# На левую и правую чашу объекта будут добавляться грузы с различным весом, 
# ваша задача определить положение чаш.

# Метод add_right принимает целое число — вес, положенный на правую чашу весов, 
# addjeft — на левую чашу. Метод result должен возвращать символ =, 
# если вес на чашах одинаковый, R — если перевесила правая, 
# L — если перевесила левая.

# Формат ввода

# Каждый тест представляет собой код, в котором будет использоваться ваш класс. 
# Файл с решением не обязательно называть solution.ру, он будет переименован автоматически. Тест запускается с вашим классом, а его вывод сравнивается с правильным решением.

# ПРИМЕР 1
# Ввод
# from solution import Balance

# balance = Balance() 
# balance.add_right(10) 
# balance.add_left(9) 
# balance.add_left(2) 
# print(balance.result())

# Вывод : L

# class Balance:
#     def __init__(self):
#         self.left = 0
#         self.right = 0

#     def add_left(self, weight):
#         self.left += weight

#     def add_right(self, weight):
#         self.right += weight

#     def result(self):
#         if self.left < self.right:
#             return 'R'
#         elif self.left > self.right:
#             return 'L'
#         else:
#             return '='

# ballance = Balance()
# ballance.add_right(10)
# ballance.add_left(9)
# ballance.add_left(2)
# print(ballance.result())

# ballance.add_right(10)
# ballance.add_left(5)
# ballance.add_left(5)
# print(ballance.result())
# ballance.add_left(1)
# print(ballance.result())
    
# РАЗБИВКА ПО ЧЕТНОСТИ

# Напишите класс OddEvenSeparator. 
# в который можно добавлять числа, получая потом отдельно чётные и нечётные. 
# Числа добавляются в объект с помощью метода add.number. 
# Методы even и odd должны возвращать списки чётных и нечётных чисел соответственно. 
# Числа в списке должны идти в том же порядке, что и при добавлении в объект.

# Формат ввода

# Каждый тест представляет собой код, в котором будет использоваться ваш класс. 
# Файл с решением не обязательно называть solution.py. 
# он будет переименован автоматически. 
# Тест запускается с вашим классом, а его вывод сравнивается с правильным решением.

# class OddEvenSeparator:
#     def __init__(self):
#         self.lst = []
        
#     def add_number(self,number):
#         self.lst.append(number)
        
#     def even(self):
#         return list(filter(lambda x : x%2 == 0, self.lst))
    
#     def odd(self):
#         return list(filter(lambda x : x%2 != 0, self.lst))
# separator = OddEvenSeparator()
# separator.add_number(1)
# separator.add_number(5)
# separator.add_number(6)
# separator.add_number(8)
# separator.add_number(3)
# print(separator.even)
# print(separator.odd)
# print(' '.join(map(str, separator.even())))
# print(' '.join(map(str, separator.odd())))

# ------------------------------

# class OddEvenSeparator():

#     def __init__(self):
#         self.odd = []
#         self.even = []

#     def add_number(self, num):
#         if not num % 2:
#             self.even.append(num)
#         else:
#             self.odd.append(num)

# separator = OddEvenSeparator()
# separator.add_number(1)
# separator.add_number(5)
# separator.add_number(6)
# separator.add_number(8)
# separator.add_number(3)
# print(separator.even)
# print(separator.odd)

# Напишите класс MinMaxWordFinder. 
# Класс должен уметь анализировать текст и находить 
# в нём слова наименьшей и наибольшей длины. 
# Текст состоит из предложений, которые добавляются в 
# обработку методом add_sentence. 
# Метод shortest_words возвращает список самых коротких 
# на данный момент слов, метод longest_words — самых длинных. 
# Слова, возвращаемые методами shortest_words и longest_words, 
# должны быть отсортированы по алфавиту.
# Если одно из самых коротких слов встретилось в 
# исходных предложениях несколько раз, оно должно столько же раз 
# повториться в списке самых коротких слов. 
# Самые длинные слова наоборот должны входить в список без повторов.

# Формат ввода

# Каждый тест представляет собой код, в котором будет использоваться ваш класс. 
# Файл с решением не обязательно называть solution.ру, 
# он будет переименован автоматически. 
# Тест запускается с вашим классом, а его вывод сравнивается с правильным решением.

class MinMaxWordFinder:
    def __init__(self):
        self.some_list = []

    def add_sentence(self, sentence):
        self.some_list.extend(sentence.split())

    def shortest_words(self):
        self.short_list = []
        short_word = self.some_list[0]
        for word in self.some_list:
            if len(word) < len(short_word):
                short_word = word
        for word in self.some_list:
            if len(word) == len(short_word):
                self.short_list.append(word)
        return sorted(self.short_list)

    def longest_words(self):
        self.long_list = []
        long_word = self.some_list[0]
        for word in self.some_list:
            if len(word) > len(long_word):
                long_word = word
        for word in self.some_list:
            if len(word) == len(long_word) and word not in self.long_list:
                self.long_list.append(word)
        return sorted(self.long_list)

finder = MinMaxWordFinder()
finder.add_sentence('hello abc world')
finder.add_sentence('def asdf qwert')
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))


