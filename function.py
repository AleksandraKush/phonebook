class PhoneBook:

    def __init__(self, path: str = 'phonebook.txt'):
        self.path = path 
        self.phone_book = []

    def open_file(self):
        with open(self.path, 'r', encoding = 'utf-8') as file: 
            data = file.readlines() 
        for contact in data:
            pb = {}
            new = contact.strip().split(';')
            pb['name'] = new[0]
            pb['phone'] = new[1]
            pb['comment'] = new[2]
            self.phone_book.append(pb)
    
    def get(self):
        return self.phone_book


    def save_file(self):
        data = []
        for contact in self.phone_book:
            data.append(';'.join(contact.values()))
        data = '\n'.join(data)
        with open(self.path, 'w', encoding = 'utf-8') as file: 
                file.write(data) 

    def add_file(self, contact: dict): 
            self.phone_book.append(contact)
            print(f'Контакт {contact.get("name")} записан')

    def change_file(self, i: int, value: dict):
        self.phone_book[i] = value
        

    def search(self, word: str) -> list: 
        res = []
        for contact in self.phone_book:
            for field in contact.values():
                if word in field:
                    res.append(contact)
                    return res


    def delete(self, i: int):
        number = self.phone_book.pop(i)
        print(f'Контакт {number.get("name")} удален') 
