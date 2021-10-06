import turtle   #터틀그래픽 임포트
t=turtle.Turtle()
t.shape("turtle")


color_list=[]   #빈 리스트 생성
color_list.append(str(input("색상 #1을 입력하십시오 : ")))  #리스트이름.append(내용물) 하면 리스트 맨끝에 내용물을 추가
color_list.append(str(input("색상 #2를 입력하십시오 : ")))  #str(내용물) 은 변수를 문자 형태로 저장함
color_list.append(str(input("색상 #3을 입력하십시오 : ")))  #이렇게 색깔 3개를 저장

t.fillcolor(color_list[0])
t.begin_fill()
t.circle(100)
t.end_fill()

t.forward(200)
t.fillcolor(color_list[1])
t.begin_fill()
t.circle(100)
t.end_fill()

t.forward(200)
t.fillcolor(color_list[2])
t.begin_fill()
t.circle(100)
t.end_fill()