number = float(input("Enter a number: "))

if number % 2 == 0:
    number = str(number)
    print(number[:-2])
elif number % 2 == 1:
    number = str(number)
    print(number[:-2])
else:
    print(number)


