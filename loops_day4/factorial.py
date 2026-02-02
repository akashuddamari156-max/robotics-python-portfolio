n = int(input("enter n (number of integers): "))
total = 1

while n > 0 :
    total *= n
    n -= 1 

print(f"n factorial is : {total}")