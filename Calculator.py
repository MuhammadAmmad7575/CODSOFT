import tkinter as tk

def update_display(value):
    current_text = display.get()
    if current_text == "0":
        display.set(value)
    else:
        display.set(current_text + value)

def calculate_result():
    try:
        result = eval(display.get())
        display.set(str(result))
    except:
        display.set("Error")

def clear_display():
    display.set("0")

root = tk.Tk()
root.title("Calculator")

display = tk.StringVar()
display.set("0")
display_label = tk.Label(root, textvariable=display, font=("Arial", 24), padx=10, pady=10)
display_label.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

row_val = 1
col_val = 0

button_colors = {
    '7': 'lightblue', '8': 'lightblue', '9': 'lightblue', '/': 'lightgray',
    '4': 'lightblue', '5': 'lightblue', '6': 'lightblue', '*': 'lightgray',
    '1': 'lightblue', '2': 'lightblue', '3': 'lightblue', '-': 'lightgray',
    '0': 'lightblue', '.': 'lightblue', '=': 'lightgreen', '+': 'lightgray',
    'C': 'red'
}

for button in buttons:
    if button != 'C':
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18),
                  command=lambda b=button: update_display(b) if b != '=' else calculate_result(),
                  bg=button_colors.get(button, 'white')).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18),
                  command=clear_display, bg=button_colors.get(button, 'white')).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
