from colorama import Fore
from colorama import init

init(autoreset=True)


def file_structure(path, ident = ''):
    if not path.is_dir():
        print(Fore.RED + 'It is not a directory')
        return

    for item in sorted(path.iterdir()):
        if item.is_dir():
            print(ident + Fore.BLUE + item.name)
            file_structure(item, ident + '    ')
        else:
            print(ident + Fore.GREEN + item.name)
