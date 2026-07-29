class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def introduce(self):
       print(f"Hello, my name is {self.name} and I am {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade=grade

    def show_grade(self):
        print(f"I got {self.grade} Grade")


student1=Student("Ali",25,"A")
student1.introduce()
student1.show_grade()
    