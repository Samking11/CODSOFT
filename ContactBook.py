# CONTACT BOOK (GUI Version using tkinter)

import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

CONTACTS_FILE = 'contacts.json'

# Load contacts from file
def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, 'r') as file:
        return json.load(file)

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = load_contacts()

        self.create_widgets()
        self.display_contacts()

    def create_widgets(self):
        tk.Button(self.root, text="Add Contact", command=self.add_contact).pack(pady=5)
        tk.Button(self.root, text="Search Contact", command=self.search_contact).pack(pady=5)
        tk.Button(self.root, text="Update Contact", command=self.update_contact).pack(pady=5)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).pack(pady=5)

        self.contact_listbox = tk.Listbox(self.root, width=60)
        self.contact_listbox.pack(pady=10)

    def display_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            display = f"{contact['name']} - {contact['phone']}"
            self.contact_listbox.insert(tk.END, display)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter name:")
        phone = simpledialog.askstring("Input", "Enter phone:")
        email = simpledialog.askstring("Input", "Enter email:")
        address = simpledialog.askstring("Input", "Enter address:")

        if name and phone:
            self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
            save_contacts(self.contacts)
            self.display_contacts()
        else:
            messagebox.showwarning("Input Error", "Name and phone are required.")

    def search_contact(self):
        query = simpledialog.askstring("Search", "Enter name or phone number:")
        if query:
            results = [c for c in self.contacts if query.lower() in c['name'].lower() or query in c['phone']]
            if results:
                result_str = "\n".join([f"Name: {c['name']}\nPhone: {c['phone']}\nEmail: {c['email']}\nAddress: {c['address']}\n" for c in results])
                messagebox.showinfo("Search Results", result_str)
            else:
                messagebox.showinfo("Search Results", "No contact found.")

    def update_contact(self):
        selected = self.contact_listbox.curselection()
        if selected:
            index = selected[0]
            contact = self.contacts[index]

            name = simpledialog.askstring("Update", "Enter name:", initialvalue=contact['name'])
            phone = simpledialog.askstring("Update", "Enter phone:", initialvalue=contact['phone'])
            email = simpledialog.askstring("Update", "Enter email:", initialvalue=contact['email'])
            address = simpledialog.askstring("Update", "Enter address:", initialvalue=contact['address'])

            if name and phone:
                self.contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
                save_contacts(self.contacts)
                self.display_contacts()
            else:
                messagebox.showwarning("Input Error", "Name and phone are required.")
        else:
            messagebox.showwarning("Selection Error", "No contact selected.")

    def delete_contact(self):
        selected = self.contact_listbox.curselection()
        if selected:
            index = selected[0]
            confirm = messagebox.askyesno("Confirm Delete", f"Delete {self.contacts[index]['name']}?")
            if confirm:
                del self.contacts[index]
                save_contacts(self.contacts)
                self.display_contacts()
        else:
            messagebox.showwarning("Selection Error", "No contact selected.")

if __name__ == '__main__':
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
