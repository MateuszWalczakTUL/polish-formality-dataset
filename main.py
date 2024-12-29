import pandas as pd

texts = pd.read_csv("dataset.csv", sep=';')

print("Number of all texts: ", len(texts))

print("Number of texts per category [0 - informal, 1 - formal]:")
print(texts['formality_2_categories'].value_counts())

print("Number of texts per category [0 - informal, 1 - moderately formal, 2 - formal]:")
print(texts['formality_3_categories'].value_counts())
