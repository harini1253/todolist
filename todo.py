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
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Entry for adding tasks
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Buttons for adding and removing tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(side=tk.LEFT, padx=5)

# Listbox to display tasks
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
listbox.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()