from main import StudentData as Sd

path = "studentsgrades.xlsx"
std = Sd(path)

student_names_df = std.students_names()

print("1- Individual report generation")
print("2- All students reports generation")

reader_choice = int(input("Please write the number of your choice: "))

if reader_choice == 1:
    print(student_names_df)
    student_name = input("Enter a student Name :")
    std.pdf_report(student_name)

elif reader_choice == 2:
    count_row = student_names_df.shape[0]  # Gives number of rows
    for i in range(0, count_row):
        student_name = student_names_df.iloc[i]
        std.pdf_report(student_name)
