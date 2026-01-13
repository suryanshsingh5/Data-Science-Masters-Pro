# NumPy Intro
import numpy as np
l1=[1,2,3,4]
l2=np.array([1,2,4,5])
print(l1,l2)
type(l2), type (l1)

# creating an array in numpy
np.array([1,35,32,543,344]) # on giving list as iterable input
np.array((1,35,32,543,344)) # on giving tuple as iterable input
# checking the dimension of an array
l2.ndim
# We can also fill different type of data in my numpy array also
l3=np.array([1,"hello", True])
print(l3)