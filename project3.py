import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task_description = entry_task.get()
    if task_description:
        tasks.append({'description': task_description, 'completed': False})
        update_task_list()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning('Warning', 'Task description cannot be empty!')

def update_task_list():
    listbox_tasks.delete(0, tk.END)
    for i, task in enumerate(tasks, start=1):
        status = 'Completed' if task['completed'] else 'Not Completed'
        listbox_tasks.insert(tk.END, f"{i}. {task['description']} - Status: {status}")

def mark_completed():
    selected_task_index = listbox_tasks.curselection()
    if selected_task_index:
        selected_task_index = int(selected_task_index[0])
        tasks[selected_task_index]['completed'] = True
        update_task_list()

# GUI setup
root = tk.Tk()
root.title('To-Do List')

label_task = tk.Label(root, text='Task:')
label_task.pack(pady=5)

entry_task = tk.Entry(root, width=30)
entry_task.pack(pady=5)

button_add = tk.Button(root, text='Add Task', command=add_task)
button_add.pack(pady=10)

listbox_tasks = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
listbox_tasks.pack(pady=5)

button_complete = tk.Button(root, text='Mark Completed', command=mark_completed)
button_complete.pack(pady=10)

update_task_list()

root.mainloop()
