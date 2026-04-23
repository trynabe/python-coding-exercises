'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab15-avg-col-sum-matrix
**/
'''
# Your Python code goes here
import numpy as np

with open('matrix.txt', 'r') as f:
    line = f.readlines()

    n_rows, n_cols = map(int, input().split())
    rows = []

    for r in line[:n_rows]:
        values = list(map(int, r.split()[:n_cols]))
        rows.append(values)
    
input_matrix = np.array(rows, dtype=np.int8)
print(input_matrix)
print(np.mean(input_matrix, axis=0))
print(np.mean(input_matrix, axis=1))


