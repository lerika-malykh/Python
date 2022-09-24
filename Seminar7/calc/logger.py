def write(some_str, result):
    with open('log.txt', 'a') as l:
        l.write(f'{some_str} = {result}' + '\n')
