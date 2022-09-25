def add(strr):
    with open('Baza.txt', 'a') as f:
        f.write(strr + '\n')
    