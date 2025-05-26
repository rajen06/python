import tkinter
import random
import string
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password = ""
    for _ in range(12):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    password_entry.insert(0, password)  
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return
    else:
        try:   
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, tkinter.END)
            # email_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)   

    
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries

website_entry = tkinter.Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = tkinter.Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2 )
email_entry.insert(0, "test@test.com")

password_entry = tkinter.Entry(width=22)
password_entry.grid(column=1, row=3)

# Buttons

generate_password_button = tkinter.Button(text="Generate Password", width=11, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=34, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

search_button = tkinter.Button(text="Search", width=11, command=find_password)
search_button.grid(column=2, row=1)




window.mainloop()