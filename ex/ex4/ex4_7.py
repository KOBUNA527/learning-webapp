for i in range(4):
    for j in range(4):
        if j < 3 - i:
            print(" ", end="")
        else:
            print(i+1, end="")
    print()

for i in range(4):
    for j in range(4):
        if j < i:
            print(" ", end="")
        else:
            print(i+1, end="")
    print()
