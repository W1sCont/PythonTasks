# day = int(input("Enter day number: "))
# match day:
#     case 1:
#         print("Ponedilok")
#     case 2:
#         print("Vivtorok")
#     case 3:
#         print("Sereda")
#     case 4:
#         print("Chetver")
#     case 5:
#         print("Piatnytcia")
#     case 6:
#         print("Subote")
#     case 7:
#         print("Nedilia")
#     case _:
#         print("Error")  # аналог else


# num = int(input("Введіть номер місяця "))

# match num:
#     case 1:
#         print("Січень " + "Зима")
#     case 2:
#         print("Лютий " + "Зима")
#     case 3:
#         print("Березень " + "Весна")
#     case 4:
#         print("Квітень " + "Весна")
#     case 5:
#         print("Травень " + "Весна")
#     case 6:
#         print("Червень " + "Літо")
#     case 7:
#         print("Липень " + "Літо")
#     case 8:
#         print("Серпень " + "Літо")
#     case 9:
#         print("Вересень " + "Осінь")
#     case 10:
#         print("Жовтень " + "Осінь")
#     case 11:
#         print("Листопад " + "Осінь")
#     case 12:
#         print("Грудень" + "Зима")
#     case _:
#         print("Error")


# month = int(input("Enter number of month "))
# match month:
#     case 12 | 1 | 2:
#         print("Зима")
#     case 3 | 4| 5:
#         print("Весна")
#     case 6 | 7 | 8:
#         print("Літо")
#     case 9 | 10 | 11:
#         print("Осінь")
#     case _:
#         print("Такого місяця не має")

# Користувач вводить шестизначне число
# скажіть чи це число щасливе
# Щасливим числом  вважається якщо сума перших 3 чисел дорівнює сумі останнім 3 числам
# 103220 - щасливе 

number = (input("Ввудіть 6 значне число: "))

if len(number)  == 6:
    sum_of_first_part = int(number[0]) + int(number[1]) + int(number[2])
    sum_of_last_part = int(number[3]) + int(number[4]) + int(number[5])
#     if sum_of_first_part == sum_of_last_part:
#         print("Lucky")
#     else:
#         print("Число щасливе!")
# else:
#     print("no 6")

    # print(f"{"" if sum_of_first_part == sum_of_last_part else "не "}щасливе")


