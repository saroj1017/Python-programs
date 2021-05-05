from tkinter import *
from tkinter import messagebox
import pyperclip
from random import randint, choice, shuffle
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list1 = [choice(letters) for _ in range(randint(8, 10))]
    password_list2 = [choice(symbols) for _ in range(randint(2, 4))]
    password_list3 = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_list1 + password_list2 + password_list3

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

    print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def find_password():
    search_input = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            content = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="please insert data before searching")
    else:
        #for key,value in content.items():
        if search_input in content:
            email = content[search_input]["email"]
            password = content[search_input]["password"]
            messagebox.showinfo(title=search_input, message=f"Email:{email}\nPassword: {password}")
            print(email)
            print(password)
        else:
            messagebox.showinfo(title=search_input, message="no match found")



def save():
    global website_name
    website_name = website_entry.get()
    email_name = email_entry.get()
    password_name = password_entry.get()
    # prompt = messagebox.showinfo(title="Title", message="message")

    new_data = {
        website_name:
            {
                "email": email_name,
                "password": password_name
            }
    }

    if len(website_name and password_name) == 0:
        messagebox.showinfo(title="Oops", message="please don't leave any fields empty")
    else:

        # prompt = messagebox.askokcancel(title="confirmation", message=f"These are the details entered:\nEmail:"
        #                                                               f" {email_name}\nPassword: {password_name}"
        #                                                               f" \nIs it ok to save it?")
        # if prompt:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
        # data_file.write(f"{website_name}  | {email_name} | {password_name} \n")
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            # print(data)
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("password manager")
window.config(padx=55, pady=40)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

website_entry = Entry(width=31)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=3)
email_entry.insert(0, string="saroj.pradhan1017@gmail.com")

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1, columnspan=1)

generate_button = Button(text="Generate Password", width=14, command=password_generator)
generate_button.grid(row=3, column=2)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
