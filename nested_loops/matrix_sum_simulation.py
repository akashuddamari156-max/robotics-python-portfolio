total = 0

for i in range(3):
    for j in range(3):
        value = float(input(f"Enter value for ({i},{j}): "))
        total += value

print("Matrix sum:", total)
