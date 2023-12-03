import tkinter as tk
import random
import string
from tkinter import messagebox
from tkinter import filedialog
from fpdf import FPDF  # Required for PDF export

password_generated = False

def generate_password():
    global password_generated
    password_length = length_entry.get()
    if not password_length:
        messagebox.showwarning("Warning", "Please input Password Length")
        return
    
    password_length = int(password_length)
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
    password_generated = True

def save_to_file():
    global password_generated
    if not password_generated:
        messagebox.showerror("Error", "No password generated yet!")
        return
    
    password = password_display.get(1.0, tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("PDF Files", "*.pdf")])
    
    if file_path:
        if file_path.endswith(".pdf"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="Generated Password", ln=True)
            pdf.cell(200, 10, txt=password, ln=True)
            pdf.output(file_path)
        else:
            with open(file_path, "w") as file:
                file.write(password)

def copy_to_clipboard():
    global password_generated
    if not password_generated:
        messagebox.showerror("Error", "No password generated yet!")
        return
    
    password = password_display.get(1.0, tk.END)
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copy to Clipboard", "Password copied to clipboard!")

def clear_password():
    global password_generated
    if not password_generated:
        messagebox.showerror("Error", "No password generated yet!")
        return
    
    password_display.config(state=tk.NORMAL)
    password_display.delete(1.0, tk.END)
    password_display.config(state=tk.DISABLED)
    password_generated = False

def show_about():
    messagebox.showinfo("About", "Password Generator App\nAuthor: Raymond C. Turner.\nApp Version 1.1.0")

root = tk.Tk()
root.title("Password Generator")

# Define window size
window_width = 400
window_height = 500

# Calculate position for the window to appear in the center
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)

# Set window size and position
root.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

# Title bar
title_frame = tk.Frame(root, bg="#1B81A8", padx=10, pady=5)
title_frame.pack(side=tk.TOP, fill=tk.X)

title_label = tk.Label(title_frame, text="Password Generator", font=("Arial", 12), bg="#1B81A8", fg="white")
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

# UI Buttons for Save to File, Copy to Clipboard, Clear Password
save_button = tk.Button(root, text="Save to File", command=save_to_file)
save_button.pack(pady=5)

copy_clipboard_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_clipboard_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear Password", command=clear_password)
clear_button.pack(pady=5)

# Interface label at bottom right
interface_label = tk.Label(root, text="codestak.io", fg="gray")
interface_label.pack(side=tk.RIGHT, anchor=tk.SE)

root.mainloop()
