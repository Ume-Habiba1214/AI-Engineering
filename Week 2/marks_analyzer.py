
def analyze_marks(marks):
    average=0
    for number in marks:
        average+=number
    average=average/len(marks)
    lowest=marks[0]
    highest=marks[0]
    for i in range(1,len(marks)):
        if lowest>marks[i]:
            lowest=marks[i]
        if highest<marks[i]:
            highest=marks[i]
    
    return average,lowest,highest



marks = [78, 85, 92, 67, 88]
average,lowest,highest=analyze_marks(marks)
print(f"Average: {average}")
print(f"Lowest number: {lowest}")
print(f"Highest number: {highest}")
