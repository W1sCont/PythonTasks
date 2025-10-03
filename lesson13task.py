# 608
def copy_text(text: str, n: int):
    return text * n

print(copy_text("Hi pythot ", 3))

# 611
def cut_word(word: str, n: int):
    return word[:n]

print(cut_word("Java", 2))

# 624
def word_return(text_1, text_2):
    return text_1[:int(len(text_1) // 2)] + text_2 + text_1[int(len(text_1) // 2):]

print(word_return("[111555]", "Hi!"))