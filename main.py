import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class StudentCertificate:
    def __init__(self, path):
        self.std_grades = pd.read_excel(path)
        columns_names = self.std_grades.iloc[:, 3:].columns.tolist()
        rubric_elements = len(columns_names)
        self.rubric = columns_names[0:rubric_elements - 1]
        self.set_grades_wieghts()
        self.grades_wieghts = self.get_grades_wieghts()

    def get_rubric(self):
        return self.rubric

    def get_grades_wieghts(self):
        return self.grades_wieghts

    def set_grades_wieghts(self):
        grades_wieghts = []
        i = 3
        while i < (self.rubric_elements - 1) + 3:
            grades_wieghts.append(self.std_grades.iloc[0, i])
            i = i + 1
        self.grades_wieghts = grades_wieghts

    def pie_chart_wights(self):
        print(self.rubric)
        plt.pie(self.grades_wieghts, radius=1, labels=self.rubric, autopct='%1.2f%%')
        plt.title('Weights distribution for students grades ')
        plt.show()
