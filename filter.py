import numpy as np 

arr = np.array([1, 2, 3, 4,6,8])
print("the original array is" ,arr)
for x in arr : 
    if x%2 ==0:
        mylist = list(x)
print("even numbers are :",mylist)

#filter the array consisting of even numbers

evennums = arr % 2 == 0
print("even numbers are" ,evennums)

