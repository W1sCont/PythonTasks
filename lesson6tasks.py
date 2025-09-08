#1 
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))

# for char in range(num1, num2 + 1):
#     if char % 3 == 0 and char % 5 != 0:
#         print(char)

# char = num1
# while char < num2:
#     char += 1
#     if char % 3 == 0 and char % 5 != 0:
#         print(char)



#2 
# number = int(input("Enter a number: "))
# result = 1
# for char in range(1, number + 1):
#     result *= char
# print(f"Факторіал числа {number} = {result}")




# 3 
# name = input("Enter your name: ")
# counter = 1
# char = len(name)
# while len(name) > 0:
#     print(name * counter)
#     counter += 1
#     char += len(name)
#     if char > 100:
#         break


#4 
# numbers = input("Введіть числа через пробіл: ")
# print(numbers)
# counter = 0
# counter_2 = 0
# for char in numbers:
#     if char in "2468":
#         counter += 1
#     elif char in "13579":
#         counter_2 += 1
# print(f"Парних чисел - {counter}\nНе парних чисел - {counter_2}")
       