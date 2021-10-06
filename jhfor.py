num=int(input("1~9? : "))

i=1
while i<=num:
    j=1
    while j<=i:
        print(j,end="")
        j+=1

    for k in range(0,num-i):
        print("*",end="")
    print()
    i+=1