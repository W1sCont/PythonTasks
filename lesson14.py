# 1
# def str_dubl(text):
#     result = ""
#     for num, el in enumerate(text, 1):
#         result += "".join(el*num).capitalize() + (f"{"" if num == len(text) else "-"}")
   
#     return result

# print(str_dubl("dssshwje"))

# 2
# def five_el_words_revers(text):
#     text = text.split()
#     result = ""
#     for el in text:
#         if len(el) >= 5:
#             result += "".join(reversed(el)) + " "
#         else:
#             result += el + " "

#     return result

# print(five_el_words_revers("Hey its python program"))