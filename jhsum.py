sum = 0
while True:
    x = int(input("정수를 입력하시오(종료:0) : "))
    sum = sum + x

    if x == 0:
        break

print("합은", sum, "입니다.")
