
'''
json_data = [worker, worker, ...]

worker = {
    name: str,
    age: int,
    skills: [str, str, ...]
}
'''
import json


# при виклику фунції новий робітник доповнює json-файл
def add_worker(name: str, age: int, skills: list[str]):
    try:
        with open('files\\workers.json', 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = []

    new_worker = {
        'name': name,
        'age': age,
        'skills': skills
    }

    data.append(new_worker)

    with open('files\\workers.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)


# при виклику функції виводяться всі робітники, які записані в файлі
def print_workers():
    try:
        with open('files\\workers.json', 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        print('Робітників немає!')
        return

    for worker in data:
        print(f'-{worker['name']}, {worker['age']}років. Навички: ')

        for skill in worker['skills']:
            print(f'\t{skill}')


def main():
    while True:
        print('1 - Додати робітника')
        print('2 - Вивести робітників')
        print('0 - Вихід')

        choice = input('Вибір: ')

        match choice:
            case '1':
                name = input('Введіть ім`я нового робітника: ')
                age = int(input('Введіть вік нового робітника: '))
                skills = input('Введіть навички через пробіл: ').split()

                add_worker(name, age, skills)
            case '2':
                print_workers()
            case '0':
                break
            case _:
                print('Невідома команда!')

if __name__ == '__main__':
    main()
