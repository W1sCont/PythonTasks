import string
# 1. Напишіть програму, що замінює всі великі літери у
# тексті, що вводить користувач, на зірочки(«*»).
# +++
# text = input("Enter your text: ")

# memory = ""
# for char in text:
#     if char.isupper():
#         memory += "*"
#     else:
#         memory += char
   
# print(memory)


#++
# 2. Дано рядок нулів та одиниць. Напишіть програму для
# знаходження найдовшої неперервної послідовності нулів у рядку.

# numbers = (input("Enter 0 1: "))
# memory = ""
# memory_len = 0
# count = 0

# for char in numbers:
#     if char == "0":
#         memory += char
#         count += 1
#     elif char != "0":
#         if count > memory_len:
#             memory_len = count
#             memory = ""
#             count = 0
    
# print(memory_len)


# 3. Напишіть програму, що приймає строку від
# користувача та знаходить:
# a. Символ, що трапляється найбільшу кількість разів.
# b. Кількість знаків пунктуації.
# c. Літери алфавіту, що не були знайдені у тексті.
# d. Кількість унікальних символів (тобто, загальна
# кількість елементів строки, що не повторюються)

# text = input("Enter your text: ")

# symbol = 0
# punkt = 0
# alpha_not = []
# # d
# unic_symb = len(set(text))

# count = 0
# symb_count = 0
# memory_punkt = ""
# memory_p = ""
# memory_symb = ""
# memory_alph = []

# for char in text:
#     # a
#     if char != " ":
#         symb_count = text.count(char)
#         if symb_count > symbol:
#             memory_symb = char
#             symbol = symb_count
#             symb_count = 0
#     # b
#     if char in string.punctuation:
#             memory_p += char
#             if memory_p not in memory_punkt:
#                 memory_punkt += char
#                 punkt += 1
#                 memory_p = ""
#     # c
# lowercase_alphabet = string.ascii_lowercase
# for alph in lowercase_alphabet:
#     if alph not in text:
#         memory_alph.append(alph)


# print(f"a. Символ, що трапляється найбільшу кількість разів: {symbol} ({memory_symb})")
# print(f"b. Кількість знаків пунктуації: {punkt} ({memory_punkt})")
# print(f"c. Літери алфавіту, що не були знайдені у тексті. {set(memory_alph)}")
# # d
# print(f"d. Кількість унікальних символів - {unic_symb} ")





# 4. Дано два слова. Складіть програму, що визначає чи
# можна чи ні з букв слова A скласти слово B. Програма не має
# враховувати регістр літер введених слів.

# word_1 = input("Введіть слово: ")
# word_2 = input("Введіть слово для перевірки: ")
# for char in word_2:
#     if word_1.count(char) < word_2.count(char):
#         print("Слово скласти не можна")
#         break
# else:
#     print("Слово скласти можна")
 


# ++
# 5. *Напишіть програму, яка зчитує рядок, кодує її
# запропонованим алгоритмом і виводить закодовану
# послідовність. Кодування повинно враховувати регістр символів.
# Правила кодування: групи однакових символів початкового
# рядка замінюються на цей символ і кількість його повторень в
# цій позиції рядка. Наприклад: рядок aaaabbbсaa кодується в
# a4b3с1a2

# text = input("Enter your text: ")

# memory = ""
# result = ""
# count = 0

# for char in text:
#     if char not in memory:
#         if count != 0:
#             result += str(count)
#         result += char
#         memory = ""
#         count = 0
#         memory += char
#         count += 1
#     elif char in memory:
#         memory += char
#         count += 1
# result += str(count) 
# print(result)

