#입력
a = float(input("출석 : "))
b = float(input("퀴즈 : "))
c = float(input("과제 : "))
d = float(input("발표 : "))
e = float(input("기말 : "))

#처리
f = (a * 0.1) + (b * 0.15) + (c * 0.35) + (d * 0.2) + (e * 0.2)

#출력
print("점수 : %.2f" %(f))
