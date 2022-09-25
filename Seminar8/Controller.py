import Import
import Input
import Export

ch = Input.user_choice()

if ch == '1':
    str1, str2, str3, str4, str5 = Input.data()
    print(str1, str2, str3, str4, str5)
    str0 = ''
    Import.add(str1)
    Import.add(str2)
    Import.add(str3)
    Import.add(str4)
    Import.add(str5)
    Import.add(str0)
elif ch == '2':
    Export.print_baza()
else:
    print('Введена недопустимая операция!')