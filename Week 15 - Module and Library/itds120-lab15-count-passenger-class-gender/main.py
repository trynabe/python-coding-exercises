'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab15-count-passenger-class-gender
**/
'''
# Your Python code goes here
import pandas as pd
df = pd.read_csv("data.csv")

df_male = df[(df["Sex"] == "male") & (df["Age"] > 40)]
df_female = df[(df["Sex"] == "female") & (df["Age"] > 40)]

male_count = df_male["Pclass"].value_counts().to_dict()
female_count = df_female["Pclass"].value_counts().to_dict()

print("male (age>40)")
for pclass in sorted(male_count.keys()):
    print(f"Pclass {pclass}: {male_count[pclass]}")

print("female (age>40)")
for pclass in sorted(female_count.keys()):
    print(f"Pclass {pclass}: {female_count[pclass]}")