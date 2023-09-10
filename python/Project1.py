x = int(input("Take one of the units for coversion: 1. Fahrenheit to Celsius 2. Celsius to Fahrenheit: "))
C=0
F=0
if x == 1:
    F= int(input("Enter the amount in Fahrenheit: "))
    C = ((F-32) * 5)/9
    print("The temperature in Celsius is: ", C)
elif x == 2:
    C=int(input("Enter the amount in Celsius: "))
    F = (C* (9/5)) + 32
    print("The temperature in Fahrenheit is: ",F)
else:
    print("Invalid input! Press 1 or 2")
