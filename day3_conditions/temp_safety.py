temp = int(input("Enter motor temperature: "))
if temp > 80 :
    print("Emergency Stop")
elif 80 >= temp >= 60 :
    print("Warning")
else:
    print("Safe")