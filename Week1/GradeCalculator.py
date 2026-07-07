print("Grade Calculator")
marks=int(input("Enter Your Marks (0-100): "))
if marks <=100 and marks>=0:
    if marks<=100 and marks>=90:
        print("A")
    elif marks<=89 and marks>=80:
        print("B")
    elif marks<=79 and marks>=70:
        print("C")
    elif marks<=69 and marks>=60:
        print("D")
    else:
        print("F")
else:
    print("Input is invalid.")