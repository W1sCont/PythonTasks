# class MyExcprion(Exception):
#     def __str__(self):
#         return "Моя валасна помилка"


# def raiser(n):
#     match n:
#         case 1:
#             raise ValueError("Це моя власна помилка")
#         case 2:
#             raise ZeroDivisionError
#         case 3:
#             raise IndexError("Це моя власна помилка")
#         case 4:
#             raise KeyError
#         case 5:
#             raise MyExcprion
        



# try:
#     raiser(5)
#     number_1 = int(input("ent num 1:"))
#     number_2 = int(input("ent num 2:"))

#     result = number_1 / number_2

#     print(result)


# except ValueError:
#     print("Ви ввели не число")

# except ZeroDivisionError:
#     print("На 0 ділити не можна")

# # except Exception as exc:
# #     print(f"Сталася інша помилка: {exc}")

# else:
#     print("Else")

# finally:
#     print("Finally")


# ---- write
# file = open("C:\\Users\\tmros\\OneDrive\\Робочий стіл\\GitHub\\PythonTasks\\files\\data.txt")   абсолютний шлях
# file = open("files\\data.txt", "w") # локальний шлях
# w - повністю перезаписує відкритий чи створений файл
# 1
# file.write("Hello world!\n")

# 2
# print("hello, print", file=file, end="\n")
# print("hello, print", file=file)


# file.close()


# ---- read

# file = open("files\\data.txt", "r")

# print(file.read())
# print(file.read())
# читання одного рядку
# print(file.readline())
# print(file.readline())
# print(file.read())
# file.seek(0) # переміщення курсору на 0 позицію
# # 3 
# for line in file:
#     print(line, end="")

# file.seek(0)
# for index, line in enumerate(file, start=1):
#     print(f"{index}, {line}", end="")

# # 4
# file.seek(0)
# print(file.readlines())
# file.close()

# ----------------append запис з збереженням (не перезаписує файл)

with open("files\\data.txt", "a", encoding="UTF-8") as file:
    print("Привіт", file=file)


