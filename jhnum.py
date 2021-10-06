sum = 0 #자릿수 합 저장할 곳
num = int(input("임의의 정수 입력 : ")) #숫자 받기
first = num #초기에 쓴 값을 복사(num이란 변수는 변화시킬거라서 보존이 안됨)

if num < 0: #num이 음수라면, -1을 곱해서 양수로 바꿈
    num = num * (-1)

numstr = str(num)   #양수로 바뀐 num을 문자열형태로 저장(길이 판별용)

while num>=10:  #num이 10이상일때
    sum = sum + (num % 10)  # sum 에다가 num을 10으로 나눈 나머지(=num의 1의자리 수)를 더함
    num = num // 10 #num을 10으로 나눈 몫으로 저장

if num < 10:    #num이 10 미만일때
    sum = sum + num #sum 에다가 num을 더함
print("{0} {1}자리 정수" .format(first, len(numstr)))   #({n}, .format 표기법 모르면 너가 아는대로 하십쇼) len(numstr)는 numstr의 문자열길이
print("각 자리의 총합 :", sum)  #이렇게
