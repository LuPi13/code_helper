mainlist = []
dist = 0
while True:
    inputlist = input(">>")

    inputlist = inputlist.split()
    mainlist.append(inputlist)

    if mainlist[-1] == ['-1']:
        mainlist.remove(mainlist[-1])
        break



for i in mainlist:
    for j in i:
        j = int(j)
        if ((dist % 2) == 0):
            for k in range(0, j):
                print("□", end="")
            dist += 1

        elif ((dist % 2) == 1):
            for k in range(0, j):
                print("■", end="")
            dist += 1
    print("")
