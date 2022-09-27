def log_info(info):
    with open('log.txt', 'a', encoding='utf-8') as f:
        if info == 1:
            f.write(f'Добавление контакта')
        elif info == 2:
            f.write(f'Вывод контактов' + '\n')
        else:
            f.write(f'Экспорт в формате xml' + '\n')