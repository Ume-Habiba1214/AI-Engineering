class Student:
    def __init__(self,name,roll_number,marks):
        self.name=name
        self.roll_number=roll_number
        self.__marks=marks

    def add_marks(self,numbers):
        if numbers>=0:
            self.__marks+=numbers
    

    def deduct_marks(self,numbers):
        if self.__marks>=numbers:
            self.__marks-=numbers
        else:
            print("Cannot deduct the  Marks")

    def get_marks(self):
        return self.__marks

    def display(self):
        print(f"Name : {self.name}")
        print(f"Roll Number : {self.roll_number}")
        print(f"Marks : {self.__marks}")



student1=Student("Ali",101,80)
student1.display()
student1.add_marks(-50)
student1.display()