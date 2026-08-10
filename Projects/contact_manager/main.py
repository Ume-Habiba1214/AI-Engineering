class ContactManager:
    def __init__(self):
        self.contacts=[]
        

    def add_contact(self,name, age, email, city):
        self.contact={

            "name":name,
            "age":age,
            "email":email,
            "city":city
        }
        self.contacts.append(self.contact)
        print("Contact added successfully!")



    def delete_contact(self,name):
        found=False
        for index,contact in enumerate(self.contacts):
            if name==contact["name"]:
                self.contacts.pop(index)
                found=True
                break
        if found==False:
            print(f"Contact not found.")
        else:
            print("Contact deleted successfully.")
            





    def view_contacts(self):
        if self.contacts==[]:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(f'Name : {contact["name"]}')
                print(f'Age : {contact["age"]}')
                print(f'Email : {contact["email"]}')
                print(f'City : {contact["city"]}')
                print("-" * 30)


    def search_contact(self,name):
        found=False
        if self.contacts==[]:
                print("No contacts found.")
        else:
            for contact in self.contacts:
                if name==contact["name"]:
                    print(f'Name : {contact["name"]}')
                    print(f'Age : {contact["age"]}')
                    print(f'Email : {contact["email"]}')
                    print(f'City : {contact["city"]}')
                    print("-" * 30)
                    found=True
                    break
        if not found:
            print("Contact not found.")



    def update_contact(self,name):
        found=False
        for contact in self.contacts:
            if name==contact["name"]:
                print("Contact Found")
                print("===== Contact Manager =====")
                print("1. Change Name")
                print("2. Change Age")
                print("3. Change Email")
                print("4. Change City")
                option=int(input("Enter the Option number:"))
                found=True
                if option==1:
                    name=input("Enter the Name: ")
                    contact["name"]=name
                elif option==2:
                    age=int(input("Enter the Age: "))
                    contact["age"]=age
                elif option==3:
                    email=input("Enter the Email Address: ")
                    contact["email"]=email
                elif option==4:
                    city=input("Enter the City: ")
                    contact["city"]=city
                else: 
                    print(" you Enter Wrong Option Number")
                break
        if not found:
            print(f"Contact not found.")
                



    def run(self):
        while True:
            print("===== Contact Manager =====")
            print("1. Add Contact")
            print("2. Delete Contact")
            print("3. View Contacts")
            print("4. Search Contact")
            print("5. Update Contact")
            print("6. Exit")
            print("\n")
            print("Choose Option: ")
            option=int(input("Enter the Option number: "))
            if option==1:
                name=input("Enter the Name: ")
                o
                age=int(input("Enter the Age: "))
                email=input("Enter the Email Address: ")
                city=input("Enter the city Name: ")
                self.add_contact(name,age,email,city)
            elif option==2:
                name=input("Enter the name to Delete Contact: ")
                self.delete_contact(name)
            elif option==3:
                self.view_contacts()9
            elif option==4:
                name=input("Enter the name to Search Contact: ")
                self.search_contact(name)
            elif option==5:
                name=input("Enter the name to Update Contact: ")
                self.update_contact(name)
            elif option==6:
                print("Good Bye!")
                break
            else: 
                print("You Enter Wrong Option Number")
            print()
            print()

manager=ContactManager()
manager.run()