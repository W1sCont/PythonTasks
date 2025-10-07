# list_1 = []
# list_2 = ["Peter"]
# list_3 = ["Peter", "Alex"]
# list_4 = ["Jacob", "Alex", "Mark"]
# list_5 = ["Jacob", "Alex", "Mark", "Max"]

# def likes(list: list):
#     if len(list) == 0:
#         return ("no one likes this")
#     elif len(list) == 1:
#         return (f"{list[0]} likes this")
#     elif len(list) == 2:
#         return (f"{list[0]} and {list[1]} likes this")
#     elif len(list) == 3:
#         return (f"{list[0]}, {list[1]} and {list[2]} likes this")
#     elif len(list) >= 4:
#         return (f"{list[0]}, {list[1]} and {len(list) - 2} likes this")


# print(likes(list_1))
# print(likes(list_2))
# print(likes(list_3))
# print(likes(list_4))
# print(likes(list_5))


# 2 дбагер поміг)

# def persistence(num: int):
#     result = 1
#     count = 0
#     while True:
#         if num < 10:                       
#             return count
        
#         for el in (str(num)):
#             result *= int(el)
#         count += 1     
#         num = result
#         result = 1
        
# print(persistence(999))


# 3 

# def heshteg(text: str):
#     if text == "":
#         return False
#     elif len(text) >= 140:
#         return False
#     return (f"#{"".join(text.split())}")


# print(heshteg("Hello, word!"))