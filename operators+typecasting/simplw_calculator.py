x = float(input("Enter value of x: "))
y = float(input("Enter value of y: "))

sum = x + y
diff = x - y
product = x * y
print(f"sum is: {sum} , difference is: {diff} , product is: {product} ")


if y != 0:
    div = x / y
    print(f"division is: {div}")
else:
    print("Invalid input of y")
