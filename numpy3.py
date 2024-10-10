import numpy as np 

np1 = np.array([1, 2, 3, 4, 5])

np2 = np1.view()
print("Original array: ", np1)
print("New array: ", np2)

print(np.square(np1)) 
print(np.square(np2))  #Changes in np2 will also reflect in np1 because they are the same array since we are using view() and the changes made in np2 are visible in np1 





np3 = np.array([1, 2, 3, 4, 5])
print("Original array: ", np3)

x =np.sqrt(np3)
print(x)  #Changes in np3 will not reflect in np4 because they are using copy mechanism and the changes made in np3 are not visible in np4 
np4 = np3.copy()
print(np4)
