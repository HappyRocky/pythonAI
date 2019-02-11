# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 14:48:07 2018

@author: gongyanshang1

测试pytorch的自动求导机制
"""

import torch 
from torch import optim

x = torch.tensor([1,2,3])
print(x.requires_grad) # 默认requires_grad=False

x = torch.tensor([1.0,2,3], requires_grad = True)
#x = torch.tensor([1,2,3], requires_grad = True) 会报错，因为只有floating型的Tensor才需要求导
print(x.requires_grad) # True

y = x.dot(x)
print(y)
print(y.requires_grad) # True, 继承了子节点x的requires_grad

y.backward(retain_graph=True) # 反向传播
# 注意，如果不设置retain_graph=True，会默认为None，这样下面再进行反向传播时会报错，因为在第一次反向传播的时候，计算梯度的图被释放了。
print(x.grad) # 输出tensor([2., 4., 6.])。y=x^2，所以导数为 y'=2x=[2,4,6]

y.backward(retain_graph=True) # 再次反向传播
print(x.grad) # 输出tensor([ 4.,  8., 12.])，是第一次反向传播后 x.grad 的 2 倍。
# 这是因为在多次求梯度时，梯度值会不断在历史的基础上进行累加。

x.grad.zero_() # 这句话可以让历史梯度值清零，这样之后再求导就是真实导数了
y.backward(retain_graph=True) # 再次反向传播
print(x.grad) # 输出tensor([2., 4., 6.])，和第一次求导后的结果相同

z = 4 * y # z = 4 * x^2
print(z)
print(z.grad_fn) # MulBackward
print(z.grad_fn.next_functions[0][0]) # DotBackward
# grad_fn 表示 z 是如何从 y 得到 z 的，这个过程就是 MulBackward
# 在前向传播时，会不断构建计算图，输入是子节点，输出是父节点，连线是操作。
# 每次生成一个新的父节点，这个父节点的 grad_fn 就会记录这个操作
# 同时，grad_fn 也会有属性 next_functions，指向了子节点的 grad_fn
# 也就是说，如果链路很长，那么从最后的输出（顶部节点）开始求导，求到最后的子节点（用户自己创建的节点），
# 只需要不断进行 z.grad_fn.next_functions[0][0].next_functions[0][0]... 即可
# 然后将每个环节求得的导数相乘，即可得到子节点的导数（链式法则）。

print(y)
print(z.grad_fn(y)) # 输出4*y，对应 z=4*y，说明 grad_fn 还是正向的，并不真的是grad函数

x.grad.zero_()
z.backward()
print(z.grad, y.grad, x.grad) # y和z的grad都是None，只有 x.grad = tensor([ 8., 16., 24.])
# 这是因为只有叶子节点才有grad，叶子节点是用户创建的、不是通过其他节点生成的
# 并不是所有叶子节点都有grad，只有设置了retain_graph=True的节点才会有grad
# 如果不是叶子节点，则无论有没有retain_graph=True，都没有grad

# detach()会返回一个requires_grad = False的Tensor
xx = x.detach()
xx.data[0] = 0.9
print(x) # requires_grad=True，但是 x[0] = 0.9，说明对xx的操作也会影响到x
print(xx) # requires_grad=False

# 最简易版本的梯度下降法： y = x^2 - 2x + 1，则 x=1时，y取最小值0
x = torch.tensor([3.5], requires_grad = True)
lr = 0.1 # 学习率
thd = 0.1 # 判断收敛的阈值
while(True):
    y = x*x - 2 * x + 1
    y.backward() # BP
    print(f'x={x.data}\ty={y.data}')
    if abs(x.grad) < thd: # 收敛
        break
    x.data -= lr * x.grad # 更新x
    x.grad.zero_() # 重要！！ 梯度清零
print(f'x={x.data.item()}时，y达到最小值，最小值为{y.data.item()}')

# 使用 optimizer 进行梯度下降法
x = torch.tensor([3.5], requires_grad = True)
optimizer = optim.SGD([x], lr=lr, momentum=0.9)
while(True):
    y = x*x - 2 * x + 1 # y = x^2 - 2x + 1，则 x=1时，y取最小值0
    y.backward() # BP
    print(f'x={x.data}\ty={y.data}')
    if abs(x.grad) < thd: # 收敛
        break
    optimizer.step()
    optimizer.zero_grad()
print(f'x={x.data.item()}时，y达到最小值，最小值为{y.data.item()}')

