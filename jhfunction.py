def sum(a, b, c):
    return(a+b+c)

def ave(a,b,c):
    return(round(sum(a,b,c)/3,3))

def grade(a,b,c):
    if ave(a,b,c)>=90:
        return("A")
    elif ave(a,b,c) >= 80:
        return("B")
    elif ave(a,b,c) >= 70:
        return("C")
    elif ave(a,b,c) >= 60:
        return("D")
    else:
        return("E")

kor=int(input("국어 : "))
eng=int(input("영어 : "))
mat=int(input("수학 : "))
print("총점 :", sum(kor,eng,mat), "평균 :", ave(kor,eng,mat), "학점 :", grade(kor,eng,mat))
