from New import StudentData


path = "studentsgrades.xlsx"
std = StudentData(path)

std.pie_chart_wights()

student_name = input("Enter a name for a student:")
print(std.student_grades(student_name))

print(std.get_rubric_weights())


print(std.missed_act(student_name))

std.bar_chart(student_name)