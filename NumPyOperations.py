# NumPy Operations
# creating numpy arrays
import numpy as np
array1=np.array([1,3,43,54])
print(array1)
array2=np.arange(1,11,2)
print(array2)
array3=np.ones((4,2))
print(array3)
array4=np.zeros((4,1))
print(array4)
array5=np.random.random((5,4))* 100
print(array5)
array6=np.linspace(0,10,num=5)
print(array6)
array7=np.identity(4)
print(array7)
array8=np.eye(4)
print(array8)

# numpy array attributes
array8.ndim
array8.itemsize
array8.size
array8.shape
array9=np.arange(0,12)
array9.reshape(3,4)
array10=np.arange(1,10)
print(array10)
array10.astype(str)
array10.astype(np.int32)
array10.astype(float)

# NumPy Operations
array11=np.arange(1,10).reshape(3,3)
array12=np.arange(11,20).reshape(3,3)
array11+array12

# Array function on numpy arrays
array13=np.arange(1,10)
np.sum(array13)
array14=np.arange(1,10).reshape(3,3)
print(array14) # sum of all
np.sum(array14, axis=0) # coloumn wise sum
np.sum(array14, axis=1) # row wise sum

np.min( array14 ) # min of all
np.min( array14, axis = 0 ) # min coloumn wise
np.min( array14, axis = 1 ) # min row wise

np.max( array14 ) # max of all
np.max( array14, axis = 0 ) # max coloumn wise
np.max( array14, axis = 1 ) # max row wise

# dot product
array15=np.arange(1,10).reshape(3,3)
array16=np.arange(1,13).reshape(3,4)
print( array15)
print(array16)
np.dot(array15,array16)

# indexing and slicing == same as normal list
array15=np.arange(1,10).reshape(3,3)
print( array15)
array15[0:3:2]
array15[0:3]
array15[0]
# loop on array
array15=np.arange(1,10).reshape(3,3)
for i in array15:
    print(f" i is : {i}")
# loop on every element index of array
for i in array15:
    for j in array15:
        print(f" i is : {i}")
        print(f" j is : {j}")
# loop on every element of an array using np.ravel
array15=np.arange(1,10).reshape(3,3)
print( array15)
for i in np.ravel(array15):
    print(f" i is : {i}")
# loop on every element of ana array using np.nditer
array15=np.arange(1,10).reshape(3,3)
print( array15)
for i in np.nditer(array15):
    print(f" i is : {i}")

# broadcasting
array16 = np.arange(1,10).reshape(3,3)
array17= np.arange(1,4).reshape(1,3)
print(array16)
print(array17)
array16+array17