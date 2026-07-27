class Employee():
    def print_funtion(self):
        print(f"Name : {self.name}")
        print(f"Department : {self.department}")
        print(f"Salary : {self.salary}")



    def __init__(self,name,department,salary):
        self.name=name
        self.department=department
        self.salary=salary

employee1=Employee("ALi","IT",5000)
employee2=Employee("Sara","HR",4500)
employee1.print_funtion()

