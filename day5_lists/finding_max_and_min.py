n = int(input("Enter number of integers: "))
a = []
for i in range(n):
    readings = float(input(f"Enter readings{i+1} :"))
    a.append(readings)
print(f"maximum is: {max(a)} and minimum is : {min(a)} ")