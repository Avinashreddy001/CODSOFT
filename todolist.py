import tkinter as tk
from tkinter import messagebox


class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"{self.description} - {status}"


class ToDoListApp:
    def __init__(self, root):
        self.tasks = []
        self.root = root
        self.root.title("To-Do List Application")
        self.root.configure(bg="#F0F0F0")

        self.frame = tk.Frame(self.root, bg="#F0F0F0")
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(
            self.frame, width=50, height=10, bg="#FFF", fg="#000", selectbackground="#ADD8E6", selectforeground="#000"
        )
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.scrollbar.config(command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        self.entry_frame = tk.Frame(self.root, bg="#F0F0F0")
        self.entry_frame.pack(pady=10)

        self.entry = tk.Entry(self.entry_frame, width=40)
        self.entry.pack(side=tk.LEFT, padx=5)

        self.add_button = tk.Button(
            self.entry_frame, text="Add Task", command=self.add_task, bg="#4CAF50", fg="#FFF", activebackground="#45a049"
        )
        self.add_button.pack(side=tk.LEFT)

        self.buttons_frame = tk.Frame(self.root, bg="#F0F0F0")
        self.buttons_frame.pack(pady=10)

        self.complete_button = tk.Button(
            self.buttons_frame, text="Mark as Completed", command=self.mark_task_completed, bg="#008CBA", fg="#FFF", activebackground="#007B9A"
        )
        self.complete_button.pack(side=tk.LEFT, padx=5)

        self.view_button = tk.Button(
            self.buttons_frame, text="View Tasks", command=self.view_tasks, bg="#f44336", fg="#FFF", activebackground="#d32f2f"
        )
        self.view_button.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        description = self.entry.get()
        if description:
            task = Task(description)
            self.tasks.append(task)
            self.entry.delete(0, tk.END)
            self.view_tasks()
        else:
            messagebox.showwarning("Input Error", "Please enter a task description.")

    def mark_task_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks[index].mark_completed()
            self.view_tasks()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

    def view_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks):
            display_text = f"{index + 1}. {task.description}"
            if task.completed:
                self.task_listbox.insert(tk.END, display_text)
                self.task_listbox.itemconfig(tk.END, {'bg':'#d3ffd3', 'fg':'#008000'})
            else:
                self.task_listbox.insert(tk.END, display_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
