temp = float(input("Enter temp: "))
if temp <= 0:
    print("A cold, isn't it?")
elif temp > 0 and temp < 10:
    print("Cool")
else:
    print("Nice wheather we're having.")