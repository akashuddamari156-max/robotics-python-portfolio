n = int(input("enter how many readings: "))
total = 0
for i in range(n):
    readings = float(input(f"enter readings{i+1} :"))
    total += readings
    readings -= 1
    
avg = total / n
print("sum of readings is: ",avg)
