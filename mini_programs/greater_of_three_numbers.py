x, y, z = map(float , input("Enter three numbers seprated by space: ").split())

value = x

for i in x,y,z :
    if i > value:
        value = i

print("The largest value is: ",value)