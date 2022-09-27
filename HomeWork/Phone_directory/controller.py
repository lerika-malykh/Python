from read_contact import read_contact
from save_contact import save_to_csv
from export_to_xml import export_to_xml

def button_click():
    print('Выберите необходимую операцию:', '1 - ввод данных "Фамилия, Имя, телефон, описание"',
          '2 - вывод данных', '3 - экспорт данных', '4 - завершение работы с модулем',
          sep='\n')

    operation_select = int(input())
    if operation_select == 1:
        soname = input('Введите фамилию: ')
        name = input('Введите имя: ')
        phone_number = input('Введите номер телефона: ')
        description = input('Введите описание: ')
        new_list = [soname, name, phone_number, description]
        save_to_csv(new_list)
        return new_list
    elif operation_select == 2:
        print('Выберите формат отображения данных:', '1 - построчно', '2 - в одну строку', sep='\n')
        num = int(input())
        if num == 1 or num == 2:
            read_contact(num)
    elif operation_select == 3:
        export_to_xml()
        print('Данные успешно экспортированы в формате xml!\n' + '-' * 20)
    else:
        print('Неверный ввод!!! Повторите!!!\n' + '-' * 20)
        button_click()