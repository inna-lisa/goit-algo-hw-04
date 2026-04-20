from task_2.get_cats import get_cats_info

def main():
    try:
        cats = get_cats_info('cats.txt')
        print(f'Cats: {cats}')
    except FileNotFoundError:
        print('File not found')

if __name__ == '__main__':
    main()
