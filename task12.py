# 5
# def camel_case(word):
#     result = []
#     word = word.split("_")
#     for el in word:
#         result.append(el.capitalize())

#     result = "".join(result)
#     return result
    

# print(camel_case("my_class_work"))

# 7
# def element_counter(words):
#     result = {}

#     for el in set(words):   
#         result[el] = words.count(el)

#     return result


# words = "the quick brown fox jumps over the lazy dog"
# result = element_counter(words) 
# res = {}   
# for key,value in result.items():
#     if value != 1:
#         res[key] = value  
        
# print(res)

# 9

# first = {
#     "first aid kit": 1,
#     "lighter": 2,
#     "sunglasses": 1,
#     "trousers": 2,
#     "socks": 4,
#     "sleeping bag": 1,
#     "hygienic set": 2,
#     "flashlight": 1,
#     "footwear": 2,
#     "tent": 1,
#     "woolen gloves": 1,
#     "dishes": 2,
#     "cap": 1
# }

# second = {
#     "first aid kit": 1,
#     "lighter": 2,
#     "sunglasses": 1,
#     "trousers": 2,
#     "socks": 4,
#     "sleeping bag": 1,
#     "hygienic set": 2,
#     "flashlight": 1,
#     "footwear": 2,
#     "t-shirts": 2,
#     "poncho": 2,
#     "batteries": 4
# }

# first_set = set(first)
# second_set = set(second)


# first_dif = first_set.difference(second_set)
# second_dif = second_set.difference(first_set)
# both = first_set.intersection(second_set)

# print("Only in the first: ")
# for el in first_dif:
#     print(f"{el}: {first[el]}")

# print()

# print("Only in the second: ")
# for el in second_dif:
#     print(f"{el}: {second[el]}")

# print()

# print("In both: ")
# for el in both:
#     print(f"{el}: {first[el] + second[el]}")



# 10

# numbers = ("6 0 3 0 5 0 0 4").split()

# for el in numbers:
#     if el == "0":
#         numbers.remove(el)
#         numbers.append(el)

# print(numbers)

# 11

# rome_code = {
#     1000: "M",
#     900: "CM",
#     500: "D",
#     400: "CD",
#     100: "C",
#     90: "XC",
#     50: "L",
#     40: "XL",
#     10: "X",
#     9: "IX",
#     5: "V",
#     4: "IV",
#     1: "I"
# }



# numbers = int(input("Enter a number for 1 to 4000: "))
# result = ""

# for char in rome_code:
#     while numbers - char >= 0:
#         result += rome_code[char]
#         numbers -= char
#         continue

# print(result)


# 12

room = [
    ['*', '*', '*', '*', '*',],
    ['*', '*', '*', '*', '*',],
    ['*', '*', 'R', '*', '*',],
    ['*', '*', '*', '*', '*',],
    ['*', '*', '*', '*', '*',]
]

print(room[0])
print(room[1])
print(room[2])
print(room[3])
print(room[4])

# raw_input = (input("Enter way (RIGHT, LEFT, UP, DOWN): "))
# column_input = int(input("Enter step: "))

way = 2
step = 2

while True:
    
    raw = way
    column = step
    way_input = input("Enter way (RIGHT, LEFT, UP, DOWN): ").lower()
    step_input = int(input("Enter step or 0 to break: "))

    if way_input == "0":
        break
        
    # if 0 > raw < 4:         # зробити перевірку поля
    #     continue
    # if 0 > column < 4:
    #     continue

    if way_input == "r": # "right":
        raw = way
        column += step_input
    elif way_input == "l": #left":
        raw = way
        column -= step_input 
    elif way_input == "u": #up":
        raw -= step_input
        column = column
    elif way_input == "d": #down":
        raw += step_input
        column = column

    room[way][step] = "*"
    room[raw][column] = "R"
    way = raw
    step = column

    print(room[0])
    print(room[1])
    print(room[2])
    print(room[3])
    print(room[4])
    print()

    

    
    

# print(room[0])
# print(room[1])
# print(room[2])
# print(room[3])
# print(room[4])








