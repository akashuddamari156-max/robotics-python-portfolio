for i in range(10):
    obstacle = int(input("is obstacle detected? (0 or 1)"))
    if obstacle == 1:
        print("Obstacle found stop scanning")
        break
    else:
        print("clear")