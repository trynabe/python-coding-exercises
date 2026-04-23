'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab15-count-words
**/
'''
# Your Python code goes here
import pandas as pd 
df = pd.read_csv('data.csv')
txt = input()
c = 0
for i in df['text']:
    c += str.count(i,txt)
print(c)