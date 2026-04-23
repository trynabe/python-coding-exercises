# numpy = "hello numpy"
# print(numpy)

# import numpy as np
# arr = np.array([1,2,3,4,5])
# print(arr)
# print(type(arr))

# import numpy as np
# arr = np.array(2)
# print(arr)

# import numpy as np
# arr = np.ndim
# print(arr)

# import numpy as np
# number_list = [1,2,3,4,5]
# arr = np.array(number_list)
# print(arr)

# import numpy as np
# number_tuple = (1,2,3,4,5,6,7,8,9,10)
# arr = np.array(number_tuple)
# print(arr)

# import numpy as np
# arr = np.array([[1,2,3],[4,5,6]])
# arr1 = arr.ndim
# print(arr)
# print(arr1)

# import numpy as np
# list_number = [[1,2,3],[4,5,6],[7,8,9]]
# arr = np.array(list_number)
# print(arr)

# import numpy as np
# number_tuple = ((1,2,3),(4,5,6),(7,8,9))
# arr = np.array(number_tuple)
# print(arr)

# import numpy as np
# number_list = [[[1,2,3],[4,5,6],[7,8,9]]]
# arr = np.array(number_list)
# arr1 = arr.ndim
# print(arr)
# print(arr1)

# import numpy as np
# arr = np.array([1,2,3,4,5])
# print(arr[-1] + arr[3])
# print(arr[0] + arr[2])
# print(arr[4] + arr[-1])

# import numpy as np
# number_list = [1,2,3,4,5]
# arr = np.array(number_list)
# arr[2] = 100
# print(arr)

# import numpy as np
# arr = np.array([[1,2],[3,4],[5,6]])
# print(arr[0][0]) #1
# print(arr[0][1]) #2
# print(arr[1][0]) #3
# print(arr[1][1]) #4
# print(arr[2][0]) #5
# print(arr[2][1]) #6

# import numpy as np
# arr = np.array([[1,2],[3,4],[5,6]])
# arr[1][1] = 100
# print(arr)

# import numpy as np
# number_list = [[1,2,3],[4,5,6],[7,8,9]]
# arr = np.array(number_list)
# print(arr[0][0])
# print(arr[0][1])
# print(arr[0][2])
# print(arr[1][0])
# print(arr[1][1])
# print(arr[1][2])
# print(arr[2][0])
# print(arr[2][1])
# print(arr[2][2])

# import numpy as np
# number_list = [[[1,2,3],[4,5,6]]]
# arr = np.array(number_list)
# dimension = arr.ndim
# print(arr)
# print(f"Dimension : {dimension}")

# import numpy as np
# number_list = [[[1,2,3],[4,5,6]]]
# arr = np.array(number_list)
# arr[dept][row][column]
# print(arr)
# print(arr[0][0][0])
# print(arr[0][0][1])
# print(arr[0][0][2])
# print(arr[0][1][0])
# print(arr[0][1][1])
# print(arr[0][1][2])

# import numpy as np
# number_list = [[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]
# arr = np.array(number_list)
# print(arr)
# print(arr[0][0][1])
# print(arr[0][1][1])
# print(arr[1][0][1])
# print(arr[1][1][1])

# import numpy as np
# number_list = [1,2,3,4,5]
# arr1 = np.array(number_list,dtype="int")
# arr2 = np.array(number_list,dtype="float")
# arr3 = np.array(number_list,dtype="complex")
# print(arr1.dtype , arr2.dtype , arr3.dtype)
# print(arr1)
# print(arr2)
# print(arr3)

# import numpy as np
# a = np.zeros(5)
# print(a)

# import numpy as np
# a = np.zeros(5,dtype="int")
# print(a)

# import numpy as np
# number_tuple = (2,2)
# a = np.zeros(number_tuple,dtype="int")
# print(a)

# import numpy as np
# number_list = [3,4]
# a = np.zeros(number_list,dtype="int")
# print(a)

# import numpy as np
# a = np.ones((10,10),dtype="int")
# print(a)

# import numpy as np
# a = np.full(5,10)
# print(a)

# import numpy as np
# # a = np.full((3,3),10)
# # print(a)
# a = np.full((4,5),7)
# print(a)

# import numpy as np
# a = np.empty([4,4])
# print(a)
# b = np.empty((4,4))
# print(b)

# import numpy as np
# a = np.identity(4)
# print(a)
# b = np.identity(5,dtype="int")
# print(b)
# c = np.eye(5)
# print(c)
# d = np.eye(3,4,dtype="int")
# print(d)
# e = np.eye(5,k=1,)
# print(e)

# import numpy as np
# ex. np.linspace(start,stop,number)
# a = np.linspace(1,10)
# print(a)
# b = np.linspace(1,5)
# print(b)
# c = np.linspace(1,5,4)
# print(c)
# d = np.linspace(1,5,endpoint=False)
# print(d)

# import numpy as np
# #how to use np.arange(start,stop,step,dtype="???")
# a = np.arange(10)
# print(a)
# b = np.arange(10.0)
# print(b)
# c = np.arange(1,5)
# print(c)
# d = np.arange(-5,6)
# print(d)
# e = np.arange(4,11,dtype="float")
# print(e)
# f = np.arange(4,11,dtype="complex")
# print(f)
# g = np.arange(1,11,2)
# print(g)

# import numpy as np
# a = np.random.random((2,2))
# print(a)
# b = np.random.random((10,10))
# print(b)

# import numpy as np
# shape count row กับ column
# size count element
# number_list = [1,2,3,4,5]
# number_list1 = [[1,2,3],[4,5,6],[7,8,9]]
# a = np.array(number_list)
# b = np.array(number_list1)
# print(a.shape)
# print(b.shape)
# print(a.size)
# print(b.size)
# print(a.item size)
# print(b.item size)

# import numpy as np
# a = np.arange(1,11)
# print(a)
# print(a[3])
# print(a[4:])
# print(a[2:6])
# print(a[:5])
# b = np.array([10,20,30,40,50,60,70,80,90])
# print(b[1:4])
# print(b[0:4:2])
# print(b[::2])

# import numpy as np
# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(a[start:stop:step,start,stop,step])
#print(a[row,column])
# print(a)
# print(a[:,2:])
# print(a[1:,1:])
# print(a[2:,2:])
# print(a[2:,1:])
# print(a[1:,:])
# print(a[:2,:])
# print(a[:2,2:])
# print(a[1:2,1:2])
# print(a[::2,:])

# import numpy as np
# number_list = [1,2,3,4,5,6,7,8,9]
# x = np.array(number_list)

# index = np.array([1,5,7])
# index = np.array([2,4,6,8])
# print(index)
# print(x[index])

# number_list = [1,2,3,4,5,6,7,8,9]
# x = np.array(number_list)

# b = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(b)

# print(b[[0,2]])
# print(b[[0,2],[2,0]])
# print(b[[0,2],[2]])
# print(b[[0,2],[1]])
# print(x[[2,3,4]])

# import numpy as np
# a = np.arange(1,5)

# print(a)
# print(a + 2)
# print(a + 10)
# print(a - 5)
# print(a * 2)
# print(a ** 2)
# print(a % 2)
# print(a / 3)

# b = np.arange(1,5)
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)
# print(a.shape)
# print(b.shape)

# x = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(x , x.shape)
# y = np.array([[10,11,12],[13,14,15],[16,17,18]])
# print(y , y.shape)

# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x % y)

# import numpy as np
# number = [0,1,2,3,4,5,6,7,8,9]
# x = np.array(number)

# print(x.reshape((2,5)))
# z = x.reshape((2,5))
# print(z)

# x.resize((2,5))
# print(x)

# import numpy as np
# number = [[1,2],[3,4],[5,6]]
# x = np.array(number)

# z = x.flatten()
# print(z)

# y = x.ravel()
# print(y)

# import numpy as np
# number = [[1,2,3],[4,5,6]]
# x = np.array(number)

# print(x.transpose())
# print(x.shape)

# import numpy as np
# x = np.array([10,5,6,78,43,13,24,67,32])
# print(x)
# print(x.sum())
# print(x.prod())
# print(x.mean())
# print(x.max())
# print(x.min())
# print(x.argmax())
# print(x.argmin())

# import numpy as np
# number = [[10,80,70],[40,50,60],[30,20,90]]
# z = np.array(number)
# print(z)
# print(np.min(z,axis=1))
# print(np.min(z,axis=0))
# print(np.max(z,axis=1))
# print(np.max(z,axis=0))
# print(z.shape)

# import numpy as np
# a = np.array([[1,2],[3,4]])
# print(a)
# b = np.array([[11,12],[13,14]])
# x = a.dot(b)
# print(x)

# import numpy as np
# number = [3,4,2,6]
# a = np.array(number)
# b = np.array([6,4,3,2])

# x = np.concatenate((a,b))
# print(x)

# import numpy as np
# a = np.array([[1,2],[3,4]])
# x = np.append(a,[[10],[20]],axis=1)
# print(x)

# import numpy as np
# a = np.array([[1,2],[3,4]])
# print(a)
# x = np.insert(a,3,100)
# print(x)

# import numpy as np
# a = np.array([[1,2],[3,4]])
# x = np.insert(a,2,100,axis=0)
# z = np.insert(a,2,100,axis=1)
# print(x)
# print(z)

import numpy as np
number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
z = np.array(number)
# x = np.split(z,4)
# print(x)

# x = z.reshape(5,4)
# print(x)

# c = np.hsplit(z,4)
c = np.vsplit(z,4)

print(c)