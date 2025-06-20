class To_Do_List:
    tasks=[]
    def add_task(self):
        
        choose=int(input('enter how many tasks do you want to add :'))
        for i in range(choose):
            task=input('enter a task :')
            To_Do_List.tasks.append(task)
        print('Task added succesfully!')

    def view_task(self):
        if not To_Do_List.tasks:
            print('no tasks found')
        else:
            for index,i in enumerate(To_Do_List.tasks,1):
                print(f'{index} : {i}')

    def delete_task(self):
        self.view_task()
        try:
            index=int(input('enter a task number,that you want to delete :'))
            if(1<=index<=len(To_Do_List.tasks)):
                remove=To_Do_List.tasks.pop(index-1)
                print(f'deleted task :{remove}')
            else:
                print('invalid task number!')
        except ValueError:
            print('enter a valid number')
    
    def save_task(self):
        with open('tasks.txt','w')as f:
            for i in To_Do_List.tasks:
                f.write(i+'\n')
            print('task saved to file successfully')
    def load_task(self):
        try:
            with open('tasks.txt','r')as f:
                for line in f:
                    To_Do_List.tasks.append(line.strip())
                print('tasks loaded from file!')
        except FileNotFoundError:
            print('no saved tasks found')
    
    def menu(self):
        while(True):
                print("\n--- To-Do List ---")
                print("1. Add Task")
                print("2. View Tasks")
                print("3. Delete Task")
                print("4. Save Tasks")
                print("5. Load Tasks")
                print("6. Exit")
                choice=int(input('enter a choice :'))

                if(choice==1):
                    self.add_task()
                elif(choice==2):
                    self.view_task()
                elif(choice==3):
                    self.delete_task()
                elif(choice==4):
                    self.save_task()
                elif(choice==5):
                    self.load_task()
                elif(choice==6):
                    print('exit the program!')
                    break
                else:
                    print('invalid choice try again')

    

obj=To_Do_List()
obj.menu()



