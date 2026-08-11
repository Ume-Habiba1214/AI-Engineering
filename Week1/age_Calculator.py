print("Age Caluculator")
age=int(input("Enter Your Age: "))
if age>=0 and age<200:
    if age>=0 and age<=12:
        print("Child")
    elif age>12 and age<=18:
        print("Teenager")
    elif age>18 and age<=50:
        print("Adult")
    else:
        print("Senior Citizens")
else:
    print("input is invalid")

