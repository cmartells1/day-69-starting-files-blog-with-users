# import tkinter
from tkinter import *


def button_clicked():
    # my_label["text"] = "Button got clicked."
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#label

my_label = Label(text="I am a label", font=("Arial", 24,"bold"))
#label won't show up unless you use the pack to pack it on to the screen
my_label.config(text="New Text")
my_label.grid(column=0, row=0)


#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)


new_button = Button(text="New Button")
new_button.grid(column=2, row=0)
#Entry

input = Entry(width=10)
input.grid(column=3, row=2)











window.mainloop()
