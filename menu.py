def print_menu():
    print('Выберите действие:\n'
    '1. Открыть файл.\n'
    '2. Сохранить файл.\n'
    '3. Показать контакты.\n'
    '4. Добавить контакты.\n'
    '5. Изменить контакт.\n'
    '6. Найти контакт.\n'
    '7. Удалить контакт.\n'
    '8. Выход')
    print()
    data = int (input('Введите номер необходимого действия: '))
    return data

def show_contact(phone_book: list):
    print()
    if phone_book:
        for i, contact in enumerate(phone_book, 1):
            print(f'{i}. {contact.get("name"):<20} '
            f' {contact.get("phone"):<20} '
            f' {contact.get("comment"):<20}')
            print()
    else:
            print('Телефонный справочник не открыт или пуст')

def input_request(text: str) -> str:
    return input(f'Введите {text}: ')

def add_file() -> dict:
    print()
    name = input('Введите имя контакта: ')
    phone = input('Введите номер контакта: ')
    comment = input('Введите комментарий контакта: ')
    print()
    return {'name': name, 'phone': phone, 'comment': comment}

def change_number(book: list) -> tuple:
    show_contact(book)
    choice = int(input('Выберите контакт, который хотите изменить: '))
    name = input('Введите новое имя или enter без изменений: ')
    phone = input('Введите новый номер  или enter без изменений: ')
    comment = input('Введите новый комментарий или enter без изменений: ')
    return choice - 1, {'name': name if name else book[choice - 1].get('name'),
                        'phone': phone if phone else book[choice - 1].get('phone'),
                        'comment': comment if comment else book[choice - 1].get('comment')}

def select_to_delete(book: list):
    show_contact(book)
    return int(input('Введите номер элемент, который хотите удалить: '))

def bye():
    print('Пока пока')