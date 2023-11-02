from tkinter import *
from tkinter import ttk
import webbrowser

app = Tk()
app.title("web browser")
app.geometry("550x450")


entery=Entry(app, width=50)
entery.place(x=120,y=175)

label=Label(text="search",font="23")
label.place(x=65,y=175)


label2=Label(text="web browser",font="arial 50 bold")
label2.place(x=60,y=2)


def search_web():
    webbrowser.open_new(entery.get())






button=Button(text="search",command=search_web,width=7,font="1.5")
button.place(x=230,y=200)

app.mainloop()