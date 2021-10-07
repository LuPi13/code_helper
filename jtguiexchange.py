from tkinter import *


def output():
    won = float(inputwon.get())
    if country.get() == 1:
        ratio = 1189.7
        unit = "달러"
    elif country.get() == 2:
        ratio = 184.34
        unit = "위안"
    elif country.get() == 3:
        ratio = 1067.38
        unit = "엔"
    elif country.get() == 4:
        ratio = 1615.67
        unit = "파운드"
    elif country.get() == 5:
        ratio = 16.43
        unit = "루블"
    exchange = won / ratio
    label4.configure(text="%.2f"%(float(exchange))+unit)

ratio = 1
unit = ""
won = 0
exchange = 0

window = Tk()
window.title("박준태_환율 계산기")

label1 = Label(window, text="환전하려는 국가를 선택하세요.", background="#FF8888", width=40)
label1.pack()

country = IntVar()
rb1 = Radiobutton(window, text="미국", variable=country, value=1, command=output)
rb1.pack(anchor=CENTER)
rb2 = Radiobutton(window, text="중국", variable=country, value=2, command=output)
rb2.pack(anchor=CENTER)
rb3 = Radiobutton(window, text="일본", variable=country, value=3, command=output)
rb3.pack(anchor=CENTER)
rb4 = Radiobutton(window, text="영국", variable=country, value=4, command=output)
rb4.pack(anchor=CENTER)
rb5 = Radiobutton(window, text="러시아", variable=country, value=5, command=output)
rb5.pack(anchor=CENTER)

label2 = Label(window, text="금액(원)을 입력하세요.", background="#FF8888")
label2.pack(anchor=CENTER)

inputwon = Entry(window)
inputwon.insert(0, 0)
inputwon.pack(anchor=CENTER)

label3 = Label(window, text="< 환전 결과 >", background="#FF8888")
label3.pack(anchor=CENTER)

label4 = Label(window, text="", background="#FF88FF")
label4.pack(anchor=CENTER)


window.mainloop()
