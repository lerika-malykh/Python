# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример: *
# 2 + 2 = > 4;
# 1 + 2 * 3 = > 7;
# 1 - 2 * 3 = > -5;
def operation(num):
    for i in range(0, len(num), 2):
        num[i] = int(num[i])

    op_1 = {'+': lambda x, y: x + y,
            '-': lambda x, y: x - y}
    op_2 = {'*': lambda x, y: x * y,
            '/': lambda x, y: x / y}
    i = 1
    while '*' in num or '/' in num:
        if num[i] in op_2:
            res = op_2[num[i]](num[i - 1], num[i + 1])
            del num[i - 1:i + 2]
            num.insert(i - 1, res)
            i = 1
        else:
            i += 2
    i = 1
    while '+' in num or '-' in num:
        if num[i] in op_1:
            res = op_1[num[i]](num[i - 1], num[i + 1])
            del num[i - 1:i + 2]
            num.insert(i - 1, res)
            i = 1
        else:
            i += 2
    num = int(*num)
    return num
# print(num)


number = '1 + 2 * 3 + 7 * 2 / 14'.split()
print(operation(number))
