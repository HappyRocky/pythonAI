# 分形树叶
import numpy as np
import matplotlib.pyplot as pl
import time

# 蕨类植物叶子的迭代函数和概率
eq1 = np.array([[0,0,0],[0,0.16,0]])
p1 = 0.01
eq2 = np.array([[0.2,-0.26,0],[0.23,0.22,1.6]])
p2 = 0.07
eq3 = np.array([[-0.15, 0.28, 0],[0.26,0.24,0.44]])
p3 = 0.07
eq4 = np.array([[0.85, 0.04, 0],[-0.04, 0.85, 1.6]])
p4 = 0.85

def ifs(p, eq, init, n):
    # 迭代向量的初始化
    pos = np.ones(3, dtype=np.float)
    pos[:2] = init # pos=[x,y,1]
    
    # 通过函数概率，计算函数的选择序列
    p = np.add.accumulate(p) # 累加，[p1,p1+p2,p1+p2+p3,...]
    rands = np.random.rand(n) # array，0~1的随机数，长度为10
    select = np.ones(n, dtype=np.int) # 想要得到的效果：select[i]=m表示第i个序列为m(0<=m<=len(p)-1)
    for i,x in enumerate(p[::-1]): # p[x:y:z]表示从x遍历到y，间隔为z。p[::-1]表示将前两个省略，间隔为-1，前两个默认为p[len(p)-1]到p[0]
        select[rands<x] = len(p)-i-1 # i=0时，x=p[len(p)-1]一定为1，因此第一步所有位置都赋为 len(p)-1。i=1时，x小于1，有一部分会满足rands<x。这一部分被赋值为 len(p)-2。这两次迭代的差集会永远被赋值为 len(p)-1不会变，则这个差集上的所有序列永远选择了第 len(p)-1 个迭代函数。
    
    # 结果的初始化
    result = np.zeros((n,2), dtype=np.float)
    c = np.zeros(n, dtype=np.float)
    
    for i in range(n):
        eqidx = select[i] # 所选函数的下标
        temp = np.dot(eq[eqidx], pos) # 迭代公式
        pos[:2] = temp # 更新迭代向量
        
        # 保存结果
        result[i] = temp # 第i次的结果：[x,y]
        c[i] = eqidx # 第i次的选择
    
    return result[:,0],result[:,1],c

start = time.clock()
x, y, c = ifs([p1,p2,p3,p4],[eq1,eq2,eq3,eq4], [-1,5], 100000)
print(time.clock() - start)
pl.figure(figsize=(6,6))
pl.subplot(121)
pl.scatter(x, y, s=1, c="g", marker="s", linewidths=0) # s=1表示散列点大小为1，c="g"表示点的颜色为green，marker="s"表示点的形状为正方形（速度最快）
pl.axis("equal")
pl.axis("off")
pl.subplot(122)
pl.scatter(x, y, s=1,c = c, marker="s", linewidths=0) # c=c表示按照每次迭代选择的序列来作为颜色，方便知道四个函数产生的点的大概位置
pl.axis("equal")
pl.axis("off")
pl.subplots_adjust(left=0,right=1,bottom=0,top=1,wspace=0,hspace=0)
pl.gcf().patch.set_facecolor("white")
pl.show()
