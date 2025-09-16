# 1 1  ++

# Напишіть програму, яка знаходить всі числа Армстронга в
# заданому діапазоні. Число Армстронга - це таке число, яке
# дорівнює сумі своїх цифр, піднятих до ступеня, рівного
# кількості цифр у числі. Наприклад, 153 є числом
# Армстронга, оскільки 1^3 + 5^3 + 3^3 = 153

# len_1 = int(input("Enter first num: "))
# len_2 = int(input("Enter second num: "))

# sum = 0

# for char in range(len_1, len_2):
#     len_char = len(str(char))
#     for digit in str(char):
#         deg = int(digit) ** len_char
#         sum += deg
#     if sum == char:
#         print (f"Armstr {sum} ")
#     sum = 0
       

# 1 2  ++

# Дана строка. Зсуньте всі знаки пунктуації та пробіли на
# кінець строки. Приклад: «Привіт, я просто тестую. Це
# звичайний текст!!» -> «ПривітяпростотестуюЦезвичайний
# текст, . !!»

# text = input("Enter text: ")

# memory = ""

# znak = ""

# for char in text:
#     if char not in "?!.,>,<':; }+-=)( []/@#":
#         memory += char
#     else:
#         znak += char

# print(f"{memory}{znak}")


# 1 3 ++
# Дан рядок. Порахуйте, скільки символів у рядку
# зустрічаються у ньому більше ніж один раз.

# text = input("Enter text: ")

# count = 0
# memory = ""
# memory_2 = ""
# text_set = set(text)
# for char in text:
#     if char in memory:
#         memory_2 += char
#     else:
#         memory += char

# for i in text_set:
#     if i in memory_2:
#         count += 1 

# print(count)

# i = 0
# while i < len(text):
#     for char in text:
#         if char > 1:
#             count += 1
#         i = i + 1


# print(count)



# 2 1  ++

# Напишіть програму, яка запитує у користувача цілі числа,
# доки він не введе 0, а потім виводить суму всіх введених
# чисел.

# sum = 0
# print("Enter 0 for break")
# while True:
#     number = int(input("Enter a numbers: "))
#     sum += number
#     if number == 0:
#         print(sum)
#         break


# 2 2  ++

# Користувач вводить текст і два символи (символ_1 та
# символ_2). Замініть всі символи_1 у тексті на символ_2.

# text = input("Enter text: ")
# symb_1 = input("Enter symb 1: ")
# symb_2 = input("Enter symb 2: ")

# memory = ""

# for char in text:
#     if char == symb_1:
#         memory += symb_2
#     elif char == symb_2:
#         memory += symb_1
#     else:
#         memory += char
    
# print(memory)
        

# 2 3 ++

# Напишіть програму, яка запитує у користувача число та
# виводить послідовність чисел Фібоначчі до цього числа за
# допомогою циклу while.

# гугл допомагав, формулу правильно зрозумів але не додумався як реалізувати цикл, перші два елементи списку я задав вручну для формули і вот тут (while i <= number - 2:) вже сам тупив
# number = int(input("Enter number: "))

# fibo_1 = 0
# fibo_2 = 1
# i = 0
# fibo = 0
# while i <= number - 2:
#     fibo = fibo_1 + fibo_2
#     fibo_1 = fibo_2
#     fibo_2 = fibo
#     i = i + 1
#     print(fibo, end=" ")


# 2 4 ++

# Напишіть програму, яка запитує у користувача рядок і
# виводить його у зворотному порядку. Використовуйте цикл
# for або цикл while для ітерації символів рядка у зворотному
# порядку.



# version 1  тут гугл дуже допоміг @_@

# text = input("Enter text: ")
# memory = text[::-1]
# print(memory)

# version 2

# text = input("Enter text: ")
# memory = []
# index = len(text) - 1
# result = ""

# while index >= 0:
#     memory.append(text[index])
#     index -= 1

# for char in memory:
#     result += char
# print(result)


# 2 5
# Напишіть програму, яка запитує у користувача рядок (великий
# текст), потім запитує ще один рядок з символами. Порахуйте,
# скільки у тексті користувача цих символів (кожного окремо).

