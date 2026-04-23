Array Creation & Shapes

1. Create an integer array of 5 zeros.
expect: shape (5,), integer
import numpy as np
a = np.zeros(5,dtype="int")
print(a,a.shape)

2. Create a 2×3 array of zeros with float dtype.
expect: shape (5,), integer
import numpy as np
a = np.zeros((2,3),dtype="float")
print(a)

3. Create evenly spaced integers [0, 2, 4, 6, 8].
fill proper arguments
import numpy as np
c = np.arange(0,10,2)
print(c)

4. Multiple choice: shapes
import numpy as np
x = np.arange(12).reshape(3,4)
print(x)
Answers = B.(3,4)

Indexing, Slicing, Boolean Masks
Complete the slices : Given

import numpy as np
x = np.array([[10, 20, 30],[40, 50, 60],[70, 80, 90]])
print(x)

1. Select the second column (as a 1D view): # expect: [20 50 80]
import numpy as np
cols2 = x[:,1]
print(cols2)

2. Select the first two rows and last two columns: # expect: [[20,30],[50,60]]
import numpy as np
block = x[0:2:,1::]
print(block)

3. Select elements greater than or equal to 50 (boolean filter giving a 1D result): # expect: [50 60 70 80 90]
import numpy as np
ge50 = x[x >= 50]
print(ge50.flatten())

4. Which lines correctly build a boolean mask?
Select all that apply (assume x is a NumPy array):
A. mask = x > 0 , B. mask = (x % 2 == 0) & (x < 50) , D. mask = (x == 3) | (x == 7) , E. mask = ~(x > 100)

Element-wise Operations vs Aggregation
Complete the code: element-wise operations

import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])

s = np.add(a,b) # addition → [5 7 9]
d = np.subtract(a,b) # subtraction → [-3 -3 -3]
m = np.multiply(a,b) # multiply → [ 4 10 18]
q = np.divide(b,a) # divide → [4.  2.5 2. ]
for i in [s,d,m,q]:
    print(i)

True/False Mark True if axis can be passed to the function.
False - np.add(..., axis=1)
True - np.sum(..., axis=1)
True - np.mean(..., axis=0)
False - np.multiply(..., axis=0)

Aggregation with axis : Given
import numpy as np
y = np.array([[1,  2,  3],[10, 20, 30]])

Fill in the blanks
import numpy as np
1. Row sums (shape (2,)): # expect: [ 6 60 ]
row_sums = np.sum(y,axis=1)
print(row_sums)

2. Column means (shape (3,)): # expect: [5.5 11.  16.5]
import numpy as np
col_means = np.mean(y,axis=0)
print(col_means)

3. Global min and max:
import numpy as np
gmin = np.min(y) # expect: 1
gmax = np.max(y) # expect: 30
print(gmin,gmax)

4. Row maxs (shape (2,)):
import numpy as np
row_max = np.max(y,axis=1) # expect: [ 3 30 ]
print(row_max)

5. Column standard deviations (shape (3,)):
import numpy as np
col_std = np.std(y,axis=0)
print(col_std)

Unique & Counting : Given
import numpy as np
z = np.array([3, 1, 2, 3, 2, 1, 3])

1. Get the sorted unique values: # expect: [1 2 3]
import numpy as np
u = np.unique(z)
print(u)

2. Get unique values and their counts: # expect: vals=[1 2 3], cnts=[2 2 3]
import numpy as np
vals , cnts = np.unique(z, return_counts=True)
print(f"vals={vals}, cnts={cnts}")

Short Coding Tasks
Compute basic statistics

Read a 2D array and print:
- Sum of all elements
- Mean of all elements
- Row-wise maximum values
- Column-wise standard deviation

import numpy as np
n_rows , n_cols = input().strip().split()
n_rows , n_cols = int(n_rows) , int(n_cols)
rows = []
for r in range(n_rows):
    values = input().strip().split()
    rows.append(np.array(values))
input_matrix = np.array(rows, dtype=np.int8)
print(f"sum={np.sum(input_matrix)}")
print(f"mean={np.mean(input_matrix)}")
print(f"row_max={np.max(input_matrix,axis=1)}")
print(f"col_std={np.std(input_matrix,axis=0)}")

Count labels using np.unique(..., return_counts=True)
1.
import numpy as np
number = int(input())
labels = list(map(int, input().split()))
vals , cnts = np.unique(labels, return_counts=True)
print(vals)
print(cnts)
print(vals[np.argmax(cnts)])

2
import numpy as np

number = int(input())
x = np.array(input().split(), dtype=np.uint8)

uni , cnts = np.unique(x , return_counts=True)

print(f"unique={uni}")
print(f"count={cnts}")
print(f"most_frequent={uni[np.argmax(cnts)]}")

Selecting specific rows and columns Given:

import numpy as np
A = np.array([[10, 20, 30],[40, 50, 60],[70, 80, 90]])
print(A)

1. Select the first row # expect: [10 20 30]
row1 = A[0:1:,::]
print(row1)

2. Select the last column # expect: [30 60 90]
last_col = A[:,2:]
print(last_col)

3. Select the middle element (row=1, col=1) # expect: 50
mid = A[1:2,1:2]
print(mid)

4. Select the top-left 2×2 block # expect: [[10 20],[40 50]]
block = A[0:2,0:2]
print(block)

Selecting multiple rows or columns Given:

import numpy as np
B = np.array([[ 1,  2,  3,  4],[ 5,  6,  7,  8],[ 9, 10, 11, 12]])

1. Select rows 0 and 2
expect: [[ 1  2  3  4]
         [ 9 10 11 12]]
rows_0_2 = B[[0,2],:]
print(rows_0_2)

2. Select columns 1 and 3
expect: [[ 2  4]
         [ 6  8]
         [10 12]]
cols_1_3 = B[:,[1,3]]
print(cols_1_3)

Selecting rows with conditions Given:
import numpy as np
C = np.array([[10, 15, 20],[25, 30, 35],[40, 45, 50]])

1. Select rows where the first column ≥ 20
expect: [[25 30 35]
         [40 45 50]]

cond = C[:,0] >= 20
filered = C[cond]
print(filered)

2. Select rows where the last column < 40
expect: [[10 15 20]
         [25 30 35]]

cond = C[:,-1] < 40
filered = C[cond]
print(filered)

Combine Selection and Summation Given:
G = np.array([[10, 20, 30],[40, 50, 60],[70, 80, 90]])

1. Select only the rows where the first column > 20, then print each row together with its row sum.
cond = G[:,0] >= 20
x = G[cond]
for i in x:
    print(f"Row : {i} → sum = {np.sum(i)}")


