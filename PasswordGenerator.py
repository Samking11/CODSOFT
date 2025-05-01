# PASSWORD GENERATOR (GUI Version using tkinter)

import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("300x250")

        self.length_var = tk.StringVar()
        self.password_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Enter Password Length:").pack(pady=10)
        tk.Entry(self.root, textvariable=self.length_var).pack(pady=5)

        tk.Button(self.root, text="Generate Password", command=self.generate_password).pack(pady=10)

        tk.Label(self.root, text="Generated Password:").pack(pady=5)
        tk.Entry(self.root, textvariable=self.password_var, state='readonly', width=30).pack(pady=5)

    def generate_password(self):
        try:
            length = int(self.length_var.get())
            if length < 4:
                messagebox.showwarning("Invalid Length", "Password length must be at least 4 characters.")
                return
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_var.set(password)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

if __name__ == '__main__':
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
