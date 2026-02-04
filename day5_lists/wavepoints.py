n = int(input("Enter number of pairs: "))
wavepoints = []
for i in range(n):
    x=int(input(f"enter x{i+1}: "))
    y=int(input(f"enter y{i+1}: "))
    pair = (x,y)
    wavepoints .append(pair)
    
print(f"Wavepoints is: {wavepoints}")

