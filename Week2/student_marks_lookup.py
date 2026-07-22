def find_marks(students, name):
    for key,value in students.items():
        if name.capitalize() == key:
            return value
    return "Student Not Found."


def find_marks_without_loop(students,name):
    name=name.capitalize()
    if name in students:
        return students[name]

    return "Student Not Found."






students = {
    "Ali": 85,
    "Sara": 91,
    "Ahmed": 78,
    "Sami":90
}
name=input("Enter the name of student: ")
result=find_marks(students,name)
print(result)
answer=find_marks_without_loop(students,name)
print(answer)