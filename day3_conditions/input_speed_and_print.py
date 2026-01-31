speed = int(input("Enter speed in m/sec: "))
if speed > 30 :
    print("Robot is moving fast")
elif 30 >= speed >= 10 :
    print("Robot speed is normal")
else:
    print("Robot is slow")