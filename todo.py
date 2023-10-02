import tkinter as tk

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def update_task(self, index, new_task):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1] = new_task

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]

class ToDoListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.todo_list = ToDoList()

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.pack(pady=10)

        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.pack()

        update_button = tk.Button(root, text="Update Task", command=self.update_task)
        update_button.pack(pady=10)

        self.new_task_entry = tk.Entry(root, width=40)
        self.new_task_entry.pack(pady=10)

        delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        delete_button.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_list.add_task(task)
            self.update_task_list()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        new_task = self.new_task_entry.get()
        if selected_index and new_task:
            self.todo_list.update_task(selected_index[0] + 1, new_task)
            self.update_task_list()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.todo_list.delete_task(selected_index[0] + 1)
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListGUI(root)
    root.mainloop()
