from New import StudentData


path = "studentsgrades.xlsx"
std = StudentData(path)

std.pie_chart_wights()

student_name = input("Enter a name for a student:")
print(std.student_grades(student_name))

