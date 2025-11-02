import numpy as np

A = np.array([[56.0,0.0,4.4,68.0],[1.2,104.0,52.0,8.0], [1.8,135.0,99.0,0.9]])
# axis = 0 → calculates down the columns (column-wise)
# axis = 1 → calculates across the rows (row-wise)

cal = A.sum(axis=0)
print(cal)
# dividing the matrix a by the 1 by 4 matrix
percentage = 100*A/cal.reshape(1,4)
print(percentage)



