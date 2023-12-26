from tkinter import *

a = 0
b = 1

win = Tk()
win.title("Clicker")
win.geometry("500x500")

def clicked():
    global a
    global b
    a += b
    button1["text"] = a, "$"


common_img = PhotoImage(width=1, height=1)

button1 = Button(win, text="0 $",
                fg="white", bg="lightblue", image=common_img, width=1520, height=1080,
                compound = "c", activebackground="lightblue", activeforeground="white",
                font=("Impact", 200), command=clicked)
button1.place(x=0, y=1)

button2 = Button(win, text="ITEM SHOP:",
                fg="white", bg="black", image=common_img, width=384, height=100,
                compound = "c", activebackground="black", activeforeground="white",
                font=("Impact", 60))
button2.place(x=1528, y=1)

button3 = Button(win, text="ITEM 1",
                fg="white", bg="orange", image=common_img, width=384, height=120,
                compound = "c", activebackground="darkorange", activeforeground="white",
                font=("Impact", 75))
button3.place(x=1528, y=108)

button4 = Button(win, text="ITEM 2",
                fg="white", bg="orange", image=common_img, width=384, height=120,
                compound = "c", activebackground="darkorange", activeforeground="white",
                font=("Impact", 75))
button4.place(x=1528, y=228)

button5 = Button(win, text="ITEM 3",
                fg="white", bg="orange", image=common_img, width=384, height=120,
                compound = "c", activebackground="darkorange", activeforeground="white",
                font=("Impact", 75))
button5.place(x=1528, y=348)

button6 = Button(win, text="ITEM 4",
                fg="white", bg="orange", image=common_img, width=384, height=120,
                compound = "c", activebackground="darkorange", activeforeground="white",
                font=("Impact", 75))
button6.place(x=1528, y=468)

button7 = Button(win, text="ITEM 5",
                fg="white", bg="orange", image=common_img, width=384, height=120,
                compound = "c", activebackground="darkorange", activeforeground="white",
                font=("Impact", 75))
button7.place(x=1528, y=588)

button8 = Button(win, text="ITEM 6",
                fg="white", bg="orange", image=common_img, width=384, height=120,
                compound = "c", activebackground="darkorange", activeforeground="white",
                font=("Impact", 75))
button8.place(x=1528, y=708)

button9 = Button(win, text="ITEM 7",
                fg="white", bg="orange", image=common_img, width=384, height=120,
                compound = "c", activebackground="darkorange", activeforeground="white",
                font=("Impact", 75))
button9.place(x=1528, y=828)

button10 = Button(win, text="",
                bg="black", image=common_img, width=390, height=75,
                compound = "c", activebackground="black")
button10.place(x=1528, y=952)

win.mainloop()