from tkinter import *

def calculate():
    print("clicked button to calculate")
    new_text = entry1.get()
    entry_label.config(text=str(int(new_text)*1.609))


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)


is_label = Label(text="is equal to")
is_label.grid(column=0, row=1)
#my_label.config(text="new text")
#my_label.config(padx=50, pady=70)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)


entry1 = Entry(width=13)
entry1.insert(END, string="0")
entry1.grid(column=1, row=0)

entry_label = Label(text="0")
entry_label.grid(column=1, row=1)
entry_label.config(padx=10,pady=10)

window.mainloop()
