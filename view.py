import text_fields

def main_menu() -> int:
    print(text_fields.main_menu)
    length_menu = len(text_fields.main_menu.split('\n')) - 1
    while True:
        choice = input('Выберите пункт меню: ')
        if choice.isdigit() and 0 < int(choice) <= length_menu:
            return int(choice)
        else:
            print(f'Введите число от 1 до {length_menu}')



def show_contacts(book: list[dict], error_message: str):
    if not book:
        print(error_message)
        return False
    else:
        for i, contact in enumerate(book):
            print(f'{i}.{contact.get("name"): < 20} '
                  f'{contact.get("phone"): < 20}'
                  f'{contact.get("comment"): < 20}')
        return True



def add_contact() ->dict:
    name = input('Введите имя: ')
    phone = input('Введите телефон:')
    comment = input('Введите комментарий: ')
    return {'name': name, 'phone': phone, 'comment': comment}



def input_index(message: str):
    return int(input(message))


def input_search(message):
    return input(message)



def change_contact(book: list[dict], index: int):
    print('Введите новые данные или  оставте пустое поле если нет изминений')
    contact = add_contact()
    return {'name': contact.get('name') if contact.get('name') else book[index-1].get('name'),
            'phone': contact.get('phone') if contact.get('phone') else book[index-1].get('phone'),
            'comment': contact.get('comment') if contact.get('comment') else book[index-1].get('comment')}
    # book[index-1]


def show_message(message: str):

    print('_'*len(message))
    print(message)
    print('_'*len(message))