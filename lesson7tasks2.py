# 1
# numbers = int(input("Скільки чисел потрібно ввести?: "))
# memory = ""
# for char in range(1, numbers +1):
#     user_num = input(f"Введіть число {char}: ")
#     memory +=  user_num + " "

# print(memory, end=" ")


# 2 
# text = input("Введіть текст: ")

# counter = 0
# for char in text.lower():
#     if char in "аяоуюеєиії":
#         counter += 1
#     elif char in "aeiouy":
#         counter += 1

# print(F"В тексті {counter} голосних букв" if counter > 1 else f"В тексті {counter} голосна буква")

# # 3
# text = input("Text: ") + " "
# text_len = int(input("number: "))

# memory = ""
# counter = 0

# for char in text:
    
#     if char not in "/?.,><:;''}{[]=+-()":
#         memory += char 

#         if char == " ":
#             if text_len + 1 == len(memory):
#                 counter += 1
#             memory = ""
                        
# print(f"В тексті {counter} слова у яких {text_len} літер" if counter <= 5 else f"В тексті {counter} слів у яких {text_len} літер")


