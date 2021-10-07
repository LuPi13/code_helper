from tkinter import *


def add():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 + num2
    entry3.delete(0, END)
    entry3.insert(0, "%s"%(result))

def subtract():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 - num2
    entry3.delete(0, END)
    entry3.insert(0, "%s" % (result))

def multiply():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 * num2
    entry3.delete(0, END)
    entry3.insert(0, "%s" % (result))

def division():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 / num2
    entry3.delete(0, END)
    entry3.insert(0, "%s" % (result))


window = Tk()
window.title("박준태_사칙연산 계산기")

label1 = Label(window, text="숫자1 입력", width=20)
label1.grid(row=0, column=0, columnspan=2, sticky=W+E)

entry1 = Entry(window, width=20)
entry1.grid(row=0, column=2, columnspan=2, sticky=W+E)

label2 = Label(window, text="숫자2 입력", width=20)
label2.grid(row=1, column=0, columnspan=2, sticky=W+E)

entry2 = Entry(window, width=20)
entry2.grid(row=1, column=2, columnspan=2, sticky=W+E)

btn1 = Button(window, text="+", command=add, width=10)
btn1.grid(row=2, column=0, sticky=W+E)

btn2 = Button(window, text="-", command=subtract, width=10)
btn2.grid(row=2, column=1, sticky=W+E)

btn3 = Button(window, text="*", command=multiply, width=10)
btn3.grid(row=2, column=2, sticky=W+E)

btn4 = Button(window, text="/", command=division, width=10)
btn4.grid(row=2, column=3, sticky=W+E)

entry3 = Entry(window, width=40)
entry3.grid(row=3, column=0, columnspan=4, sticky=W+E)

window.mainloop()
