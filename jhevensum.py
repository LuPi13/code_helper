i=1
sum=0
a=[]

while True:
    if i<=100:
        if i%2==0:
            a.append(i)
            sum = sum + i
        i+=1
    else:
        break

for j in range(0,50):
    print(a[j],end=" ")
print("\n1~100 짝수 합 :", sum)