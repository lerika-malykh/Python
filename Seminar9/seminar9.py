# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода: 
# какой тип данных выбрать, в теле функции или снаружи.

# first_list = ['1','2','3','4','5']
# second_list = ['one', 'two', 'three', 'four', 'five']

# magic_dict = {}
# for i in range (len(first_list)):
#     magic_dict[first_list[i]]=second_list[i]
# print(magic_dict)

# -----------------------

# magic_dict={first_list[i]: second_list[i] for i in range(len(first_list))}
# print(magic_dict)

# def num_translate(number):
#     dig_dict={'one': 'один', 'two': 'два', 'three': 'три'}
#     print(dig_dict.get(number))

# num_translate(input('Введите число: '))

# 2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): 
# реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. 
# Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

# def num_translate(number):
#     s_dict = {'one': 'один', 'two': 'два', 'three': 'три'}
#     if number[0].isupper():
#         print(s_dict.get(number.lower(), 'none').capitalize())
#     else: print(s_dict.get(number))

# num_translate(input('Vvod: '))

# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, 
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. 
# Например:
# >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"], 
#     "М": ["Мария"], "П": ["Петр"]
# }

def thesaurus(*args):
    some_dict = {}
    for i in args:
        if i[0] in some_dict.keys():
            some_dict[i[0]].append(i)
        else:
            some_dict[i[0]] = [i]
    print(some_dict)

thesaurus("Иван", "Мария", "Петр", "Илья")
