num = 0

naenwa = int(input("숫자 내놔 : "))
for i in range(1,naenwa+2):
    for k in range(i,naenwa+1):
        print(" ",end="")
    for j in range(1,i):
        if (num == 10):
            num = 0
        print(num,end="")
        num += 1
    print()
