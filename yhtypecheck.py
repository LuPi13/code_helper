try:
    hours = float(input("Enter Hours : "))
    rate = float(input("Enter Rate : "))
    pay = hours * rate  #계산식 다른거면 너가 바꾸십쇼
    print("Pay : {0}" .format(pay))
except: #try 속 내용물을 처리하다가 오류가 나면 무시하고 이쪽으로 넘어온다. 제시된 문제점은 float형에 문자를 집어넣은 것
    print("Error, please enter numeric input")