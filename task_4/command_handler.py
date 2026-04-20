from task_4.menu import bot_menu


def start():
    print('Hello! How can I help you?')
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

    print('Contact added')


def change_contact(contacts, args):
    if len(args) < 2:
        print('Incorrect command')
        return
    if args[0] in contacts:
        contacts[args[0]] = args[1]
    else:
        print('Contact not found')

    print('Contact updated')
    pass


def show_contact(contacts, args):
    if len(args) < 1:
        print('Incorrect command')
        return
    print(contacts.get(args[0], 'Not found'))


def show_all_contacts(contacts):
    print(contacts)


def close_contact():
    print('Goodbye!')
