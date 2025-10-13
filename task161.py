

# 1
def all_files_in_one(*args):
    for el in args:
        with open(el, 'r', encoding="UTF-8") as file:
            with open("files\\all_files_in_one.txt", "a+", encoding="UTF-8") as new_file:
                for line in file:
                    print(line, file=new_file, end="")
                    print(line, end="")
                    

# all_files_in_one("files\\data.txt", "files\\input.txt")

# 2

def raiser():
    raise IndexError


def print_list(list):
    try:
        # raiser() # виклик помилки через функцію
        for index, el in enumerate(list, start=1):
            print(f"i={index}, element={el}")
            print(list[10]) # помилка якщо індексів буде менше ніж 10 
    except IndexError:
        print("Цикл запустився, виконав першу ітерацію і при спробі знайти і=10 показав помилку IndexError")


# user_list = input("Enter your list: ")
list_test = [1,2,4,5]
# print_list(list_test)

# 3
def open_file(*args):
    try:
        for el in args:
            with open(el, 'r', encoding="UTF-8") as file:
                for line in file:
                    print(line, end="")

    except FileNotFoundError:
        print("File nor found!")


# open_file("files\\not_found_file.txt")