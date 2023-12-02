import tkinter as tk
import random
import string
from tkinter import messagebox

def generate_password():
    password_length = int(length_entry.get())
    complexity = ""
    if uppercase_var.get():
        complexity += string.ascii_uppercase
    if lowercase_var.get():
        complexity += string.ascii_lowercase
    if digits_var.get():
        complexity += string.digits
    if special_chars_var.get():
        complexity += string.punctuation
    
    password = ''.join(random.choice(complexity) for _ in range(password_length))
    password_display.config(state=tk.NORMAL)
    password_display.delete(1.0, tk.END)
    password_display.insert(tk.END, password)
    password_display.config(state=tk.DISABLED)

def show_about():
    messagebox.showinfo("About", "Password Generator App\nCreated with Tkinter\nVersion 1.0")

root = tk.Tk()
root.title("Password Generator")

# Define window size
window_width = 400
window_height = 350

# Calculate position for the window to appear in the center
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)

# Set window size and position
root.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

# Title bar
title_frame = tk.Frame(root, bg="#4CAF50", padx=10, pady=5)
title_frame.pack(side=tk.TOP, fill=tk.X)

title_label = tk.Label(title_frame, text="Python Password Generator", font=("Arial", 14), bg="#4CAF50", fg="white")
title_label.pack(side=tk.LEFT)

about_button = tk.Button(title_frame, text="About", command=show_about)
about_button.pack(side=tk.RIGHT)

# Length selection
length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

# Character complexity options
uppercase_var = tk.IntVar()
uppercase_check = tk.Checkbutton(root, text="Uppercase", variable=uppercase_var)
uppercase_check.pack()

lowercase_var = tk.IntVar()
lowercase_check = tk.Checkbutton(root, text="Lowercase", variable=lowercase_var)
lowercase_check.pack()

digits_var = tk.IntVar()
digits_check = tk.Checkbutton(root, text="Digits", variable=digits_var)
digits_check.pack()

special_chars_var = tk.IntVar()
special_chars_check = tk.Checkbutton(root, text="Special Characters", variable=special_chars_var)
special_chars_check.pack()

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)  # Adding padding for spacing

# Display generated password
password_display = tk.Text(root, height=5, width=30)
password_display.config(state=tk.DISABLED)
password_display.pack()

# Interface label at bottom right
interface_label = tk.Label(root, text="codestak.io", fg="gray")
interface_label.pack(side=tk.RIGHT, anchor=tk.SE)

root.mainloop()
