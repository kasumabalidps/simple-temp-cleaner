import os
import shutil
import ctypes
from tkinter import Tk, Label, Button, messagebox, Checkbutton, IntVar, PhotoImage

def empty_temp_folder():
    temp_folder = os.getenv('TEMP')
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

def empty_recycle_bin():
    try:
        result = ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 0x0007)
        if result == 0:
            messagebox.showinfo("Success", "Recycle Bin has been cleaned.")
        else:
            messagebox.showerror("Error", "Failed to clean Recycle Bin.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to clean Recycle Bin: {str(e)}")

def clean_system():
    empty_temp_folder()
    if var_recycle_bin.get() == 1:
        empty_recycle_bin()

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
var_recycle_bin = IntVar()
check_recycle_bin = Checkbutton(root, text="Empty Recycle Bin", variable=var_recycle_bin, font=("Helvetica", 14), bg="#f5f5f5", fg="#333", selectcolor="#d3d3d3")
check_recycle_bin.pack(pady=10)

# Clean Button
Button(root, text="Clean", command=clean_system, font=("Helvetica", 14), bg="#007BFF", fg="white", relief="flat", padx=20, pady=10).pack(pady=20)

root.mainloop()