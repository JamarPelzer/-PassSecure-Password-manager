# Import necessary modules from tkinter and random
from tkinter import *
from tkinter import Entry
from tkinter import messagebox
from random import choice, shuffle


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']  # List of letters
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  # List of numbers

    # Generate password components
    password_letters = [choice(letters) for _ in range(15)]
    password_numbers = [choice(numbers) for _ in range(5)]

    # Combine password components
    password_list = password_letters + password_numbers

    shuffle(password_list)  # Shuffle the combined list

    password = "".join(password_list)  # Convert list to a string
    formatted_password = '-'.join(
        password[i:i + 5] for i in range(0, len(password), 5))  # Insert "-" every 5 characters
    password_entry.delete(0, END)  # Clear any previous content
    password_entry.insert(0, formatted_password)  # Insert the generated password into the entry


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0:
        messagebox.showinfo(title="Empty Field", message="Please make sure you fill in 'Website'")
    elif len(password) == 0:
        messagebox.showinfo(title="Empty Field", message="Please make sure you fill in 'Password'")
    else:
        # Ask user for confirmation before saving
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email:{email},"
                                                              f"\n Password:{password} \n is it ok to save?")
        if is_ok:
            # Open and write the details to a file
            with open("code.text", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)  # Clear website entry
                password_entry.delete(0, END)  # Clear password entry


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pass Secure")
window.config(padx=70, pady=70)

# Logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo_2.png")
canvas.create_image(145, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=38)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "@email.com")
password_entry: Entry = Entry(width=21, )
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, columnspan=2)
add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
