#Create a list of your five favorite fruits.
fruits=["Apple",
        "Banana",
        "Pineapple",
        "Kiwi",
        "Grapes"]
print(f" My Favourite Fruit ist {fruits[0]}.")
print(f" My Favourite Fruit ist {fruits[-1]}.")
print(f" Total numbers of fruits are  {len(fruits)}.")



#print Even number in list
numbers = [15, 28, 41, 56, 73, 84, 91, 100]
for number in numbers:
    if number%2==0:
        print(number)


#Check the Student exist in the list 
students = ["Ali", "Abeeha", "Sara", "Ahmed", "John"]
name=input("Enter the name of student: ")
if name in students:
    print( "Student found" )
else:
    print("Student not found")
