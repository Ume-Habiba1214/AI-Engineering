class ContactManager:
    def __init__(self):
        self.contacts=[]
        self.contact={}
        

    def add_contact(name, age, email, city):
        self.contact={

            "name":name,
            "age":age,
            "email":email,
            "city":city
        }
        self.contacts.append(self.contact)
        print("Contact added successfully!")

    def run():
        print("===== Contact Manager =====")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3.")
        print("Exit")
        print("\n")
        print("Choose Option: ")
        option=int(input("Enter the Option number:"))
        if option==1:
            name=input("Enter the Name: ")
            age=int(input("Enter the Age: "))
            email=input("Enter the Email Address: ")
            city=input("Enter the city Name: ")
            ContactManager.add_contact(name,age,email,city)

ContactManager.run()