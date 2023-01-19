from New import StudentData
import pandas as pd

path = "studentsgrades.xlsx"
std = StudentData(path)

std.pie_chart_wights()