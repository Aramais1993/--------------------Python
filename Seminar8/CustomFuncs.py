import os

def show_contacts(file_name):
    os.system('CLS')
    with open(file_name, 'r') as file: 
        data = file.readlines()

        for contact in data:
            print(contact, end='')
    
    input('\npress any key')

def add_contact(file_name):
    os.system('CLS')
    with open(file_name, 'a') as file:
        res = ''
        res += input('Input a surname of contact: ') + ' '
        res += input('Input a name of contact: ') + ' '
        res += input('Input a phone number of contact: ')

        file.write('\n'+ res)
    
    input('Contact was successfully added! Press any key for return')
        
def search_contact(file_name):
    os.system('CLS')
    target = input('Input a name of contact for searching: ')

    with open(file_name, 'r') as file: 
        contacts = file.readlines()

        for contact in contacts:                
            if target in contact:
                print(contact)
                break
        else :
            print('there is no contacts with this name.')

    input('press any key')

def drawing():
    print('1 - show contacts')
    print('2 - add contact')
    print('3 - search contact')
    print('4 - exit')

def main(file_name):
    while True:
        os.system('CLS')
        drawing()
        user_choice = int(input("Input a number from 1 to 4: "))

        if user_choice == 1 :
            show_contacts(file_name)
        elif user_choice == 2 :
            add_contact(file_name)
        elif user_choice == 3 :
            search_contact(file_name)
        elif user_choice == 4 :
            print('Have a nice day!')
            return
        
def confirmation(text: str):
    confirm = input(f"Подтвердите {text} записи: y - да, n - нет\n")
    while confirm not in ('y', 'n'):
        print('Введены неверные данные')
        confirm = input(f"Подтвердите {text} записи: y - да, n - нет\n")
    return confirm


def replace_record_line(file_name: str, record_id, replaced_line: str):
    replaced = ''
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            replaced += line
            if record_id == line.split(';', 1)[0]:
                replaced = replaced.replace(line, replaced_line)
    with open(file_name, 'w', encoding='utf-8') as data:
        data.write(replaced)


def change_records(file_name: str):
    record_id = check_id_record(file_name, 'изменить')
    if record_id != 'q':
        replaced_line = f'{int(record_id)};' + ';'.join(
            input('Введите фамилию, имя, отчество, номер телефона через пробел\n').split()[:4]) + ';\n'
        confirm = confirmation('изменение')
        if confirm == 'y':
            replace_record_line(file_name, record_id, replaced_line)


def delete_records(file_name: str):
    record_id = check_id_record(file_name, 'удалить')
    if record_id != 'q':
        confirm = confirmation('удаление')
        if confirm == 'y':
            replace_record_line(file_name, record_id, '')

main('test.txt')