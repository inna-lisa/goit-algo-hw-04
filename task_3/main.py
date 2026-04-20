import sys
from pathlib import Path
from colorama import Fore
from task_3.file_structure import file_structure

def main():
    path = None
    if len(sys.argv) == 2:
        path = Path(sys.argv[1])
    elif len(sys.argv) == 1:
        path = Path(__file__).parent.parent
    else:
        print(Fore.RED + 'Enter path to file')
        return
    try:
        file_structure(path)
    except FileNotFoundError:
        print('File not found')

if __name__ == '__main__':
    main()
