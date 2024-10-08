# 1

for i in range(7):
    for j in range(5):
        if j == (3 - i) or j == 3 or i == 6:
            print("+", end = "")
        else:
            print(" ", end = "")
    print()