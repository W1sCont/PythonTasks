import random

# 1. Заповніть список випадковими цілими числами (не менше
# десяти штук). У цьому списку, потрібно визначити мінімальний і
# максимальний елементи, порахувати кількість від'ємних
# елементів, порахувати кількість додатних елементів, порахувати
# кількість нулів. Результати вивести на екран.

numbers = [random.randint(-20, 20) for _ in range(10)]
memory_minus = []
memory_plus = []
zero = 0
print(numbers)
for char in numbers:
    if char < 0:
        memory_minus.append(char)
    elif char > 0:
        memory_plus.append(char)
    else:
        zero += 1

print(f"мінімальний елемент {min(numbers)}")
print(f"максимальний елемент {max(numbers)}")
print(memory_minus) # дописати саме к-сть
print(memory_plus)
print(zero)

# 2. Дан список з словами. Залиште в цьому списку лише слова,
# що починаються з великої літери.

# text = input("Enter your text: ").split()
# memory = []

# for ls in text:
#     if ls[0].isupper():
#         memory.append(ls)
# print(" ".join(memory))



# 3. Дан список цілих чисел. Знайдіть в ньому ті числа, що
# з’являється непарну кількість разів. Кожен елемент повинен
# виводитись тільки один раз!!!

# numbers = input("Enter your numbers: ").split()
# # numbers = [23, 10, 2, 1, 23, 5, 2, 2, 1, 23, 2, 2, 10, 7, 7, 7, 7, 7, 7]
# num_set = set(numbers)
# count = 0
# list_nums = []

# for char in num_set:
#     count = numbers.count(char)
#     if count % 2 != 0:
#         list_nums.append(char)
#         count = 0

# print(" ".join(list_nums))


# 4. Дан список (types_list) з даними всіх основних типів, що є в
# Python. Перенесіть дані із types_list у нові списки, кожен з яких
# відповідає своєму типу даних (list_int, list_str, list_bool,
# list_float). В кожному списку повинні бути лише ті дані, яким
# він відповідає.




# 5. Напишіть програму, яка приймає два списки чисел від
# користувача і створює новий список, що містить суму елементів
# з однаковими індексами двох вихідних списків. Виведіть
# отриманий список на екрані. Передбачається, що списки мають
# однакову довжину. Наприклад, якщо користувач вводить списки
# [1, 2, 3] та [4, 5, 6], програма повинна вивести [5, 7, 9].