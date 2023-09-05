import tkinter as tk
from tkinter import messagebox
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")
def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")
def mark_completed():
    try:
        selected_task_index = listbox.curselection()[0]
        task = listbox.get(selected_task_index)
        completed_listbox.insert(tk.END, task)
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")
def clear_completed():
    completed_listbox.delete(0, tk.END)
root = tk.Tk()
root.title("To-Do List")
entry = tk.Entry(root, width=40)
entry.pack(pady=10)
listbox = tk.Listbox(root, width=40)
listbox.pack()
completed_listbox = tk.Listbox(root, width=40)
completed_listbox.pack()
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
mark_completed_button = tk.Button(root, text="Mark as Completed", command=mark_completed)
clear_completed_button = tk.Button(root, text="Clear Completed", command=clear_completed)
add_button.pack(pady=5)
remove_button.pack()
mark_completed_button.pack()
clear_completed_button.pack()
root.mainloop()

