# from cgi import print_exception
# from re import A


# class Auto:
#     def __init__(self, price):
#         self.price = price

#     def __add__(self, other):
#         return self.price + other.price

#     def __str__(self):
#         return 'привет, я машина!'

#     def __gt__(self, other):
#         return self.price > other.price


# a = Auto(1000000)    
# b = Auto(2000000)    
# print(a + b)
# print(a)
# print(a > b)

# -----------------------------------

# Марина заботится о здоровом питании. Она попросила вас написать класс Foodinfo, экземпляры которого будут описывать пищевую ценность продуктов, 
# а при сложении — возвращать новый экземпляр, описывающий суммарную пищевую ценность его составляющих.
# Интерфейс класса:
# fi = Foodlnfo(proteins, fats, carbohydrates) — инициализировать экземпляр заданным количеством белков, жиров и углеводов. 
# Все три параметра определяются весом в граммах (целым числом).
# fi.get_proteins() — вернуть количество белков. fi.get_fats() — вернуть количество жиров. fi.get_carbohydrates() — вернуть количество углеводов.
# fi.get_kcalories() — вернуть число килокалорий в пище по формуле (4 * белки + 9 * жиры +
# 4 * углеводы).
# fi_sum = fi1 + fi2 — результат сложения fi_sum должен быть новым объектом Foodinfo, описывающим суммарную пищевую ценность 
# продуктов fi 1 + fi2. fi 1 и fi2 не должны
# измениться.

# class FoodInfo:
#     def __init__(self, proteins, fats, carbohydrates):
#         self.proteins = proteins
#         self.fats = fats
#         self.carbohydrates = carbohydrates

#     def get_proteins(self):
#         return self.proteins

#     def get_fats(self):
#         return self.fats

#     def get_carbohydrates(self):
#         return self.carbohydrates

#     def get_kcalories(self):
#         return 4 * self.proteins + 9 * self.fats + 4 * self.carbohydrates

#     def __add__(self, other):
#         return FoodInfo(self.proteins + other.proteins, self.fats + other.fats, \
#             self.carbohydrates + other.carbohydrates)
                  

# food1 = FoodInfo(100, 100, 100)
# food2 = FoodInfo(50, 60, 70)
# food3 = food1 + food2
# print(food1.get_proteins(),food1.get_fats(),food1.get_carbohydrates(),food1.get_kcalories())
# print(food2.get_proteins(),food2.get_fats(),food2.get_carbohydrates(),food2.get_kcalories())
# print(food3.get_proteins(),food3.get_fats(),food3.get_carbohydrates(),food3.get_kcalories())    

# Список в обратном порядке
# Пример 1
# from solution import ReversedList
# rl = ReversedList([10, 20, 30]) 
# for i in range(len(rl)): 
#     print(rl[i])

# Пример 2
# from solution import ReversedList
# rl = ReversedList([]) printden(rl))

# Решение преподавателя

class ReversedList:
    def __init__(self, some_list):
        self.some_list = list(reversed(some_list))

    def __getitem__(self, item):
        return self.some_list[item]

    def __len__(self):
        return len(self.some_list)

rl = ReversedList([10, 20, 30])
for i in range(len(rl)):
    print(rl[i])

rl = ReversedList([])
print(len(rl))

# Наше решение в зале

# class ReversedList:

#     def __init__(self, lst):
#         self.lst = lst

#     def reverse(self):
#         new_lst = []
#         for i in reversed(range(len(self.lst))):
#             new_lst.append(self.lst[i])
#         return new_lst

# rl = ReversedList([10, 20, 30, 40])
# print(rl.reverse())



    

    

