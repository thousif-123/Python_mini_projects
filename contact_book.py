class Contact_book:
    contact={}
    def add_contact(self):
        name=input("enter name :")
        phone_number=int(input('enter phone number :'))
        Contact_book.contact[name]=phone_number
        print(f'contact of {name} addedd succesfully!\n')

    def view_contacts(self):
        if not Contact_book.contact:
            print('contact book is empty\n')
        else:
            print('All contacts :')
            for name,phone in Contact_book.contact.items():
                print(f'{name} - {phone}')
            print()
    
    def search_contact(self):
        search_name=input('Search contact :')
        if search_name in Contact_book.contact:
            print(f'{search_name}- {Contact_book.contact[search_name]}\n')
        else:
            print('contact not found!')
    
    def main_loop(self):
        while True:
            print('===Contact Book===')
            print('1 .Add contact')
            print('2 .View contact')
            print('3 .search contact')
            print('4 .Exit')

            choose=int(input('choose 1-4 :\n'))
            if choose==1:
                self.add_contact()
            elif choose==2:
                self.view_contacts()
            elif choose==3:
                self.search_contact()
            elif choose==4:
                print('Thank you and bye, exit!')
                break
            else:
                print("invalid choise!")


obj=Contact_book()
obj.main_loop()
