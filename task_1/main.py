from task_1.total_salary import total_salary

def main():
    try:
        salary, average = total_salary('salary.txt')
        print(f'Total salary: {salary}, Average salary: {average}')
    except FileNotFoundError:
        print('File not found')

if __name__ == '__main__':
    main()
