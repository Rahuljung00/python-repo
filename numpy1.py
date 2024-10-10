import numpy as np
#initialize two D arrays in numpy

arr1 = np.array([[1,2,3,4 ,5], [5,6,7,8,9]])
arr2 = np.array([1,2,3,4,5,6,7,8,9,10,11])

print(arr1)
print(arr2)

print(arr1[0 ,::2]) #increase the indes with +2



print(arr1[0 , 2::]) #print the values form index 2 to all the way up to the end

print(arr1[1 , 1::2]) #print the values form index 1 to all the way up to the end with a step of 2
