
# string = "Hello World!"
# 1 Case -методи

# print(string.upper()) призвоить до верхнього регістру

# print(string.lower()) до нижнього регістру

# s = "hi"
# s.upper()
# print(s)

# print("hElLo, wOrLd.".capitalize()) першу літеру робить великою всі інші маленькі
# print(string.swapcase())

# string.conut(" ")

# 2 bool-метод
# методи з припискою "is" повертають булевні значення

# print(string.islower())
# print("hello".isalpha())  True повертає тільки якщо всі символи це літери, пробіл чи щось інше вже видасть False
# print("1234".isdigit())  перевірка на цифри
# print("12334".isnumeric())
# print("World Hello Python Hi".istitle())
# print(string.startswith("He")) True якщо строка починається з вказаної підсктроки
# print(string.endswith("old")) True якщо закінчується


# 3 Методи для роботи з підстроками (substring)


# string = "Hello, world"

# print(string.index("l")) буква "l" на 2 індексі
# print(string.index("world"))

# print(string.find("l"))           аналогічно index але при не вірних даних не видає помилку
# print(string.find("world"))

# print(string.replace("l", "*")) дозволяє швидко заміняти якісь елементи __old на  _new
# print(string.replace("world", "$"))


# print("  a b sd r e   ".strip()) забирає пробіли з початку і в кінці
# print("||d|s|d|f|r||".strip("|"))


# 4 join та split

# words = "for while any if else return break"

# print(words.split())

# result = words.split()

# print(", ".join(result))

# print(', '.join(split_result))
# print('|'.join('abcdefgh'))
# print(''.join(str(number) for number in range(1, 101)))

# random.choice(строка)

# import random
# import string

# text = random.choice()
# password = ""
# for _ in range(10):
#     password += 
    
    
# print(password)


    # print("".join(random.choice(string.ascii_letters + string.digits)for _ in range(10)))


# string = input(': ')

# upper_count = 0
# lower_count = 0
# letters_count = 0
# digits_count = 0
# spaces_count = 0

# for char in string:
#     if char.isupper():
#         upper_count += 1
#     elif char.islower():
#         lower_count += 1

#     if char.isalpha():
#         letters_count += 1
#     elif char.isdigit():
#         digits_count += 1
#     elif char == ' ':
#         spaces_count += 1


# # =================

# upper_count = sum(1 for char in string if char.isupper())
# lower_count = sum(1 for char in string if char.islower())
# letters_count = sum(1 for char in string if char.isalpha())
# digits_count = sum(1 for char in string if char.isdigit())
# spaces_count = string.count(' ')

# # 1
# print(string[-1] + string[1:-1] + string[0])

# # 3
# n = int(input('n: '))

# print(string[:n].upper() + string[n:].lower())

# # 2
# print(' '.join(string.split()))