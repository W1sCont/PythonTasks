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

# room = [
#     ['*', '*', '*', '*', '*',],
#     ['*', '*', '*', '*', '*',],
#     ['*', '*', 'R', '*', '*',],
#     ['*', '*', '*', '*', '*',],
#     ['*', '*', '*', '*', '*',]
# ]

# print(room[0])
# print(room[1])
# print(room[2])
# print(room[3])
# print(room[4])

# way = 2
# step = 2




# while True:
#     start_end = input("Press enter for star or 0 for break: ")
#     if start_end == "0":
#         print(room[0])
#         print(room[1])
#         print(room[2])
#         print(room[3])
#         print(room[4])
#         print()
#         break
        
#     while True:
#         way_input = input("Enter way (RIGHT(r), LEFT(l), UP(u), DOWN(d)): ").lower()
#         if way_input not in "rlud":
#             continue
#         step_input = int(input("Enter step or 0 to break: "))
#         if step_input not in range(5):
#             continue
#         elif step_input == 0:
#             print(room[0])
#             print(room[1])
#             print(room[2])
#             print(room[3])
#             print(room[4])
#             print()
#             break


#         raw = way
#         if 5 < raw < 0:
#             break
#         column = step
#         if 5 < column < 0:
#             break

#         if way_input == "r": # "right":
#             raw = way
#             column += step_input
#             if column >= 5:
#                 break

#         elif way_input == "l": #left":
#             raw = way
#             column -= step_input 
#             if column < 0:
#                 break
        
#         elif way_input == "u": #up":
#             column = column
#             raw -= step_input
#             if raw < 0:
#                 break

#         elif way_input == "d": #down":
#             column = column
#             raw += step_input
#             if raw >= 5:
#                 break


#         room[way][step] = "*"
#         room[raw][column] = "R"
#         way = raw
#         step = column

#         print(room[0])
#         print(room[1])
#         print(room[2])
#         print(room[3])
#         print(room[4])
#         print()
    


# 4
# ітерація у функціях означає що по них можна пройтись циклом від 0 до останньго і використати дані для потрібних дій