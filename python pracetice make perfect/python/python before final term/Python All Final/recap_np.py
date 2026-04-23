Q1
import numpy as np
a = np.array([5, 12, 7, 20, 3, 15])
a = np.array(list(map(int,input().split())))
result = a[a > 10]
print(result)

Q2
import numpy as np
row1 = np.array(list(map(int,input().split())))
row2 = np.array(list(map(int,input().split())))
row3 = np.array(list(map(int,input().split())))
block = np.array([row1,row2,row3])
print(block[:2,:2])

Q3
import numpy as np
row1 = np.array(list(map(int,input().split())))
row2 = np.array(list(map(int,input().split())))
block = np.array([row1,row2])
result = np.mean(block,axis=0)
print(result)

Q4
import numpy as np
score = np.array(list(map(int, input().split())))
score[score < 60] = 0
print(score)

Q5
import numpy as np
row1 = np.array(list(map(int,input().split())))
unique, count = np.unique(row1, return_counts=True)
print(f"unique = {unique}")
print(f"counts = {count}")

Q6
import numpy as np
row1 = np.array(list(map(int,input().split())))
row2 = np.array(list(map(int,input().split())))
row3 = np.array(list(map(int,input().split())))
block = np.array([row1,row2,row3])
result = block[block % 2 == 0]
print(result)

Q7
import numpy as np
row1 = np.array(list(map(int,input().split())))
row2 = np.array(list(map(int,input().split())))
block = np.array([row1,row2])
norm = np.linalg.norm(block,axis=1,keepdims=True)
A_normalized = block / norm
print(A_normalized)

Q8
import numpy as np
row1 = np.array(list(map(int,input().split())))
row2 = np.array(list(map(int,input().split())))
row3 = np.array(list(map(int,input().split())))
block = np.array([row1,row2,row3])
col_mean = np.mean(block , axis=0)
col_to_sum = block[:,col_mean > 10]
result = np.sum(col_to_sum)
print(result)

Q9
import numpy as np
block = np.array(list(map(int,input().split())))
compute = block[block > 10]
even = compute[compute % 2 == 0]
print(even)

Q10
import numpy as np
row1 = np.array(list(map(int,input().split())))
row2 = np.array(list(map(int,input().split())))
row3 = np.array(list(map(int,input().split())))
row4 = np.array(list(map(int,input().split())))
block = np.array([row1,row2,row3,row4])
print(block[1:3:,1:3:])

Q11
import numpy as np
row1 = np.array(list(map(int,input().split())))
row2 = np.array(list(map(int,input().split())))
row3 = np.array(list(map(int,input().split())))
block = np.array([row1,row2,row3])
row_mean = np.mean(block,axis=1)
rows_selected = block[row_mean < 10,:]
result = np.max(rows_selected,axis=0)
print(result)

Q12
import numpy as np
row1 = np.array(list(map(int,input().split())))
row2 = np.array(list(map(int,input().split())))
row3 = np.array(list(map(int,input().split())))
block = np.array([row1,row2,row3])
block[block < 50] = 0
block[(block >= 50) & (block < 80)] = 1
block[block >= 80] = 2
print(block)

Q13
import numpy as np
row1 = np.array(list(map(int,input().split())))
row2 = np.array(list(map(int,input().split())))
row3 = np.array(list(map(int,input().split())))
block = np.array([row1,row2,row3])
result = np.std(block,axis=1)
print(result)

Q14
import numpy as np
row1 = np.array(list(map(int,input().split())))
row2 = np.array(list(map(int,input().split())))
block = np.array([row1,row2])
result = block.flatten()
print(result)

Q15
import numpy as np
block = np.array(list(map(int,input().split())))
block = block[block > 5]
unique, count = np.unique(block, return_counts=True)
print(f"unique={unique}")
print(f"counts={count}")
