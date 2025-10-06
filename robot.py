
room = [
['*', '*', '*', '*', '*',],
['*', '*', '*', '*', '*',],
['*', '*', 'R', '*', '*',],
['*', '*', '*', '*', '*',],
['*', '*', '*', '*', '*',]
]

robot_row = 2
robot_column = 2


def print_room(robot_room: list):
    for row in robot_room:
       print(' '.join(row))


def choice_is_correct(user_choice: str):  # UP 5
    user_choice = user_choice.split()

    if len(user_choice) != 2:
        return False

    if user_choice[0].lower() not in ('up', 'down', 'left', 'right'):
        return False

    if not user_choice[1].isdigit():
        return False

    return True


def move(direction: str, distance: int):
    room[robot_row][robot_column] = '*'

    match direction.lower():
        case 'up':
            change_robot_row(-distance)
        case 'down':
            change_robot_row(distance)
        case 'left':
            change_robot_column(-distance)
        case 'right':
            change_robot_column(distance)

    room[robot_row][robot_column] = 'R'


def change_robot_row(distance: int):
    global robot_row

    robot_row += distance

    # 1-й спосіб
    if robot_row < 0:
        robot_row = 0

    if robot_row > 4:
        robot_row = 4


def change_robot_column(distance: int):
    global robot_column

    robot_column += distance

    # 2-й спосіб
    robot_column = max(0, robot_column)
    robot_column = min(4, robot_column)


def get_split_result(user_choice: str):
    user_choice = user_choice.split()
    
    return user_choice[0], int(user_choice[1])


def main():
    while True:
        print_room(room)
        choice = input('Введіть команду руху(НАПРЯМ КІЛЬКІСТЬ): ')
        
        if choice == '0':
            print('Дякую за гру!')
            break

        if not choice_is_correct(choice):
            print('Невірна команда!')
            continue

        dir, dis = get_split_result(choice)

        move(dir, dis)


if __name__ == '__main__':  # перевірка, що файл запускається вручну
    main()


