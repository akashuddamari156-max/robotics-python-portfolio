battery = int(input("Enter bateery% : "))
robot = {"battery":(battery)}
print(f"battery is {robot}")

robot["battery"] = robot["battery"] - 10

print("updated battery is: ",robot["battery"])