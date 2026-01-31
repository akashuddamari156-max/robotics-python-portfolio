obstacle = int(input("is obstacle detected? 1 or 0: "))
distance = float(input("Enter distance in meteres:"))#distance to obstacle in meters

if obstacle == 1 and distance < 0.5 :
    print("Stop")
elif obstacle == 1 and distance >= 0.5 :
    print("Slow down")
else:
    print("Move")