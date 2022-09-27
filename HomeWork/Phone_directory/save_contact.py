def save_to_csv(info):
    with open('contact.csv', 'a', encoding='utf-8') as b:
        for i in range(len(info)):
            if i != len(info) - 1:
                b.write(f'{info[i]};')
            else:
                b.write(f'{info[i]}')
        b.write('\n')
