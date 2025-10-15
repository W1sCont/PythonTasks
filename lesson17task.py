import json
import datetime


now = datetime.datetime.now() # перевести в строку перед загрузкою в базу


def dump_json(data):
    with open('files\\diary.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)



def load_json():
    try:
        with open('files\\diary.json', 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = []
    
    return data


def new_data(title: str, content: str, date_time: str):
    data = {
        "title": title,
        "content": content,
        "date_time": date_time
    }
    return data


def print_data(data):
    if not data or data == []:
        print("Список пустий")
    else:
        for num, el in enumerate(data, start = 1):
            print(f"#{num} Заголовок: {el["title"]}")
            print(f"Запис: {el["content"]}")
            print(f"Дата запису: {el["date_time"]}")
            print()


def remove_el(el_for_remove: int, data):
    if 0 <= el_for_remove <= len(data):
        data.pop(el_for_remove - 1)
    else:
        return
            
    
def modify_data(el_for_modify: int, data):
    if 0 <= el_for_modify <= len(data):
        title = input("Введіть заголовок: ")
        content = input("Ваш запис:")
        date_time = "modify " + datetime.datetime.now().strftime("%H:%M %d-%m-%Y")

        data[el_for_modify - 1] = new_data(title, content, date_time)
        dump_json(data)
    else:
        return
    

def main():
    data = load_json()
    while True:
        print("1 - Новий запис")
        print("2 - Вивести дані")
        print("3 - Видалити запис")
        print("4 - Модифікувати запис")
        print("0 - Вихід")

        choice = input('Вибір: ')
        match choice:
            case "1":
                title = input("Введіть заголовок: ")
                content = input("Ваш запис:")
                date_time = "created " + datetime.datetime.now().strftime("%H:%M %d-%m-%Y")

                new_entry = new_data(title, content, date_time)
                data.append(new_entry)
                dump_json(data)
            case "2":
                print_data(data)
            case "3":
                el_for_remove = int(input("Вкажіть номер запису який бажаєте видалити: "))
                remove_el(el_for_remove, data)
                dump_json(data)
            case "4":
                el_for_modify = int(input("Вкажіть номер запису який бажаєте модифікувати: "))
                modify_data(el_for_modify, data)
            case "0":
                break
            case _:
                print('Невідома команда!')

    dump_json(data)




if __name__ == '__main__':
    main()