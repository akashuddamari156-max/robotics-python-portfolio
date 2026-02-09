x = input("Enter Command forward/stop/left/right ").lower()

if x == "forward":
    print("Robot is moving Forward")
elif x == "stop":
    print("Robot Stopped")
elif x == "left":
    print("Robot is turning left")
elif x == "right":
    print("robot is turning right")
else:
    print("invalid command")