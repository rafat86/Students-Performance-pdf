import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class StudentData:

    def __init__(self, path):
        self.std_df = pd.read_excel(path)

        columns_names = self.std_df.iloc[:, 3:].columns.tolist()
        self.rubric_length = len(columns_names)
        self.rubric = columns_names[0:self.rubric_length - 1]
        self.rubric_weights = []
        i = 3
        while i < (self.rubric_length - 1) + 3:
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

    def missed_act(self, student_name):
        student_act = self.student_grades(student_name)
        print("You Missed This Activity/Activities:")
        for i in range(0, self.rubric_length-1):
            if pd.isnull(student_act[i]) == True:
                print("\n", self.rubric[i])

    def bar_chart(self, student_name):
        labels = self.std_df.iloc[:, 3:].columns.tolist()
        x = np.arange(len(labels))
        student_marks = self.student_grades(student_name)
        rubric_weight = self.rubric_weights + [100]
        width = 0.25
        fig, ax = plt.subplots()
        ax.bar(x, rubric_weight, width, label="Full Grade", color="red")
        ax.bar(x, student_marks, width, label="Your Grade", color="blue")
        ax.set_ylabel('Grades')
        ax.set_title('Activities')
        ax.set_xticks(x)
        ax.set_xticklabels(labels, rotation='horizontal')
        ax.legend()
        fig.tight_layout()
        plt.savefig('charts/'+student_name+'.png', dpi=300, bbox_inches='tight')