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

    def student_rank_chart(self, student_name):
        class_grades_df = self.std_df[["Names", "Total Grade"]].sort_values(by="Total Grade").drop(0)
        student_total = self.student_grades(student_name)[self.rubric_length-1]
        student_rank = list(class_grades_df["Total Grade"]).index(student_total)
        student_total_list = []
        student_names_list = []
        for i in range(len(list(class_grades_df["Total Grade"]))):
            if i == student_rank:
                student_total_list.append(student_total)
                student_names_list.append("You")
            else:
                student_total_list.append(0)
                student_names_list.append(" ")

        fig, ax = plt.subplots()
        width = 0.3
        ax.bar(class_grades_df["Names"], class_grades_df["Total Grade"], width)
        ax.bar(class_grades_df["Names"], student_total_list, width)
        ax.set_ylabel('Grades')
        ax.set_title('Whole Class')
        ax.set_xticks(class_grades_df["Names"])
        ax.set_xticklabels(student_names_list, rotation='horizontal')
        fig.tight_layout()
        plt.savefig('charts/'+student_name+'rank.png', dpi=300, bbox_inches='tight')
