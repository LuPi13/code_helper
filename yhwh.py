width = 17
height = 12.0 # 소수점 찍는 순간부터 얘는 실수형(float)으로 인식함

print(width//2) # // 는 나눈 몫 출력, 몫의 개념이 있다는건 당연히 결괏값은 정수형(int)
print(width/2.0) # 17/2=8.5, 결괏값은 실수형(float)
print(height/3) # 실수형(float)과 정수형(int) 관의 연산이 있으면 결괏값은 무조건 실수형(float)
print(1+2*5) # 정수(int) 끼리만 연산하고, 결괏값이 정수라면 결괏값도 정수형(int)

print(type(width//2))
print(type(width/2.0))
print(type(height/3))
print(type(1+2*5))
# type(내용물) 로 이것의 타입(자료형)을 알 수 있음
