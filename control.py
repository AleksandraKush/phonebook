import menu
import function

pb = function.PhoneBook()

def start():
    while True:
        choice = menu.print_menu()
        match choice:
            case 1:
                print()
                print ('Файл октрыт')
                pb.open_file()
                print()
            case 2:
                print()
                print ('Файл сохранен')
                pb.save_file()
                print()
            case 3:
                print()
                book = pb.get()
                menu.show_contact(book)
                print()
            case 4:
                print()
                new_cont = menu.add_file()
                pb.add_file(new_cont)
                print()
            case 5:
                print()
                new_value = menu.change_number(pb.get())
                pb.change_file(*new_value)
                print()
            case 6:
                print()
                word = menu.input_request('номер для поиска')
                result = pb.search(word)
                menu.show_contact(result)
                print()
            case 7:
                print()
                contact_del = menu.select_to_delete(pb.get())
                pb.delete(contact_del)
                print()
            case 8:
                menu.bye
                break