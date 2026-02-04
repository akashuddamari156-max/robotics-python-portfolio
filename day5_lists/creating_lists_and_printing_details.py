n = int(input("Enter number of readings: "))
a = []

for i in range(n):
    readings = float(input(f"ENter raeding{i+1}: "))
    a.append(readings)

print(f"the list is{a}")
print(f"length of list is {len(a)}")

if len(a) > 0 :
    print(f"first element is{a[0]} , last element is {a[-1]}")