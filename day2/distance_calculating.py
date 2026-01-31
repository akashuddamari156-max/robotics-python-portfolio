import math
x1 = float(input("Enter X1 "))
x2 = float(input("Enter x2 "))
y1 = float(input("Enter y1 "))
y2 = float(input("Enter y2 "))

Distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"Distance is:{Distance:.2f}")