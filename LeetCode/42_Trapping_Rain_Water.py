# -*- coding: utf-8 -*-

'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

给定n个非负整数，代表一个高程地图，整数值为高度，宽度均为1.
计算下雨之后，整体可以存储多少水。

示例：
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

'''
import matplotlib.pyplot as plt
def trap(height):
    """
    :type height: List[int]
    :rtype: int
    递归。
    寻找到最高的两个柱子，他们两个之间形成的水池，高度就是两个柱子之间较低的那个。
    其之间的柱子高度都不高于他们两个，相当于水底的小山丘，占据了水的体积，需要减掉。
    然后，这两个柱子，将整个地图分成了三部分，中间这一部分刚刚已经计算过，使用递归继续处理剩下的两个水池。
    最后，三个水池的水的体积相加即可。
    """
    
    l = len(height)
    if l <= 2:
        return 0
    
    # 1、寻找两个最高的柱子
    max1_idx = 0 if height[0] > height[1] else 1 # 最大值的索引
    max2_idx = 1 - max1_idx # 第二大值的索引
    for i in range(2, l):
        h = height[i]
        if h > height[max1_idx]:
            max2_idx = max1_idx
            max1_idx = i
        elif h > height[max2_idx]:
            max2_idx = i
    
    # 2、计算两个柱子之间的水量
    # 获取较低的高度
    small_height = min(height[max1_idx], height[max2_idx])
    if small_height == 0: # 较低高度为0，说明全场只有一根柱子有高度，存不了水
        return 0
    left_idx = min(max1_idx, max2_idx)
    right_idx = max(max1_idx, max2_idx)
    # 先计算两根柱子之间的容量
    middle_vol = max((right_idx - left_idx - 1) * small_height, 0)
    # 再减去之间的其他柱子所占据的体积
    middle_vol -= sum(height[left_idx + 1 : right_idx])
    
    # 3、递归计算剩余部分的水量
    return middle_vol + trap(height[:left_idx+1]) + trap(height[right_idx:])

def trap2(height):
    """
    :type height: List[int]
    :rtype: int
    维护左右两个指针，作用是进行遍历。
    维护左右两个已扫描过的柱子中的最高柱子，作用是与当前指针计算高度差，高度差即为这根柱子上面的水的体积。
    """
    left,right = 0, len(height)-1
    maxleft , maxright= 0,0
    ret = 0
    while left <= right:
        if height[left] <= height[right]: # 左边低于右边
            if height[left] < maxleft: # 左边当前高度小于左边最大高度
                ret += maxleft - height[left] # 高度查为当前柱子上面的水量
            else: # 左边当前高度大于左边最大高度
                maxleft = height[left] # 更新左边最大高度
            left += 1

        else: # 右边低于左边
            if height[right] < maxright:
                ret += maxright - height[right]
            else:
                maxright = height[right]
            right -= 1

    return ret
        
if '__main__' == __name__:
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    
    # 画出柱状图
    X = list(range(0, len(height)))
    Y = height
    plt.bar(X, Y, 1)
    plt.ylim(0, max(Y)+1) 
    for a,b in zip(X,Y):
        plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=11) 
    plt.show()
    
    print(trap2(height))
    
    
    
    