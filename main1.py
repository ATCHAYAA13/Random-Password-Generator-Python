from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import tkinter as tk
import random
import string
import pyperclip

# Set the appearance mode to "dark"
customtkinter.set_appearance_mode("dark")

# Set a specific color theme (e.g., "dark-blue")
customtkinter.set_default_color_theme("dark-blue")

# Create the main window using customtkinter.CTk
root = customtkinter.CTk()
root.title("Password Generator")
root.iconbitmap(r"D:\ATCHAYAA THINGAL\Projects\Oasis Infotech\Random Password Generator\Icon.ico")
root.geometry("500x650")

# Load the image
pwd_image = ImageTk.PhotoImage(Image.open("Random Password Generator\Password generator.jpg"))
pwd1 = Label(root, image=pwd_image, bd=0)
pwd1.pack(pady=20)

#h = customtkinter.CTkEntry(master = app, placeholder_text="Height in cm",width=200,height=30,border_width=1,corner_radius=20)
#h.pack(pady=10)
# Label
complexity_label = customtkinter.CTkLabel(root, text="Password Complexity:",width=200,height=30,corner_radius=20)
complexity_label.pack(pady=10)

# Option menu for complexity
complexity_var = customtkinter.StringVar(value="Weak")  # set initial value

def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

combobox = customtkinter.CTkOptionMenu(master=root,
                                       values=["Weak", "Medium","Strong"],
                                       command=optionmenu_callback,
                                       variable=complexity_var)
combobox.pack(padx=20, pady=10)



def generate_password():
    complexity = complexity_var.get()
    
    if complexity == "Weak":
        length = 8
        use_upper = False
        use_lower = True
        use_digits = True
        use_special = False
    elif complexity == "Medium":
        length = 12
        use_upper = True
        use_lower = True
        use_digits = True
        use_special = False
    elif complexity == "Strong":
        length = 16
        use_upper = True
        use_lower = True
        use_digits = True
        use_special = True
    else:
        result_label.configure(text="Select a complexity level.")
        return

    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    #result_label.configure(text=f"Generated Password: {password}")

# Button to generate password

generate_button = customtkinter.CTkButton(master=root, text="Generate Password",width=190,height=40,fg_color="#8e4585",hover_color="#5b7b7a",compound="top",command=generate_password)
generate_button.pack(pady=10)

# Display the generated password
#password_entry = Entry(root)
#password_entry.pack()
password_entry = customtkinter.CTkEntry(root, width=200, height=30, corner_radius=20)
password_entry.pack(pady=10)

def copy_password():
    password = password_entry.get()
    pyperclip.copy(password)
    copy_button.configure(text="Password Copied!")
    root.after(2000, lambda: copy_button.configure(text="Copy to Clipboard"))

# Button to copy the password
copy_button = customtkinter.CTkButton(master=root, text="Copy to Clipboard",width=190,height=40,fg_color="#8e4585",hover_color="#5b7b7a", command=copy_password)
copy_button.pack(pady=10)

# Display the result message

result_label = customtkinter.CTkLabel(root, text="",width=200,height=30,corner_radius=20)
result_label.pack(pady=10)

# Run the GUI
root.mainloop()
