import pandas as pd
import matplotlib.pyplot as plt


class StudentData:

    def __init__(self, path):
        self.std_df = pd.read_excel(path)

        columns_names = self.std_df.iloc[:, 3:].columns.tolist()
        self.rubric_elements = len(columns_names)
        self.rubric = columns_names[0:self.rubric_elements - 1]
        self.rubric_weights = []
        i = 3
        while i < (self.rubric_elements - 1) + 3:
            self.rubric_weights.append(self.std_df.iloc[0, i])
            i = i + 1

    def get_rubrics(self):
        return self.rubric

    def get_rubric_weights(self):
        return self.rubric_weights

    def pie_chart_wights(self):
        plt.pie(self.rubric_weights, radius=1, labels=self.rubric, autopct='%1.2f%%')
        plt.title('Weights distribution for students grades ')
        plt.savefig('charts/rubric_weight.png', dpi=300, bbox_inches='tight')

    def student_grades(self, student_name):
        new_df = self.std_df
        new_df = new_df.set_index("Names")
        return list(new_df.loc[student_name])[2:]

