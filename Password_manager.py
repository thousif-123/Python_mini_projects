import tkinter as tk
from tkinter import messagebox
import base64
import os

class Password_manager:
    
    Password_file='password.txt'

    def main_gui(self):
        self.root=tk.Tk()
        self.root.title("Password Manager")
        self.root.geometry("400x300")

        self.input_fields_buttons()  
        self.root.mainloop()


   
    def encrypt_password(self,password):
        return base64.b64encode(password.encode("utf-8")).decode("utf-8")
    
    def decrypt_password(self,encoded_password):
        return base64.b64decode(encoded_password.encode("utf-8")).decode("utf-8")
    
    def save_passwords(self):
        self.website=self.entry_website.get()
        self.username=self.entry_username.get()
        self.password=self.entry_password.get()

        if(self.website=="" or self.username=="" or self.password==""):
            messagebox.showerror("Error","All fields are required!")
            return

        self.encrypted_pw=self.encrypt_password(self.password)

        with open(Password_manager.Password_file,'a')as f:
            f.write(f"{self.website} | {self.username} | {self.encrypted_pw}\n")
        
        messagebox.showinfo('Success',"Password saved successfully!")

        self.entry_website.delete(0,tk.END)
        self.entry_username.delete(0,tk.END)
        self.entry_password.delete(0,tk.END)

    
    def view_passwords(self):
        if not os.path.exists(Password_manager.Password_file):
            messagebox.showinfo("No data found","No saved passwords found!")
            return
        with open(Password_manager.Password_file,'r')as f:
            data=f.readlines()

        if not data:
            messagebox.showinfo("NO data","No saved Passwords Found!")
            return 
        
        result_window=tk.Toplevel(self.root)
        result_window.title("Saved Passwords!")

        for line in data:
            self.website, self.username, self.encrypted_pw = line.strip().split(" | ")
            decrypted_pw=self.decrypt_password(self.encrypted_pw)
            tk.Label(result_window, text=f"{self.website} | {self.username} | {decrypted_pw}", font=("Arial", 12)).pack()

    def input_fields_buttons(self):
        tk.Label(self.root, text="Website:", font=("Arial", 12)).pack()
        self.entry_website = tk.Entry(self.root, width=40)
        self.entry_website.pack()

        tk.Label(self.root, text="Username:", font=("Arial", 12)).pack()
        self.entry_username = tk.Entry(self.root, width=40)
        self.entry_username.pack()

        tk.Label(self.root, text="Password:", font=("Arial", 12)).pack()
        self.entry_password = tk.Entry(self.root, width=40, show="*")
        self.entry_password.pack()
        
        tk.Button(self.root, text="Save Password", command=self.save_passwords, bg="green", fg="white").pack(pady=5)
        tk.Button(self.root, text="View Passwords", command=self.view_passwords, bg="blue", fg="white").pack(pady=5)   


obj=Password_manager()
obj.main_gui()
