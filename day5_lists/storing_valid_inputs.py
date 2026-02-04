n = int(input("Enter number of integers: "))
a = []
total = 0 
count = 0

for i in range(n):
    readings = float(input(f"Enter readings{i+1}: "))
    
    if readings > 0:
        a.append(readings)

        total += readings
        readings -= 1
        count += 1
        
        
avg = total/count


print(f"the list is: {a}")
print("Average is: ",avg)
