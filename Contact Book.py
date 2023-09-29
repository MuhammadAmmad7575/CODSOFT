import tkinter as tk
from tkinter import ttk  

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    contact = {
        'Name': name,
        'Phone': phone,
        'Email': email,
        'Address': address
    }
    
    contacts.append(contact)
    update_contact_list()
    clear_entries()

def update_contact_list():
    contact_tree.delete(*contact_tree.get_children())  
    
    for contact in contacts:
        name = contact['Name']
        phone = contact['Phone']
        email = contact['Email']
        address = contact['Address']
        
        contact_tree.insert('', 'end', values=(name, phone, email, address))

def search_contact():
    search_term = search_entry.get().lower()
    search_results.delete(0, tk.END)
    for contact in contacts:
        name = contact['Name'].lower()
        phone = contact['Phone'].lower()
        if search_term in name or search_term in phone:
            search_results.insert(tk.END, f"{contact['Name']}, {contact['Phone']}")

def update_selected_contact():
    selected_item = contact_tree.selection()
    if selected_item:
        index = contact_tree.index(selected_item)
        new_phone = new_phone_entry.get()
        new_email = new_email_entry.get()
        new_address = new_address_entry.get()

        contacts[index]['Phone'] = new_phone
        contacts[index]['Email'] = new_email
        contacts[index]['Address'] = new_address

        contact_tree.item(selected_item, values=(contacts[index]['Name'], new_phone, new_email, new_address))

        clear_update_entries()

def delete_selected_contact():
    selected_item = contact_tree.selection()
    if selected_item:
        index = contact_tree.index(selected_item)
        del contacts[index]
        contact_tree.delete(selected_item)

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def clear_update_entries():
    new_phone_entry.delete(0, tk.END)
    new_email_entry.delete(0, tk.END)
    new_address_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Contact Manager")
bg_color = "#E0E0E0"  
btn_color = "#4CAF50"  
text_color = "white" 
root.configure(bg=bg_color)

root.geometry("1200x680")

input_frame = tk.Frame(root, bg=bg_color)
input_frame.grid(row=0, column=0, padx=20, pady=20)

button_frame = tk.Frame(root, bg=bg_color)
button_frame.grid(row=0, column=1, padx=20, pady=20)

update_frame = tk.Frame(root, bg=bg_color)
update_frame.grid(row=1, column=1, padx=20, pady=20)

labels = ["Name:", "Phone:", "Email:", "Address:"]
entries = []

for i, label_text in enumerate(labels):
    label = tk.Label(input_frame, text=label_text, bg=bg_color)
    label.grid(row=i, column=0, sticky='w')
    entry = tk.Entry(input_frame, width=40)
    entry.grid(row=i, column=1, padx=10, pady=(0, 10))
    entries.append(entry)

name_entry, phone_entry, email_entry, address_entry = entries
add_button = tk.Button(button_frame, text="Add Contact", command=add_contact, bg=btn_color, fg=text_color)
add_button.grid(row=0, column=0, columnspan=2, padx=10, pady=(0, 10))
search_label = tk.Label(button_frame, text="Search:", bg=bg_color)
search_label.grid(row=1, column=0, sticky='w')
search_entry = tk.Entry(button_frame, width=40)
search_entry.grid(row=1, column=1, padx=10, pady=(0, 10))
search_button = tk.Button(button_frame, text="Search", command=search_contact, bg=btn_color, fg=text_color)
search_button.grid(row=2, column=0, columnspan=2, padx=10, pady=(0, 10))
search_results = tk.Listbox(button_frame, height=8, width=100)
search_results.grid(row=3, column=0, columnspan=2, padx=10, pady=(0, 10))

contact_tree = ttk.Treeview(button_frame, columns=("Name", "Phone", "Email", "Address"), show="headings", height=8)
contact_tree.grid(row=5, column=0, columnspan=2, padx=10, pady=(0, 10))

contact_tree.heading("Name", text="Name")
contact_tree.heading("Phone", text="Phone")
contact_tree.heading("Email", text="Email")
contact_tree.heading("Address", text="Address")

contact_tree.column("Name", width=200)
contact_tree.column("Phone", width=150)
contact_tree.column("Email", width=200)
contact_tree.column("Address", width=200)

scrollbar = tk.Scrollbar(button_frame, orient=tk.VERTICAL, command=contact_tree.yview)
scrollbar.grid(row=5, column=2, sticky='ns')
contact_tree.config(yscrollcommand=scrollbar.set)

update_phone_label = tk.Label(update_frame, text="Update Phone Number:", bg=bg_color)
update_phone_label.grid(row=0, column=0, sticky='w')
new_phone_entry = tk.Entry(update_frame, width=40)
new_phone_entry.grid(row=0, column=1, padx=10, pady=(0, 10))

update_email_label = tk.Label(update_frame, text="Update Email:", bg=bg_color)
update_email_label.grid(row=1, column=0, sticky='w')
new_email_entry = tk.Entry(update_frame, width=40)
new_email_entry.grid(row=1, column=1, padx=10, pady=(0, 10))

update_address_label = tk.Label(update_frame, text="Update Address:", bg=bg_color)
update_address_label.grid(row=2, column=0, sticky='w')
new_address_entry = tk.Entry(update_frame, width=40)
new_address_entry.grid(row=2, column=1, padx=10, pady=(0, 10))

update_button = tk.Button(update_frame, text="Update Selected Contact", command=update_selected_contact, bg=btn_color, fg=text_color)
update_button.grid(row=3, column=0, columnspan=2, padx=10, pady=(0, 10))

delete_button = tk.Button(update_frame, text="Delete Selected Contact", command=delete_selected_contact, bg=btn_color, fg=text_color)
delete_button.grid(row=4, column=0, columnspan=2, padx=10, pady=(0, 10))

update_contact_list()

root.mainloop()
