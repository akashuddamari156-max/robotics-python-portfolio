n = int(input("Enter number of integers: "))
a = []

for i in range(n):
    readings = float(input(f"Enter readings{i+1} :"))
    a.append(readings)

max_value = 0
min_value = 0

for value in a:
    if max_value < value:
        max_value = value
    if min_value > value:
        min_value = value

print(f"maximum is {max_value}")
print("minnimum is ",min_value)
