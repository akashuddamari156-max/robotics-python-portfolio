x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))
operator = input("Enter operator add/subtract/multiply/division: ").lower()

add = x + y
subtract = x - y
multiply = x * y
division = x / y

if operator == "add":
    print(add)
elif operator == "subtract":
    print(subtract)
elif operator == "multiply":
    print(multiply)

elif operator == "division":
    if y != 0 :
        print(division)
    else:
        print("Invalid input of y")

else:
    print("Invalid operator")