#1
import numpy as np 
arr_a = np.array([1,2,3,2,3,4,3,4,5,6])
arr_b = np.array([7,2,10,2,7,4,9,4,9,8])
arr_c = np.intersect1d(arr_a, arr_b)
print(arr_c)
#2
arr_d = np.setdiff1d(arr_a, arr_b)
print(arr_d)

#3
arr_e = np.array([2,6,1,9,10,3,27,8,6,25,16])
arr_f = arr_e[(arr_e>4)&(arr_e<11)]
print(arr_f)