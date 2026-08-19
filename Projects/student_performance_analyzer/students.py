def calculate_average(marks):
    return sum(marks.values())/len(marks)

def check_result(marks):
    average=calculate_average(marks)
    if average>=50:
        return "Pass"
    else:
        return "Fail"


def calculate_grade(average):
    if average<50:
        return "F"
    elif average<55:
        return "D"
    elif average<60:
        return "D+"
    elif average<65:
        return "C"
    elif average<70:
        return "C+"
    elif average<75:
        return "B"
    elif average<80:
        return "B+"
    elif average<85:
        return "A"
    elif average>=85:
        return "A+"


def get_highest_marks_subjects(marks):
    maximum=max(marks.values())
    highest_marks_subjects=[key  for key,value in marks.items() if value==maximum]
    return highest_marks_subjects


def get_lowest_mark_subjects(marks):
    minimun=min(marks.values())
    lowest_marks_subjects=[key  for key,value in marks.items() if value==minimun]
    return lowest_marks_subjects
