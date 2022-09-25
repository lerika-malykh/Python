def print_baza():
    with open('Baza.txt', 'r',encoding='utf-8') as b:
        print(b.readlines())

print_baza()
