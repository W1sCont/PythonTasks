num_1 = float(input("Enter 1 number: "))
operation = input("Enter operacion (+-*/): ")
num_2 = float(input("Enter 2 number: "))

if operation == "+":
    print(num_1 + num_2)
elif operation == "-":
    print(num_1 - num_2)
elif operation == "*":
    print(num_1 * num_2)
elif operation == "/":
    # if num_2 != 0:
    #     print(num_1 / num_2)
    # else:
    #     print("Error")    
    print(num_1 / num_2 if num_2 != 0 else "Error")
else:
    print("Enter correct data!")      

    # elif operation == "/":
    #     pass - заглушка для пропуску     