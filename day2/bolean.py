user = int(input("Obstacle detcted? Yes==1 or No==0"))
obstacle_detected = bool(user)

print("Obstacke detected :",obstacle_detected)

if obstacle_detected:
    print("Stop robot")
else:
    print("no obstacles")