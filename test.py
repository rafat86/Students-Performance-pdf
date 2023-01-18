from main import StudentCertificate
import pandas as pd
#print(std_grades)

std_grades = pd.read_excel("studentsgrades.xlsx")
columns_names = std_grades.iloc[:, 3:].columns.tolist()
rubric_elements = len(columns_names)
rubric = columns_names[0:rubric_elements-1]

#print(rubric)


grades_wieghts = []

i = 3
while i < (rubric_elements-1)+3:
    grades_wieghts.append(std_grades.iloc[0, i])
    i = i+1

print(grades_wieghts)
''''
my_rubric = StudentCertificate("rubric")
my_rubric.set_rubric()
print(my_rubric.get_rubric())
'''