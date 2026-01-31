battery = int(input("Enter Bateery %: "))
obstacle = input("Obstacle detetced? 1 or 0 ")
command = input ("Forward or Stop ")

if battery < 15 :
    print("go Charge")
elif obstacle == 1 and command == "forward" :
    print("Stop")
else:
    print("Command executed")