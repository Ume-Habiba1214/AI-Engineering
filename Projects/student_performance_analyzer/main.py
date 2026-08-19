import students

marks = {
    "Python": 85,
    "Math": 78,
    "English": 90
}
print(students.calculate_average(marks))
print(students.check_result(marks))
print(students.calculate_grade(students.calculate_average(marks)))
print(students.get_highest_marks_subjects(marks))
print(students.get_lowest_mark_subjects(marks))