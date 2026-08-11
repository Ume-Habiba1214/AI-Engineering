class ContactManager:
    def __init__(self):
        self.contacts=[]
        

    def add_contact(self,name, age, email, city):
        self.contact={
            "name":name,
            "age":age,
            "email":email,
            "city":city}
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
                while True:
                    try:
                        option=int(input("Enter the Option number:"))
                        break
                    except ValueError:
                        print("Enter the valid Number.")
                found=True
                if option==1:
                    while True:
                        name=input("Enter the Name: ")
                        if name and name.isalpha():
                            contact["name"]=name
                            break
                        else:
                            print("Enter the valid Name to update")
                    
                elif option==2:
                    while True:
                        try:
                            age=int(input("Enter the Age: "))
                            if age>0:
                                contact["age"]=age
                                break
                            else:
                                print("Enter positive integer.")
                        except ValueError:
                            print("Enter the valid number.")
                    
                elif option==3:
                    while True:
                        email=input("Enter the Email Address: ")
                        if email and "@" in email and "." in email:
                            contact["email"]=email
                            break
                        else:
                            print("Enter Valid Email to update")
                elif option==4:
                    while True:
                        city=input("Enter the City: ")
                        if city:
                            contact["city"]=city
                            break
                        else:
                            print("Enter valid city name to update.")
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
            while True:
                try:
                    option=int(input("Enter the Option number: "))
                    break
                except ValueError:
                    print("Please Enter valid Number.")
            if option==1:
                while True:
                    name=input("Enter the Name: ")
                    if name and name.isalpha():
                        break
                    else:
                        print("Enter the valid Name.")
                while True:
                    try: 
                        age=int(input("Enter the Age: "))
                        if age>0:
                            break
                        else:
                            print("Enter Positive integer")
                    except ValueError:
                        print("please enter valid Number")
                while True:
                    email=input("Enter the Email Address: ")
                    if email and "@" in email and "." in email:
                        break
                    else:
                        print("Enter Valid Email.")
                while True:
                    city=input("Enter the city Name: ")
                    if city and city.isalpha():
                        break
                    else:
                        print("Enter valid city name.")
                self.add_contact(name,age,email,city)
            elif option==2:
                while True:
                    name=input("Enter the name to Delete Contact: ")
                    if name and name.isalpha():
                        break
                    else:
                        print("Enter the Valid name to delete. ")
                self.delete_contact(name)
            elif option==3:
                self.view_contacts()
            elif option==4:
                while True:
                    name=input("Enter the name to Search Contact: ")
                    if name and name.isalpha():
                        break
                    else:
                        print("Enter the valid name to search.")
                self.search_contact(name)
            elif option==5:
                while True:
                    name=input("Enter the name to Update Contact: ")
                    if name and name.isalpha():
                        break
                    else:
                        print("Enter the valid name to update")
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