mylist=[]

while True:
    mysublist=[]
    mysublist = list(map(int,input('>>').split()))
    if mysublist[0] ==-1:
        break
    else:
        mylist.append(mysublist)

print(mylist)

for sublist in list:
    for value in sublist:
        for i in value:
            for i in range(0, value):
                if value%2 == 1:
                    print(" ■ ", end="1")

for sublist in list:
    for value in sublist:
        for i in value:
            for i in range(0, value):
                if value%2==0:
                    print(" □ ", end="0")
