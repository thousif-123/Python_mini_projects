import tkinter as tk
from tkinter import messagebox

class Todo_gui:
    def main_window(self):
        self.root = tk.Tk()
        self.root.title("Todo list app")
        self.root.geometry("300x400")

        self.tasks_listbox = tk.Listbox(self.root, width=40, height=10)
        self.tasks_listbox.pack(pady=20)

        self.task_entry = tk.Entry(self.root, width=25)
        self.task_entry.pack(pady=10)

      
        add_button = tk.Button(self.root, text='Add task', command=self.add_task)
        add_button.pack(pady=5)

        delete_button = tk.Button(self.root, text='Delete task', command=self.delete_task)
        delete_button.pack(pady=5)

        self.root.mainloop()

    def add_task(self):
        task = self.task_entry.get()
        if task != '':
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter the task first!")

    def delete_task(self):
        try:
            select_task_index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(select_task_index)
        except:
            messagebox.showwarning("Warning", "Select a task to delete!")


obj = Todo_gui()
obj.main_window()
