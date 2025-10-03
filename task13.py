# 1
# def calculator(a:float, b:float, c:str):
#     if c == "+":
#         return a + b
#     elif c == "-":
#         return a - b
#     elif c == "*":
#         return a * b
#     elif c == "/":
#         return a / b
#     else:
#         print("Unknown operation")

# num_1 = float(input("Enter number 1: "))
# num_2 = float(input("Enter number 2: "))
# operacion = input("Enter operacion (+ - * /): ")
# print(calculator(num_1, num_2, operacion))

# 2
# def is_palindrome(word):
#     rev = "".join(reversed(word))
#     if word == rev:
#         return True
#     else:
#         return False
    
# word = input("Enter word: ")
# print(is_palindrome(word))

# 3
# def teg_word(teg: str, word: str):
#     return (f"<{teg}>") + word + (f"</{teg}>")


# teg = input("Enter teg: ")
# word = input("Enter word: ")
# print(teg_word(teg, word))

# 4
# def is_prime(n):
#     if n == 1:
#         return False
#     elif n == 2:
#         return True
#     elif n % 2 != 0 and n % 3 != 0:
#         return True
#     else:
#         return False
    
# number = int(input("Enter natural number:"))
# print(is_prime(number))

# 5
# def count_vowels_consonants(word):
#     word = word.lower()
#     count_golosni = 0
#     count_prygolosni = 0
#     for el in list(word):
#         if el in "aeiou" or el in "аяоуюеєиії":
#             count_golosni += 1
#         else:
#             count_prygolosni += 1
#     return (f"Голосних - {count_golosni}\nПриголосних - {count_prygolosni}")
        

# word = input("Enter word: ")
# print(count_vowels_consonants(word))

