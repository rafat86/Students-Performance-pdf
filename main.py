import pandas as pd
#import matplotlib.pyplot as plt
#import numpy as np

std_grades = pd.read_excel("studentsgrades.xlsx")


class StudentCertificate:
    def __init__(self, rubric):
        self.rubric = rubric

    def get_rubric(self):
        return self.rubric

    def set_rubric(self):
        columns_names = std_grades.iloc[:, 3:].columns.tolist()
        rubric_elements = len(columns_names)
        self.rubric = columns_names[0:rubric_elements - 1]
