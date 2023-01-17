#from main import DataManipulator
import pandas as pd

df = pd.read_excel("studentsgrades.xlsx")
print(df)

rubric = df.iloc[0,0]
print(rubric)
