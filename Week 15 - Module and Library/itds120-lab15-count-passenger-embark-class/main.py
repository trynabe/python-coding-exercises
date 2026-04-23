'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab15-count-passenger-embark-class/main.py
'''
# Your Python code goes here
import numpy as np
import pandas as pd
df = pd.read_csv('data.csv')
e = ['S','C','Q','UNK']
a = ['Pclass','Fare','Embarked']
for i in e:
    print(f'Embarked: {i}')
    e_df = df[df['Embarked'] == i]
    x = e_df[a].sort_values(by=['Pclass','Fare'],ascending=[True,False])
    print(x.head(5))
    print(x.tail(5))