def calculate_average(marks):
    return sum(marks) / len(marks)



marks=[90,80,67,54,98,66]
average = calculate_average(marks)
print(average)

def get_min_max(numbers):
    return min(numbers),max(numbers)

numbers = [45, 12, 89, 34, 67]
smallest, largest= get_min_max(numbers)
print(smallest,largest)


#dictionary comprehension 
names = ["Ali", "Sara", "John"]
length_names={name:len(name) for name in names}
print(length_names)
names = ["Ali", "Sara", "John", "Alexander"]
length_names={name:len(name) for name in names if len(name)>4}
print(length_names)