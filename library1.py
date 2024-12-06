import numpy as np

# 0 DIMENSION IN ARRAY:-

arr = np.array(20)
print(arr)
print(type(arr))
print(arr.ndim)

# 1 DIMENSION IN ARRAY:-
 
arr = np.array([1,2,3,4,5])
print("values of the array:-",arr)
print("type of the array:-",type(arr))
print("length of the array:-",len(arr))
print("Dimension of the array:-",arr.ndim)

arr = np.array((6,7,8,9,10))
print(arr)
print(type(arr))
print(arr.ndim)
 
# 2 DIMENSION IN ARRAY:-

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
print(type(arr))
print(arr.ndim)

# DIMENSION IN ARRAY:-

arr = np.array([[[1,2,3],[4,5,6],[8,9,10]]])
print(arr)
print(type(arr))
print(arr.ndim)

# ALL ARRAY WILL SHOW IN ONE ANSWER:-

arr0 = np.array(20)
arr1 = np.array([1,2,3,4,5,6])
arr2 = np.array([[1,2,3],[4,5,6]])
arr3 = np.array([[[1,2,3],[4,5,6],[8,9,10]]])

print(arr0)
print(arr1)
print(arr2)
print(arr3)

print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)


# SLICING IN 1D ARRAY:-

arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5])

arr = np.array([1,2,3,4,5,6])
print(arr[::2])

# SILICING IN 2D ARRAY:-

arr = np.array([[10,20,30,40,50],[60,70,80,90,100]])
print(arr[0,1:5])
print(arr[1,1:4])

# checking the data type of an array:-

arr = np.array([1,2,3,4,5])
print(arr.dtype)

arr = np.array(["animals","bat","cat"])
print(arr.dtype)

# CREATING ARRAYS WITH A DEFINED DATA TYPE:-

arr = np.array([1,2,3,4], dtype="S")
print(arr)
print(arr.dtype)

# CREATE AN ARRAY WITH DATA TYPES 4 BYTES INTEGER:-

arr = np.array([1,2,3,4], dtype = "i4")
print(arr)
print(arr.dtype)

# NUMPY ARRAY SHAPE:-
# the shape of an array is the number of elements in each dimension
# print the shape of an 2d array

arr = np.array([[1,2,3,4],[5,6,7,8]]) 
print(arr.shape)

arr = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]]) 
print(arr.shape)

# JOINING OF NUMPY 1D ARRAYS:-

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
arr = np.concatenate((arr1,arr2))
print(arr)

# JOINING OF NUMPY 2D ARRAYS:-

arr1 = np.array([[1,2,3,4],[5,6,7,8]])
arr2 = np.array([[11,12,13,14],[15,16,17,18]])
arr = np.concatenate((arr1,arr2),axis = 1)
print(arr)

# SPLITTING NUMPY ARRAY:-

arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr,3)
print(newarr)

arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr,4)
print(newarr)

# RAVEL & FLATTEN:-
# convert multidimensional array into 1d array

m = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(m)
print("dimension is:-",m.ndim)
n = m.ravel()
print(n)
print("now the dimension is",n.ndim)

m = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(m)
print("dimension is:-",m.ndim)
n = m.flatten()
print(n)
print("now the dimension is",n.ndim)

m = np.array([[[[1,2,3],[4,5,6],[7,8,9],[10,11,12,]]]])
print(m)
print("dimension is:-",m.ndim)
n = m.ravel()
print(n)
print("now the dimension is",n.ndim)

m = np.array([[[[1,2,3],[4,5,6],[7,8,9],[10,11,12,]]]])
print(m)
print("dimension is:-",m.ndim)
n = m.flatten()
print(n)
print("now the dimension is",n.ndim)
  
# UNIQUE FUNCTION:-

k = np.array([12,4,6,7,8,9,13,14,12,14,13])
print(k)
x = np.unique(k)
print(x)

k = np.array([12,4,6,7,8,9,13,14,12,14,13])
print(k)
x = np.unique(k,return_index = True)
print(x)


k = np.array([12,4,6,7,8,9,13,14,12,14,13])
print(k)
x = np.unique(k,return_index = True,return_counts = True)
print(x)

# DELETE:-

a = np.array([12,13,14,15])
d = np.delete(a,[1])
print(d)

a = np.array([[12,13,14,15],[16,18,19,20]])
print(a)
d = np.delete(a,1,axis = 0)
print()
print(d)