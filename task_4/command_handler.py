from task_4.menu import bot_menu


def start():
    bot_menu()


def add_contact(contacts, args):
    if len(args) < 2:
        print('Incorrect command')
        return

    if args[0] in contacts:
        print(f'Contact already exists. Contact name will be: {args[0] + '1'}')
        contacts[args[0] + '1'] = args[1]
    else:
        contacts[args[0]] = args[1]


def change_contact(contacts, args):
    if len(args) < 2:
        print('Incorrect command')
        return
    if args[0] in contacts:
        contacts[args[0]] = args[1]
    else:
        print('Contact not found')


def show_contact(contacts, args):
    if len(args) < 1:
        return None, 'Incorrect command'
    return contacts.get(args[0], 'Not found')


def show_all_contacts(contacts):
    return contacts
