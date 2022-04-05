def collatz(num):
    count = 0  # 반복횟수
    progress = [num]  # 과정 저장할 리스트
    while True:  #무한 반복
        if (count >= 100):  # 100번 이상 했으면
            print("(-1)")
            break


        elif (progress[-1] == 1):  # 과정 리스트의 마지막 숫자가 1 이라면
            print("(" + str(count) + ")", end="")

            # 쭉 출력(마지막은 화살표 X)
            for i in range(0, len(progress)):
                if (i != (len(progress)-1)):
                    print(str(progress[i]) + "->", end="")
                else:
                    print(progress[i])
            break


        elif ((progress[-1] % 2) == 0):  # 짝수라면
            count += 1
            progress.append(int(progress[-1] / 2))

        elif ((progress[-1] % 2) != 0):  # 홀수라면
            count += 1
            progress.append((progress[-1] * 3) + 1)


#collatz(171)