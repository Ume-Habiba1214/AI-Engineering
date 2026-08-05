class ContactMAnager:
    def __init__(self):
        self.contacts=[]
        

    def add_contact(self, name, age, email, city):
        self.contact={

            "name":name,
            "age":age,
            "email":email,
            "city":city
        }
        self.contacts.append(self.contact)
        print("Contact added successfully!")

    def run(self):
        name=input("Enter the Name: ")
        age=int(input("Enter the Age: "))
        email=input("Enter the Email Address: ")
        city=input("Enter the city Name: ")
