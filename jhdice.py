import random

count=[0,0,0,0,0,0]

for i in range(1,1000):
    x=random.randint(1,6)
    if x==1:
        count[0]+=1
    elif x==2:
        count[1]+=1
    elif x==3:
        count[2]+=1
    elif x==4:
        count[3]+=1
    elif x==5:
        count[4]+=1
    elif x==6:
        count[5]+=1

for i in range(0,6):
    print("주사위가", i+1, "인 경우는", count[i], "번")
