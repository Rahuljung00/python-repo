import numpy as np

#initialize 3D array

mat1 = np.array([

[11,12,13,14,15],
[6,7,8,9,10]

])
print(mat1)
print()
mat2 = np.array([
[1,2,3,4,5],
[6,7,8,9,10]

])

print(mat2)

out = np.dot(mat1,mat2)
print(out)