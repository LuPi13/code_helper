namelist = input("이름 입력 : ").split(" ")  # 이름받고 띄어쓰기로 쪼개고 리스트로 저장
scorelist = input("점수 입력 : ").split(" ")  # 점수받고 ~~

# 점수 받은거 문자열 형태이므로 정수형으로 모두 형변환
for i in range(0, len(scorelist)):
    scorelist[i] = int(scorelist[i])


if (len(namelist) == len(scorelist)):  # 두 리스트 길이가 같을때
    # 내림차순 정렬 알고리즘
    for j in range(1, len(namelist)):  # (원소개수-1)번 반복
        for k in range(0, len(namelist)-1):
            if (scorelist[k] < scorelist[k+1]):  # k번째 보다 k+1번째가 더 크면
                scorelist[k], scorelist[k+1] = scorelist[k+1], scorelist[k]  # 둘이 위치 변경
                namelist[k], namelist[k+1] = namelist[k+1], namelist[k]  # 이름리스트도 둘이 위치 변경

    # abc 저장할 곳
    alist = []
    blist = []
    clist = []
    # 모든 원소에 대해
    for l in range(0, len(namelist)):
        if (l+1 <= (len(namelist) * 0.3)):  # 성적 등수가 전체 개수의 0.3 이하라면
            alist.append(namelist[l])
        elif (l+1 <= (len(namelist) * 0.6)):  # 성적 등수가 전체 개수의 0.6 이하라면
            blist.append(namelist[l])
        else:  # 그 외
            clist.append(namelist[l])

    print("A학점 :", alist)
    print("B학점 :", blist)
    print("C학점 :", clist)


else: # 두 리스트 길이가 다를 때
    print("두 리스트의 원소 개수 다름")
