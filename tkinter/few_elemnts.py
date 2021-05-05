import tkinter
from tkinter import *
window = tkinter.Tk()
window.title('My first GUI program')
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I'M A LABEL", font=("Arial", 24, "bold"))
my_label.pack()
# my_label.pack(side="left")

my_label['text'] = "New Text"
my_label.config(text="New Text")

# Button
def button_clicked():
    print("i got clicked")
    new_text = input.get()
    #my_label.config(text="Button got clicked")
    my_label.config(text=new_text)

button = Button(text= "click me", command = button_clicked)
button.pack()


# Entry

input = Entry(width=10)
input.pack()
print(input.get())

# import turtle
# tim = turtle.Turtle()
# tim.write("some text")


window.mainloop()
