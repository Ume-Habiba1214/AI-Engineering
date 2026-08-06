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

    def run(self):
        while True:
            print("===== Contact Manager =====")
            print("1. Add Contact")
            print("2. Delete Contact")
            print("3. View Contacts")
            print("4. Exit")
            print("\n")
            print("Choose Option: ")
            option=int(input("Enter the Option number:"))
            if option==1:
                name=input("Enter the Name: ")
                age=int(input("Enter the Age: "))
                email=input("Enter the Email Address: ")
                city=input("Enter the city Name: ")
                self.add_contact(name,age,email,city)
            elif option==3:
                self.view_contacts()
            elif option==4:
                print("Good Bye!")
                break

manager=ContactManager()
manager.run()