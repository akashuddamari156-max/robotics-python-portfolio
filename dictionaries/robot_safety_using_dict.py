battery = int(input("Enter battery %: "))
obstacle = int(input("Enter obstacle yes==1 or no==0 "))

robot = {"Battery":(battery),"Obstacle":(obstacle)}
print(robot)

if robot["obstacle"] == 1:
    print("STOP 🚫")
elif robot["battery"] < 20:
    print("GO CHARGE 🔋")
else:
    print("MOVE ✅")

'''for key, value in robot.items():
    if obstacle == 1:
        print("Stop")
    elif battery < 20 :
        print("Go charge")
    else:
        print("Move")'''