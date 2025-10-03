import random
import string

# 5
# words = "my_first_variable_in_python".split("_")

# 5.1
# result = ""

# for w in words:
#     result += w.capitalize()

# print(result)

# 5.2

# print("".join(w.capitalize() for w in words))

# 7
text = "the quick brown fox jump over the lazy dog"

# 7.1
# result = {char: text.count(char) for char in text}

# print(result)

# 7.2
# result = {}
# for char in text:
#     if char in result:
#         result[char] += 1
#     else:
#         result[char] = 1

# print(result)

# 7.3

# result3 = {}
# for char in text:
#     result3[char] = result3.get(char, 0) + 1

# print(result3)


# 00000

# numbers = [10, 0, 9, 0, 0, 1, 2, 3, 0, 0, 5, 2, 1]
# for el in numbers:
#     if el == 0:
#         numbers.remove(0)
#         numbers.append(0)
# print(numbers)

# first = {
#     1: 23,
#     2: 22
# }
# second = {
#     1:22,
#     2:44
# }

# print("spilni rechi")
# for key in set(first).intersection(second):
#     print(f" {key}: {first[key] + second[key]}")

# print(set(first) & set(second))
# print(set(first).intersection(second))

# funkcii

def say_hello(): # def nazwa(parametry): kod
    print("Hello")


def say_hello_for_name(name: str) -> str:
    print(f"Hello, {name}!")


def sum_of_two_numbers(a: int | float, b: int | float):
    return a + b # повертає результат функції


def counter(n):
    for number in range(1, n + 1):
        return number # після виконання закриває функцію (як break в циклі)


def password_generator(password_len):
    if password_len not in range(8, 26):
        return 

    password = ""

    for _ in range(password_len):
        password += random.choice(string.ascii_letters + string.digits)

    return password


print(counter(25))

say_hello() # wyklyk funkcii
say_hello_for_name("Rostik")

result = sum_of_two_numbers(10, 20)
print(f"Result: {result}")

print(sum_of_two_numbers(sum_of_two_numbers(1, 4), sum_of_two_numbers(5, 10)))


print(password_generator(-5))
print(password_generator(10))
print(password_generator(599))
print(password_generator(9))