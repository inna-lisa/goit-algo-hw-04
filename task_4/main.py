from task_4.command_handler import start, add_contact, change_contact, show_contact, show_all_contacts
from task_4.menu import bot_menu


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    contacts = {}
    bot_menu()

    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)

        match command:
            case 'start':
                print('Hello! How can I help you?')
                start()
            case 'add':
                add_contact(contacts, args)
                print('Contact added')
            case 'change':
                change_contact(contacts, args)
                print('Contact updated')
            case 'phone':
                print(show_contact(contacts, args))
            case 'all':
                print(show_all_contacts(contacts))
            case 'exit':
                print('Goodbye!')
                break
            case _:
                print(f'Unknown command: {command}')


if __name__ == '__main__':
    main()
