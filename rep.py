numbers = (input("Enter a number: "))

n1 = numbers[0]
n2 = numbers[1]
n3 = numbers[2]

if n1 == n2 and n2 == n3:
    print(3)
elif n1 == n2 or n2 == n3  or n2 == n3:
    print(2)
elif n1 != n2 and n2 != n3 and n1 !=n3:
    print(0)
