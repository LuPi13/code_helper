mylist=[]

while True:
    mysublist=[]
    mysublist = list(map(int,input('>>').split()))
    if mysublist[0] ==-1:
        break
    else:
        mylist.append(mysublist)

print(mylist)

for sublist in mylist:
    for value in sublist:
        if value%2 == 1:
            for i in range(0, value):
                print(" ■ ",end="")
            value = 3

        elif value%2 == 0:
            for i in range(0, value):
                print(" □ ",end="")
            value = 2
