import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBookApp:
    def __init__(self, root):
        self.contacts = []
        self.root = root
        self.root.title("Contact Book")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)
        
        tk.Label(self.root, text="Phone:").grid(row=1, column=0)
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=1, column=1)
        
        tk.Label(self.root, text="Email:").grid(row=2, column=0)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=2, column=1)
        
        tk.Label(self.root, text="Address:").grid(row=3, column=0)
        self.address_entry = tk.Entry(self.root)
        self.address_entry.grid(row=3, column=1)
        
        tk.Button(self.root, text="Add Contact", command=self.add_contact).grid(row=4, column=0)
        tk.Button(self.root, text="View Contacts", command=self.view_contacts).grid(row=4, column=1)
        tk.Button(self.root, text="Search Contact", command=self.search_contact).grid(row=5, column=0)
        tk.Button(self.root, text="Update Contact", command=self.update_contact).grid(row=5, column=1)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).grid(row=6, column=0)

        self.contact_listbox = tk.Listbox(self.root, width=50)
        self.contact_listbox.grid(row=7, column=0, columnspan=2)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        
        if name and phone:
            self.contacts.append(Contact(name, phone, email, address))
            self.clear_entries()
            self.refresh_contact_list()
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Name and phone number are required!")

    def view_contacts(self):
        self.refresh_contact_list()

    def search_contact(self):
        search_term = self.name_entry.get() or self.phone_entry.get()
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                self.contact_listbox.insert(tk.END, f"{contact.name} - {contact.phone}")

    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            name = self.name_entry.get()
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()
            if name and phone:
                self.contacts[index] = Contact(name, phone, email, address)
                self.clear_entries()
                self.refresh_contact_list()
                messagebox.showinfo("Success", "Contact updated successfully!")
            else:
                messagebox.showerror("Error", "Name and phone number are required for update!")
        else:
            messagebox.showerror("Error", "Please select a contact to update!")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            del self.contacts[selected_index[0]]
            self.refresh_contact_list()
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Please select a contact to delete!")

    def refresh_contact_list(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact.name} - {contact.phone}")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
