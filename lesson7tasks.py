# 1
# counter = 0

# for num in range(100,1000):

#     num = str(num)
#     if num[0] == num[1]:
#         counter += 1
        
#     elif num[1] == num[2]:
#         counter += 1
        
#     elif num[0] == num[2]:
#         counter += 1

# print(f"В діапазоні від 100 до 999 є {counter} числа у яких дві однакові цифри")

# 2
# numbers = range(2, 100)
# counter = 0
# for char in numbers:
#     if char % 2 == 0 and char % 3 == 0 or char % 3 == 0 and char % 5 == 0 or char % 2 == 0 and char % 5 == 0:
#         counter += 1
#         print(counter, char)

# print(counter)


# 3

# user_number = input("Enter a number: ")
# memory = ""
# dell_3 = "3"
# dell_6 = "6"

# for char in user_number:
#     if char != dell_3 and char != dell_6:
#         memory += char
    
# print(memory)
   
# 4
# ragne_1 = int(input("Enter first range num: "))
# range_2 = int(input("Ente a second range num: "))
# user_number = int(input("Your number: "))

# while True:
#     if user_number not in range(ragne_1, range_2 + 1):
#         print("Number not in range")
#         user_number = int(input("Your number: "))
#     else:
#         break
# for char in range(ragne_1, range_2 + 1):
#     print(char if char != user_number else f"!{user_number}!", end=" ")





# 5
# num1 = int(input("Enter number: "))
# num2 = int(input("Enter srcond number: "))

# for char in range(num1, num2 + 1):
#     print()
#     for n in range(1, 11):
#         print(f"{char} * {n} = {char*n}", end=" ")
        
