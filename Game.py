import random
from tkinter import *


k = 0


def control1():
    global k
    k = 1
    label3.config(text="Камень")
    game()


def control2():
    global k
    k = 2
    label3.config(text="Ножницы")
    game()


def control3():
    global k
    k = 3
    label3.config(text="Бумага")
    game()


def game():
    r = random.randint(1,3)
    if(r == 1):
        label4.config(text="Камень")
    elif(r == 2):
        label4.config(text="Ножницы")
    elif(r == 3):
        label4.config(text="Бумага")

    result = k - r

    if(result == 0):
        label6.config(text="Ничья")
    elif(result == -1 or result == 2):
        label6.config(text="Игрок")
    elif(result == 1 or result == -2):
        label6.config(text="Компьютер")


root = Tk()
root.title("Игра Камень, Ножницы, Бумага")
root.geometry("400x200")
root.resizable(width=False, height=False)
canvas = Canvas(bg="white", width=400, height=200)
canvas.pack(anchor=CENTER, expand=1)
label1 = Label(root, text="Игрок:", background="white")
label1.place(x=50, y=20)
label2 = Label(root, text="Компьютер:", background="white")
label2.place(x=50, y=50)
label3 = Label(root, text="0", background="white")
label3.place(x=150, y=20)
label4 = Label(root, text="0", background="white")
label4.place(x=150, y=50)
label5 = Label(root, text="Победитель:", background="white")
label5.place(x=250, y=20)
label6 = Label(root, text="0", background="white")
label6.place(x=250, y=50)
button1 = Button(root, text="Камень", width=8, command=control1)
button1.place(x=50, y=120)
button2 = Button(root, text="Ножницы", width=8, command=control2)
button2.place(x=170, y=120)
button3 = Button(root, text="Бумага", width=8, command=control3)
button3.place(x=290, y=120)
button4 = Button(root, text="Выход", width=8, command=root.destroy)
button4.place(x=290, y=160)
canvas.create_rectangle(40, 10, 220, 45)
canvas.create_rectangle(40, 45, 220, 75)
canvas.create_rectangle(240, 10, 350, 75)
root.mainloop()