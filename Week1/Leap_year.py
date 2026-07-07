year=int(input("Enter the Year: "))
if year>0:
    if year%4!=0:
        print("Not a Leap Year.")
    elif year%100!=0:
        print("It is a leap Year")
    elif year%400==0:
        print("It is leap Year")
    else:
        print("Not a leap Year")
else:
    print("Invalid Value")
    