import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

class Tasbih:
    def root_window(self):
        self.root=tk.Tk()
        self.root.title("Tasbih App")
        self.root.geometry('300x400') #root.geometry(widthxheight)
        self.count=0
        # self.adding_images()
        self.count_label=tk.Label(self.root,text=str(self.count),font=('Arial',40),fg='green')
        self.count_label.pack(pady=40)
        self.increase_button=tk.Button(self.root,text="Count",command=self.increase_count,font=("Arial",20),bg='blue')
        self.increase_button.pack(pady=20)
        self.reset_button=tk.Button(self.root,text='Reset',command=self.reset_count,font=("Arial",16),bg='red',fg='white')
        self.reset_button.pack(pady=10)
        self.phrases()

    
    # def adding_images(self):
    #     image = Image.open("/home/sk/tasbih_app/tasbih_image.jpeg")

    #     self.bg_image = ImageTk.PhotoImage(image)  # store in self
    #     bg_label = tk.Label(self.root, image=self.bg_image)

    #     bg_label=tk.Label(self.root,image=self.bg_image)
    #     bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    #     bg_label.lower()
        # selected_label = tk.Label(self.root, text="Current: SubhanAllah", font=("Arial", 14), fg="blue")
    
    def increase_count(self):
        self.count+=1
        self.count_label.config(text=str(self.count))
        
        
    def reset_count(self):
        self.count=0
        self.count_label.config(text=str(self.count))
       
        
    def phrases(self):
        tasbih_phrases=tk.StringVar()
        tasbih_phrases.set("Subhanallah")
        dropdown=tk.OptionMenu(self.root,tasbih_phrases,'Subhanallah','Alhamdulillah','Allahuakbar','Lailaha illallah','Astagfirullah')
        dropdown.config(font=('Arial',14))
        dropdown.pack(pady=20)
        
    
        


obj=Tasbih()
obj.root_window()

obj.root.mainloop()
