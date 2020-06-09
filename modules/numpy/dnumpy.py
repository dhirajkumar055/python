#numpy is faster then list
#Faster to read less bytes of memory
#No type checking when iterating through objects
#Numpy uses contiguos memory

import numpy as np
a=np.array([1,2,3])
#[1,2,3]
d=np.array([np.array([2,3,4]),np.array([3,5])])
#[array([2, 3, 4]) array([3, 5])]
print(d.ndim)
#1 because len of first array is not equal to len of second array
b=np.array([[9,8,7],[6,5,4]])
#[list([2, 3, 4]) list([3, 5])]
print(b.ndim)
#2
print(a.shape)
#(3,) #elements in first row
print(b.shape)
#(2,3) #2rows 3columns
print(a.dtype,a.itemsize)
#(dtype('int64'), 8)
a=np.array([1,2,3], dtype='int16')
#(dtype('int16'), 2)
print(a.dtype,a.itemsize)
print(a.nbytes)
#6
print(b[1][-1])
#4
print(b[0,:])
#[9 8 7]   #printing 0th row
print(b[:,2])
##[7 4]   print 2nd column
b[:,1]=5  
#update first column with 5
#[[9 5 7]
# [6 5 4]]
b[:,2]=[8,78] 
#[[ 9  5  8]
 #[ 6  5 78]]
d=np.zeros((3))
#[0. 0. 0.]
d=np.ones((2,3))
#[[1. 1. 1.]
 #[1. 1. 1.]]
d=np.full((2,2),78,dtype='int32')
#[[78 78]
 #[78 78]]
d=np.full_like(a,77)
#[77 77 77]
d=np.random.rand(3,2) #Generates 3*2 matrix with random numbers
#[[0.38546541 0.94281689]
# [0.77335365 0.45513944]
# [0.04192609 0.58580143]]
d=np.random.random_sample(a.shape)
#[0.8240258  0.66134284 0.08775011]
print(a.shape)
#(3,)
d=np.random.randint(-1,8,size=(3,2)) #Radom integers from -1 to 7
#[[ 3 -1]
# [ 2  3]
# [-1  5]]
d=np.identity(3)
#[[1. 0. 0.]
# [0. 1. 0.]
# [0. 0. 1.]]
a=np.array([1,2,3])
d=np.repeat(a,3)
#[1 1 1 2 2 2 3 3 3]
d=np.repeat(a,3, axis=0)
#[1 1 1 2 2 2 3 3 3]
a=np.array([[1,2,3]])
d=np.repeat(a,3,axis=0)
#[[1 2 3]
# [1 2 3]
# [1 2 3]]
d=a.copy()
#[[1 2 3]]
d=d+1
#[[2 3 4]]
d=d*2
#[[4 6 8]]
d=d/2
#[[2 3 4]]
d=d-1
#[[1 2 3]]
d=d**2
#[[1 4 9]]
d=np.cos(a)
[[ 0.54030231 -0.41614684 -0.9899925 ]]
d=a.copy()
d=a+d
#[[2 4 6]]
d=d-a
#[[1 2 3]]
a=np.ones((2,3))
b=np.full((3,2),2)
d=np.matmul(a,b)
#[[6. 6.]
# [6. 6.]]
a=np.identity(3)
d=np.linalg.det(a) #dereminant of linear algebra
#1.0
d=np.array([[1,2,3],[4,5,6]])
print(np.min(d))
#1
print(np.max(d))
#6
print(np.min(d,axis=1))
#[1 4]
print(np.min(d,axis=0))
#[1 2 3] All the values of row 0
print(np.max(d,axis=0))
#[4 5 6]
print(np.max(d,axis=1))
#[3 6]
print(np.sum(d))
#21
print(np.sum(d,axis=0))
#column-wise sum
#[5 7 9]
print(np.sum(d,axis=1))
#row-wise sum
#[ 6 15]
d=np.array([[1,2,3,4],[5,6,7,8]])
#[[1 2 3 4]
# [5 6 7 8]]
d=d.reshape((4,2))
#[[1 2]
# [3 4]
# [5 6]
# [7 8]]
d=d.reshape((2,2,2))
a=np.array([1,2,3])
b=np.array([5,6,7])
d=np.vstack([a,b,b]) #length of a and b should be same
#[[1 2 3]
# [5 6 7]
# [5 6 7]]
a=np.ones((2,4))
b=np.zeros((2,2))
d=np.hstack((a,b))
#d=np.genfromtxt('from.txt',delimiter=',')
#d=d.astype('int32')
#[[1. 1. 1. 1. 0. 0.]
# [1. 1. 1. 1. 0. 0.]]
print(d>0)
#[[ True  True  True  True False False]
# [ True  True  True  True False False]]
d=np.array(range(1,10))
#[1 2 3 4 5 6 7 8 9]
d=d[[1,2,8]]
#[2 3 9]
d=np.array(range(1,10))
d=d[[d>4]]
#[5 6 7 8 9]

#np.any(d>50, axis=0)  #True if any of the columnvalue is greater then 50
#np.all(d>50, axis=0)  #True if all the columnvalues are greater then 50

print(d)