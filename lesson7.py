# numbers = input("Enter a numbers: ") + " "

# odd_count = 0
# even_count = 0
# memory = ""
# sum_of_numbers = 0

# for char in numbers:
#     if char != " ":
#         memory += char
#     else:
#         if not memory: # якщо меморі пуста то перезапускає і провіряє заново
#             continue

#         if int(memory) % 2 == 0:
#             odd_count += 1
#         else:
#             even_count += 1

#         sum_of_numbers += int(memory)
#         memory = " "
# print(f"odd {odd_count}")
# print(f"even {even_count}")
# print(F"summ {sum_of_numbers}")


# вкладені цикли

# for x in range(1, 11):
#     print(f"x = {x}")

#     for y in range(1, 11):
#         print(f"y = {y}")


# import random # робота з випадковими числами
# import time # робота з часом
# import math # математика
# import datetime # глобальна робота з датами
# import re # регулярні вирази (шаблони)
# import tkinter # робота з інтерфейсом

# # root = tkinter.Tk()

# # btn = tkinter.Button(root, text = "klick", command=lambda : print("Hi"))

# #pyqt5 install
# import string # містить шаблони та функції роботи зі строками

# import sqlite3 # робота з локальними даними
# import functools # функції
# import itertools # ітерації
# import csv # робота з csv
# import json # робота з json

# 4
# ragne_1 = int(input("Enter first range num: "))
# range_2 = int(input("Ente a second range num: "))
# user_number = int(input("Your number: "))

# R = range(ragne_1, range_2 + 1)
# if  range_1 >= user_number <= range_2:
#         for char in range(ragne_1, range_2):
#             print(char) 
# while not ragne_1 <= user_number <= range_2
#     print("Not in range")
#     user_number = int(input("Your number: "))

# while True:
#     user_number = int(input("Your number: "))
#     if user_number in R:
#         break

# for n in R:
#     print(n if n != user_number else f"!{n}!", end = " ")



# # 4
# start = int(input('Start: '))
# end = int(input('End: '))

# R = range(start, end + 1)

# # number = int(input('Число з діапазону: '))
# #
# # while number not in R:
# #     print('Число не в діапазоні!')
# #     number = int(input('Число з діапазону: '))

# while True:
#     number = int(input('Число з діапазону: '))

#     if number in R:
#         break

#     print('Число не в діапазоні!')

# for n in R:
#     print(n if n != number else f'!{n}!', end=' ')

# 5

# 5
# start = int(input('Start: '))
# end = int(input('End: '))

# for number in range(start, end + 1):
#     for mult in range(1, 11):
#         print(f'{number} * {mult} = {number * mult}', end=' ')
#     print()
