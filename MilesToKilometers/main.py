from tkinter import *

def calculate():
    miles = int(miles_input.get())
    miles *= 1.6
    converted_miles_label.config(text=f"{miles}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)
window.minsize(width=200, height=100)

#Label
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

converted_miles_label = Label(text="0", justify="center")
converted_miles_label.config(padx=30)
converted_miles_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

miles_input_label = Label(text="Miles")
miles_input_label.grid(column=2, row=0)

#Button
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

#input
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)



window.mainloop()