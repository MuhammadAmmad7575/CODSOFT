import tkinter as tk
import string
import secrets

def generate_password():
    password_length = int(length_entry.get())
    
    if password_length < 1:
        password_result.set("Password length should be at least 1 character.")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(secrets.choice(characters) for _ in range(password_length))
        password_result.set(generated_password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")  
root.configure(bg='lightblue')  

length_label = tk.Label(root, text="Enter Password Length:", bg='lightblue', font=("Arial", 12))
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg='lightgreen', font=("Arial", 12))
generate_button.pack()

password_result = tk.StringVar()
password_result.set("")
result_label = tk.Label(root, textvariable=password_result, font=("Arial", 14), fg='blue', bg='lightblue')
result_label.pack()

root.mainloop()
