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

# 切片
a = np.arange(10)
b = slice(2,7,2)
print(a[b])
print(a[2:7:2])
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print('初始化a=\n',a)
print('第二行=\n',a[1,...])
print('第二列=\n',np.transpose([a[...,1]]))
print('第二列和第三列=\n',np.transpose([a[...,1:]]))

# 高级索引
a = np.array([[1,2],[3,4],[5,6]])
x = np.array([[0,0],[2,2]])
y = np.array([[0,1],[0,1]])
print('a=\n',a)
print('四个角的元素：\n',a[x,y])

# 布尔索引
print(a[~(a*a>2)])

# asarray和array的区别
a = [1,1] # a是一般数组
b = np.array(a) # array和asarray没有区别，都是会创建一个新的ndarray对象
c = np.asarray(a)
a[1] = 2
print('a=',a)
print('b=',b) # a的变化不会影响到b和c
print('c=',c)

a = np.ones(2,dtype='i') # a本身就是ndarray对象
b = np.array(a) # array会复制一个ndarray对象给b
c = np.asarray(a) # asarray不会复制，而是和a占用同一个内存
a[1] = 2
print('a=',a)
print('b=',b) # a的变化与b无关
print('c=',c) # a与c是同一个内存，即同一个对象

# 迭代
a = np.arange(0,60,5)
a = a.reshape(3,4)
b = a.reshape(4,3)
print('a=',a)
print('b=',b)
print('a迭代：')
for x in np.nditer(a):
    print(x,end=' ')
print('\nb迭代：')
for x in np.nditer(b):
    print(x,end=' ')
a[0,0]=-1
print('a=',a)
print('b=',b)

# 视图和复制，视图会访问原数据，但是shape可以不同，复制是数据全部复制一遍，两个就完全没关系了
a = np.ones([2,3],dtype='i')
b = a.view()
print('a=',a,'id(a)=',id(a))
print('b=',b,'id(b)=',id(b))
a[0,0]=-1
print('a=',a,'id(a)=',id(a))
print('b=',b,'id(b.T)=',id(b.T))

a = np.ones([2,3],dtype='i')
b = a.copy()
print('a=',a,'id(a)=',id(a))
print('b=',b,'id(b)=',id(b))
a[0,0]=-1
print('a=',a,'id(a)=',id(a))
print('b=',b,'id(b.T)=',id(b.T))