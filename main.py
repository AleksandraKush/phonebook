def print_menu():
    print('Это телефонный справочник. Выберите действие:\n'
    '1. Открыть файл.\n'
    '2. Сохранить файл.\n'
    '3. Показать контакты.\n'
    '4. Добавить контакты.\n'
    '5. Изменить контакт.\n'
    '6. Найти контакт.\n'
    '7. Удалить контакт.\n'
    '8. Выход')
    data = int (input('Введите номер необходимого действия: '))
    return data

import function

while True:
    user_choice = print_menu()
    match user_choice:
        case 1:
            print ('Открыть файл')
            function.open_phone_book()
        case 2:
            print ('Сохранить файл')
            function.save_phone_book()
        case 3:
            print ('Показать контакты')
            function.show_phone_book()
        case 4:
            print ('Добавить контакты')
            function.add_phone_book()
        case 5:
            print ('Изменить контакты')
            function.change_phone_book()
        case 6:
            print ('Найти контакт')
            function.search_phone_book()
        case 7:
            print ('Удалить контакт')
            function.delete_phone_book()
        case 8:
            print ('Выход')
            break