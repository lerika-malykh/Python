import Task_01 as op


string = '(1 + 2) - 3 * 6 / 2'.replace('(', ' ( ').replace(')', ' ) ').replace('+', ' + ').replace('-', ' - ')\
                                                                      .replace('*', ' * ').replace('/', ' / ').split()
for i in range(len(string)):
    if string[i].isdigit():
        string[i] = int(string[i])
print(string)
index_start = -1

while True:
    for i in range(len(string)):
        if string[i] == '(':
            index_start = i
    if index_start == -1:
        break
    else:
        index_end = string.index(')', index_start) + 1
        print(index_start, index_end)
        lst = string[index_start:index_end]
        del string[index_start:index_end]

        lst.pop(0)
        lst.pop(-1)
        op.operation(lst)
        lst = int(*lst)

        string.insert(index_start, lst)
        index_start = -1


op.operation(string)
print(*string)
