import numpy as np

# 自定义类型
student = np.dtype([('name','S20'),  ('age',  'i1'),  ('marks',  'f4')]) 
print(student)
a = np.array([('1',2,3)],dtype=student)
print(a[0]['name'])

# 调整数组大小
a = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.shape)
a.shape = (3, 2)
print(a)
print(a.shape)
a = a.reshape(6,1)
print(a)

# 维度
a = np.array([1,2,3])
print(a.ndim)
a = np.array([[1],[2]])
print(a.ndim)
a = np.array([[[1],[2]],[[3],[4]]])
print(a.ndim)
a = np.arange(24)
a = a.reshape(2,3,4)
print(a.ndim)
print(a[0][0][0])

# 标志
print(a.flags)

# empty
a = np.empty([1,2,3],dtype=int)
print(a)
a = np.zeros((2,3))
b = np.zeros([2,3])
print(a)
print(b)
print(a == b)

