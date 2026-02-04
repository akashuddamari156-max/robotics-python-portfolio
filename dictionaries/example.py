robot = {
    "name": "TurtleBot4",
    "battery": 90,
    "speed": 0.4,
    "obstacle": False
}

print(robot)
robot["speed"] = robot["speed"] + 0.1
print("Updated speed:", robot["speed"])
robot["mode"] = "AUTO"
print(robot)

robot1 = {"name":"AkashBot","Battery":100,"speed":0.5}
print(robot1["Battery"])
robot1["mode"]="auto"
robot1["Battery"]=robot1["Battery"]-15
print(robot1)
for key, value in robot.items():
    print(key, "=", value)  