# 1
# count = 0

# for number in range(100, 1000):

    # var 1
    # number = str(number)

    # if number[0] == number[1] or number[0] == number[2] or number[1] == number[2]:
    #     count += 1
    
    # var 2
    # memory = ''
    # for digit in str(number):
    #     if digit not in memory:
    #         memory += digit
    #     else:
    #         count += 1
    #         break

#     var 3
#     number = str(number)

#     if len(number) > len(set(number)):
#         count += 1

# print(count)

# number = 12542251
# number = str(number)
# print(set(number)) 


# 2

# count = 0
# for number in range(2,100):
#     is_break = False
#     for divider in range(2, number):
#         if number % divider == 0:
#             is_break = True
#             break
        
#         if not is_break:
#             count += 1
# print(count)

    
#     for divider in range(2, number):
#         if number % divider == 0:
#             break
#     else:
#         count += 1
# print(count)

# 3

# number = int(input(": "))

# new_number = ""

# for digit in number:
#     if digit not in "36":
#         new_number += digit

# print(f"New number: {new_number}")


# text = "Hello, world! I'm learning python!"
# find_len = int(input("len text: "))
# counter = 0
# word = ""

# for char in text:
#     if char not in ".,!?;: '":
#         word += char
#     else:
#         if len(word) == find_len:
#             counter += 1
#             word = ""

# print(counter)

