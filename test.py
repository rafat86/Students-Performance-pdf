from New import StudentData as sd

path = "studentsgrades.xlsx"
std = sd(path)

student_names_df = std.students_names()
print(student_names_df)

#student_name = input("Enter a student Name :")

student_name = "student08"
std.pdf_report(student_name)





print(std.student_grades(student_name))

print(std.get_rubric_weights())


print(std.missed_act(student_name))
