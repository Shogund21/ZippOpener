import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import pyzipper
import os

class ZipApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Zip Application")

        self.compress_button = tk.Button(master, text="Compress File", command=self.compress_file)
        self.compress_button.pack()

        self.extract_button = tk.Button(master, text="Extract File", command=self.extract_file)
        self.extract_button.pack()

        self.use_password_var = tk.BooleanVar()
        self.use_password_checkbox = tk.Checkbutton(master, text="Use Password", variable=self.use_password_var)
        self.use_password_checkbox.pack()

    def get_password(self):
        if self.use_password_var.get():
            return simpledialog.askstring("Password", "Enter password:", show='*')
        return None

    def compress_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            zip_path = filedialog.asksaveasfilename(defaultextension=".zip")
            if zip_path:
                password = self.get_password()
                try:
                    if password:
                        with pyzipper.AESZipFile(zip_path, 'w', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zf:
                            zf.setpassword(password.encode())
                            zf.write(file_path, os.path.basename(file_path))
                    else:
                        with pyzipper.ZipFile(zip_path, 'w', compression=pyzipper.ZIP_LZMA) as zf:
                            zf.write(file_path, os.path.basename(file_path))
                    messagebox.showinfo("Success", "File compressed successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def extract_file(self):
        zip_path = filedialog.askopenfilename(filetypes=[("Zip files", "*.zip")])
        if zip_path:
            extract_path = filedialog.askdirectory()
            if extract_path:
                password = self.get_password()
                try:
                    if password:
                        with pyzipper.AESZipFile(zip_path) as zf:
                            zf.setpassword(password.encode())
                            zf.extractall(extract_path)
                    else:
                        with pyzipper.ZipFile(zip_path) as zf:
                            zf.extractall(extract_path)
                    messagebox.showinfo("Success", "File extracted successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {str(e)}")

root = tk.Tk()
app = ZipApp(root)
root.mainloop()