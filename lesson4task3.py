name = input("Enter your name: ")
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Привіт, " + name)
elif number % 3 == 0:
    print(number ** 2)
else:
    print("Bye!")