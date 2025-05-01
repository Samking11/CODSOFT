# SIMPLE CALCULATOR (GUI Version using tkinter)

import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x300")

        self.num1_var = tk.StringVar()
        self.num2_var = tk.StringVar()
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Enter First Number:").pack(pady=5)
        tk.Entry(self.root, textvariable=self.num1_var).pack(pady=5)

        tk.Label(self.root, text="Enter Second Number:").pack(pady=5)
        tk.Entry(self.root, textvariable=self.num2_var).pack(pady=5)

        tk.Button(self.root, text="Add", command=self.add).pack(pady=2)
        tk.Button(self.root, text="Subtract", command=self.subtract).pack(pady=2)
        tk.Button(self.root, text="Multiply", command=self.multiply).pack(pady=2)
        tk.Button(self.root, text="Divide", command=self.divide).pack(pady=2)

        tk.Label(self.root, text="Result:").pack(pady=5)
        tk.Label(self.root, textvariable=self.result_var, font=('Arial', 12, 'bold')).pack(pady=5)

    def get_input(self):
        try:
            num1 = float(self.num1_var.get())
            num2 = float(self.num2_var.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers.")
            return None, None

    def add(self):
        num1, num2 = self.get_input()
        if num1 is not None:
            self.result_var.set(num1 + num2)

    def subtract(self):
        num1, num2 = self.get_input()
        if num1 is not None:
            self.result_var.set(num1 - num2)

    def multiply(self):
        num1, num2 = self.get_input()
        if num1 is not None:
            self.result_var.set(num1 * num2)

    def divide(self):
        num1, num2 = self.get_input()
        if num1 is not None:
            if num2 == 0:
                self.result_var.set("Error: Divide by 0")
            else:
                self.result_var.set(num1 / num2)

if __name__ == '__main__':
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
