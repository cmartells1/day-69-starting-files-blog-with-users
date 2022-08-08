# import tkinter
from tkinter import *


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#label

my_label = Label(text="I am a label", font=("Arial", 24,"bold"))
#label won't show up unless you use the pack to pack it on to the screen
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

#Button

def button_clicked():
    # my_label["text"] = "Button got clicked."
    new_text = input.get()
    my_label.config(text=new_text)
button = Button(text="Click Me", command=button_clicked)
button.pack()

#Entry

input = Entry(width=10)
input.pack()











window.mainloop()
