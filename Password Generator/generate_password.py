import random
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import font

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_clicked():
    password_length = int(length_entry.get())
    if password_length < 4:
        messagebox.showerror("Error", "Password length must be at least 4 characters.")
        return
    
    password = generate_password(password_length)
    password_label.config(text="Generated Password: " + password)

def reset_button_clicked():
    length_entry.delete(0, tk.END)
    password_label.config(text="Generated Password: ")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create a custom font
custom_font = font.Font(family="Helvetica", size=18, weight="bold")

# Create heading label
heading_label = tk.Label(root, text="Password Generator", font=custom_font)
heading_label.pack()

# Create widgets
username_label = tk.Label(root, text="Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_button_clicked)
generate_button.pack()

accept_button = tk.Button(root, text="Accept", command=reset_button_clicked)
accept_button.pack()

reset_button = tk.Button(root, text="Reset", command=reset_button_clicked)
reset_button.pack()

password_label = tk.Label(root, text="Generated Password: ")
password_label.pack()

# Start the GUI event loop
root.mainloop()
