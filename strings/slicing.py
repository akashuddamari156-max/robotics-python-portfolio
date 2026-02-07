x = input("Enter x: ")

if len(x) >= 3:
    print("First three charcters are: ",x[ : 3])
    print("Last three charcters are: ",x[-3 :])

else:
    print("string is less than three")
