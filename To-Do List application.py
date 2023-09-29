from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
        tasks.append(task_string)
        the_cursor.execute('insert into tasks values (?)', (task_string,))
        list_update()
        task_field.delete(0, 'end')

def update_task():
    selected_task = task_listbox.get(task_listbox.curselection())
    new_task_text = task_field.get()
    if selected_task and new_task_text:
        tasks.remove(selected_task)
        tasks.append(new_task_text)
        list_update()
        the_cursor.execute('update tasks set title = ? where title = ?', (new_task_text, selected_task))
        task_field.delete(0, 'end')
    else:
        messagebox.showinfo('Error', 'Select a task to update and provide a new task text.')

def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)

def delete_task():
    try:
        the_value = task_listbox.get(task_listbox.curselection())
        if the_value in tasks:
            tasks.remove(the_value)
            list_update()
            the_cursor.execute('delete from tasks where title = ?', (the_value,))
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

def delete_all_tasks():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')
    if message_box == True:
        while(len(tasks) != 0):
            tasks.pop()
        the_cursor.execute('delete from tasks')
        list_update()

def clear_list():
    task_listbox.delete(0, 'end')

def close():
    print(tasks)
    guiWindow.destroy()

def retrieve_database():
    while(len(tasks) != 0):
        tasks.pop()
    for row in the_cursor.execute('select title from tasks'):
        tasks.append(row[0])

if __name__ == "__main__":
    guiWindow = Tk()
    guiWindow.title("To-Do List")
    guiWindow.geometry("665x400+550+250")
    guiWindow.resizable(True, True)
    guiWindow.configure(bg="#B5E5CF")

    the_connection = sql.connect('listOfTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('create table if not exists tasks (title text)')

    tasks = []

    functions_frame = Frame(guiWindow, bg="Green")

    functions_frame.pack(side="top", expand=True, fill="both")

    task_label = Label(
        functions_frame,
        text="Enter the Task:",
        font=("arial", 14, "bold"),
        background="white",
        foreground="black"
    )

    task_label.place(x=20, y=30)

    task_field = Entry(
        functions_frame,
        font=("Arial", 14),
        width=42,
        foreground="black",
        background="white",
    )

    task_field.place(x=180, y=30)

    add_button = Button(
        functions_frame,
        text="Add Task",
        width=15,
        bg='#2ecc71',
        font=("arial", 14, "bold"),
        command=add_task,
    )

    update_button = Button(
        functions_frame,
        text="Update Task",
        width=15,
        bg='#2ecc71',
        font=("arial", 14, "bold"),
        command=update_task,
    )

    del_button = Button(
        functions_frame,
        text="Delete Task",
        width=15,
        bg='#2ecc71',
        font=("arial", 14, "bold"),
        command=delete_task,
    )

    del_all_button = Button(
        functions_frame,
        text="Delete All Tasks",
        width=15,
        font=("arial", 14, "bold"),
        bg='#2ecc71',
        command=delete_all_tasks,
    )

    exit_button = Button(
        functions_frame,
        text="Exit",
        width=15,
        bg='#2ecc71',
        font=("arial", 14, "bold"),
        command=close,
    )

    add_button.place(x=18, y=80)
    update_button.place(x=240, y=80)
    del_button.place(x=460, y=80)
    del_all_button.place(x=18, y=120)
    exit_button.place(x=240, y=120)

    task_listbox = Listbox(
        functions_frame,
        width=57,
        height=7,
        font=("bold"),
   
        background="WHITE",
        foreground="black",
        selectbackground="#D4AC0D",
        selectforeground="blue"
    )

    task_listbox.place(x=17, y=200)

    retrieve_database()
    list_update()
    guiWindow.mainloop()
    the_connection.commit()
    the_cursor.close()
