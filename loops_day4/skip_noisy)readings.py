n = int(input("Enter number of readings: "))
total = 0
count = 0
for i in range(n):
    readings = float(input(f"Enter raeding{i+1}: "))
    if readings < 0:
        continue
    total += readings
    count += 1

if count == 0 :
    print("no valid readings entered")
else:
    avg = total/count
    print(f"Average of readings is: {avg}")