import tkinter as tk
import random

class Color_Picker_game:
    def main(self):
        self.root=tk.Tk()
        self.root.title("Random Color changer")
        self.root.geometry("400x300")
        self.colors=['red', 'green', 'blue', 'yellow', 'pink', 'orange', 'purple', 'cyan' ,'black','white','grey','brown']
    
    def change_color(self):
        choosen_color=random.choice(self.colors)
        self.root.configure(bg=choosen_color)
        
    
    def buttons(self):
        change_button=tk.Button(self.root,text='Click me to change the color',command=self.change_color,font=('Arial',14),bg='white',fg='black')
        change_button.pack(pady=100)
        self.root.mainloop()

obj=Color_Picker_game()
obj.main()
obj.change_color()
obj.buttons()

        