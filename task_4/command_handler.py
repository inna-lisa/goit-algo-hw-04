def add_contact(contacts, args):
    if len(args) < 2:
        return 'Incorrect command'

    if args[0] in contacts:
        contacts[args[0] + '1'] = args[1]
        return f'Contact name is already exists. New contact name will be: {args[0] + '1'}'
    else:
        contacts[args[0]] = args[1]
        return 'Contact added'


def change_contact(contacts, args):
    if len(args) < 2:
        return 'Incorrect command'
    if args[0] in contacts:
        contacts[args[0]] = args[1]
        return 'Contact updated'
    else:
        return 'Contact not found'


def show_contact(contacts, args):
    if len(args) < 1:
        return None, 'Incorrect command'
    return contacts.get(args[0], 'Not found')


def show_all_contacts(contacts):
    return contacts
