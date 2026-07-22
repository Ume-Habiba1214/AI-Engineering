#Dictionary
#print name and course
student = {
    "name": "Abeeha",
    "age": 30,
    "course": "Python"
}
print(student["name"])
print(student["course"])
print()


#add new value in age and another key and print whole dictionary
student["age"]=31
print(student["age"])
student["city"]="munich"
print(student)
print()


#loop through the dictionary and print
for key,value in student.items():
    print(f"{key} : {value}")
print()

#Nested dictionary
employees={
    "Ali":{
        "department":"IT",
        "salary":"5000"
    },
    "Sara":{
        "department":"HR",
        "salary":"4500"
    }
}
employee=input("Enter the eployee Name: ").capitalize()
print(employees.get(employee,"Employee Not Found"))
print(f'ALi works in {employees["Ali"]["department"]}')
print(f'Sara earns {employees["Sara"]["salary"]}')
