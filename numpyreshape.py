import numpy as np

np1 = np.array([[1, 2, 3,4,5,6 ,7,8,9,10,11,12,13,14,15,16]])
print(np1)

np2 = np1.reshape(2,8)
print(np2)

np3 = np1.reshape(2,2,4) #2 arrays with 3  subarrays of unknown size (mno of elements)

print(np3)


np4 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
print(np4.shape)
print(np4)
np5 = np4.reshape(2,2,4)
print(np5)
print()
np6 = np4.reshape(4,4) #no of rows  4 and no of elements are 4 too
print(np6)
np7 = np6.reshape(-1)
print(np7)