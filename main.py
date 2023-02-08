"""
Final Project: Student PDF Certificate Generation Python Code Using Excel file
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF

title = 'Course Performance Report'

# Inherits fpdf class to modify header and footer for pdf Report


class PDF(FPDF):

    def header(self):
        # font
        self.set_font('helvetica', 'B', 15)
        # Logo
        self.image('ppulogo.png', 10, 8, 25)
        # Calculate width of title and position
        title_w = self.get_string_width(title) + 6
        doc_w = self.w
        self.set_x((doc_w - title_w) / 2)
        # Title
        self.cell(title_w, 10, title, ln=1, align='C')
        # Line break
        self.ln(15)

    def footer(self):
        # Set position of the footer
        self.set_y(-15)
        # set font
        self.set_font('helvetica', 'I', 8)
        # Set font color grey
        self.set_text_color(169, 169, 169)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

# Creating a class containing all methods used in generating PDF Report


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

    def students_names(self):
        names = self.std_df.iloc[1:, 1]
        return names

# Creating a class method to plot and save a pie chart image for the activities weights (same for all students)
    def pie_chart_wights(self):
        plt.pie(self.rubric_weights, radius=1, labels=self.rubric, autopct='%1.2f%%')
        plt.title('Weights distribution for students grades ')
        plt.savefig('charts/rubric_weight.png', dpi=300, bbox_inches='tight')

# Creating a class method to make a list of grades for a student
    def student_grades(self, student_name):
        new_df = self.std_df
        new_df = new_df.set_index("Names")
        return list(new_df.loc[student_name])[2:]

# Creating a class method to make a list of un submitted activities
    def missed_act(self, student_name):
        student_act = self.student_grades(student_name)
        student_missed_list = []
        for i in range(0, self.rubric_length-1):
            if pd.isnull(student_act[i]) is True:
                student_missed_list.append((self.rubric[i]))
        return student_missed_list

# Creating a class method to plot and save a bar chart showing the activities grades for a student
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
        ax.set_title('Activities Grades')
        ax.set_xticks(x)
        ax.set_xticklabels(labels, rotation='horizontal')
        ax.legend()
        fig.tight_layout()
        plt.savefig('charts/'+student_name+'.png', dpi=300, bbox_inches='tight')

# Creating class method to plot and save a bar chat image for the rank of the student to whole class
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
        ax.set_title('Whole Class Ranking')
        ax.set_xticks(class_grades_df["Names"])
        ax.set_xticklabels(student_names_list, rotation='horizontal')
        fig.tight_layout()
        plt.savefig('charts/'+student_name+'rank.png', dpi=300, bbox_inches='tight')

# Creating a class method to generate PDF containing the report contents
    def pdf_report(self, student_name):
        self.pie_chart_wights()
        pie_chart_file = 'charts/rubric_weight.png'
        bar_chart_file = 'charts/'+student_name+'.png'
        student_rank_chart_file = 'charts/'+student_name+'rank.png'
        report_name = student_name + '.pdf'
        course_rubrics = self.get_rubrics()
        course_activities_marks = self.get_rubric_weights()
        student_activities_marks = self.student_grades(student_name)
        student_missed_activities = self.missed_act(student_name)
        self.bar_chart(student_name)
        self.student_rank_chart(student_name)


# Preparing the properties of PDF Report File
        pdf_report = PDF('P', 'mm', 'A4')
        pdf_report.set_auto_page_break(auto=True, margin=15)
        pdf_report.add_page()
        pdf_report.set_font('helvetica', 'BI', 14)

# Preparing the contents of PDF Report File
        pdf_report.cell(10, 10, "Student Name :" + student_name, ln=True)
        pdf_report.cell(10, 10, 'Course activities', ln=True)
        pdf_report.cell(10, 10, str(course_rubrics), ln=True)
        pdf_report.cell(10, 10, 'Course activities Weights', ln=True)
        pdf_report.cell(10, 10, str(course_activities_marks), ln=True)
        pdf_report.cell(10, 10, 'Your grade in each of the course activities and your Total Grade', ln=True)
        pdf_report.cell(10, 10, str(student_activities_marks), ln=True)
        pdf_report.cell(10, 10, 'You missed the following activity/activities', ln=True)
        pdf_report.cell(10, 10, str(student_missed_activities), ln=True)

        pdf_report.ln(50)
        pdf_report.image(pie_chart_file, 50, 150, 120)

        pdf_report.add_page()
        pdf_report.image(bar_chart_file, 50, 50, 120)

        pdf_report.ln(100)
        pdf_report.image(student_rank_chart_file, 40, 150, 150)

        pdf_report.output(report_name)
