import tkinter as tk
from tkinter import filedialog, Text

# Function to create a new file
def new_file():
    text_area.delete(1.0, tk.END)

# Function to open an existing file
def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

# Function to save the file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))

# Create the main window
root = tk.Tk()
root.title("Simple Text Editor")

# Create a text area
text_area = Text(root, wrap="word")
text_area.pack(expand="yes", fill="both")

# Create a menu bar
menu_bar = tk.Menu(root)

# Create File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)  # Fix the error here
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add File menu to menu bar
menu_bar.add_cascade(label="File", menu=file_menu)

# Configure the menu bar
root.config(menu=menu_bar)

# Run the application
root.mainloop()
