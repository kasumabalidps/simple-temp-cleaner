import os
import shutil
from tkinter import Tk, Label, Button, messagebox, Checkbutton, IntVar, PhotoImage

def empty_temp_folder():
    temp_folder = '/tmp'
    try:
        for root, dirs, files in os.walk(temp_folder):
            for file in files:
                try:
                    os.remove(os.path.join(root, file))
                except Exception as e:
                    print(f"Cannot remove file: {file} - {e}")
            for dir in dirs:
                try:
                    shutil.rmtree(os.path.join(root, dir))
                except Exception as e:
                    print(f"Cannot remove directory: {dir} - {e}")
        messagebox.showinfo("Success", "Temp folder has been cleaned.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to clean Temp folder: {str(e)}")

def empty_trash():
    trash_folder = os.path.expanduser('~/.local/share/Trash')
    try:
        for root, dirs, files in os.walk(trash_folder):
            for file in files:
                try:
                    os.remove(os.path.join(root, file))
                except Exception as e:
                    print(f"Cannot remove file: {file} - {e}")
            for dir in dirs:
                try:
                    shutil.rmtree(os.path.join(root, dir))
                except Exception as e:
                    print(f"Cannot remove directory: {dir} - {e}")
        messagebox.showinfo("Success", "Trash has been cleaned.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to clean Trash: {str(e)}")

def clean_system():
    empty_temp_folder()
    if var_trash.get() == 1:
        empty_trash()

# Create UI
root = Tk()
root.title("Cleaner System")
root.geometry("400x300")
root.configure(bg="#f5f5f5")

# Use custom icon
script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir, 'image.png')

if os.path.exists(icon_path):
    root.iconphoto(False, PhotoImage(file=icon_path))
else:
    print(f"Icon file not found at: {icon_path}")

# Title Label
Label(root, text="Cleaner System", font=("Helvetica", 20, "bold"), bg="#f5f5f5", fg="#333").pack(pady=20)

# Checkbox
var_trash = IntVar()
check_trash = Checkbutton(root, text="Empty Trash", variable=var_trash, font=("Helvetica", 14), bg="#f5f5f5", fg="#333", selectcolor="#d3d3d3")
check_trash.pack(pady=10)

# Clean Button
Button(root, text="Clean", command=clean_system, font=("Helvetica", 14), bg="#007BFF", fg="white", relief="flat", padx=20, pady=10).pack(pady=20)

root.mainloop()
