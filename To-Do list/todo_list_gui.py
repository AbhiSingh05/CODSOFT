import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.tasks = []
        
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()
        
        self.tasks_listbox = tk.Listbox(root, width=40, height=10)
        self.tasks_listbox.pack(pady=10)
        
        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()
        
        self.refresh_button = tk.Button(root, text="Refresh List", command=self.refresh_tasks)
        self.refresh_button.pack()
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.refresh_tasks()
            messagebox.showinfo("Task Added", f"Task '{task}' added to the list.")
        else:
            messagebox.showwarning("Empty Task", "Please enter a task.")

    def remove_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.tasks[index]
            self.tasks.pop(index)
            self.refresh_tasks()
            messagebox.showinfo("Task Removed", f"Task '{task}' removed from the list.")
        else:
            messagebox.showwarning("No Task Selected", "Please select a task to remove.")
        
    def refresh_tasks(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
