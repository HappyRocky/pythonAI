# 问题：给定两个字符串A和B，要求判断A是否包含B，如果包含返回第一次出现B的index
class FindSubStr:
    def __init__(self, source, target):
        self.source = source
        self.target = target
        
    # 最传统的方法，双重循环，O(m*n)
    def findByCommon(self):
        if self.source is None or self.target is None:
            return -1
        for i in range(len(self.source) - len(self.target) + 1):
            for j in range(len(self.target)):
                if self.source[i + j] != self.target[j]:
                    break
            else: # 此else对应的是for，表示for循环没有被break过
                return i
        return -1
    
    # 新的方法，O(m) + O(n)
    def findByKMP(self):
        if self.source is None or self.target is None:
            return -1
        
        '''
        根据已有的next_list，求下一个next的值
        '''
        def getNext(self, next_list):
            idx = len(next_list) - 1 # 当前next_list的最大索引
            if idx == -1: # next为空，所求为第一个字符的next值，固定为-1
                return -1
            k = next_list[idx] # next_list最后一位的值
            while k != -1:
                if self.target[idx] == self.target[k]: # 新来的值是否等于最长匹配前后缀后面的那个字符
                    return k+1
                k = next_list[k] # 更新最长匹配前后缀的长度
            return 0
        
        # 构造next数组
        next_list = list()
        while len(next_list) < len(self.target):
            next_list.append(getNext(self, next_list))
        print('next_list:',next_list)
        
        # 开始检索
        i = 0 # source字符串的索引
        j = 0 # target字符串的索引
        while i < len(self.source):
            if self.source[i] == self.target[j]: # 字符相同，则都往右移一位继续比较
                i += 1
                j += 1
                if j == len(self.target): # target的最后一个字符都匹配到了，则匹配成功
                    return i - j # 返回匹配字符串的第一个字符的索引，所以需要减去子字符串长度
            else:
                j = next_list[j] # 字符不同，按照next_list更新target的索引
                if j == -1: # 因为next_list[0]=-1，所以说明当前的source字符连target的第一个字符都不匹配，则从source的下一个字符开始检索
                    j = 0
                    i += 1
        return -1
        
if __name__ == '__main__':
    S = FindSubStr('bababaabd','abaabd')
    print('source:',S.source) 
    print('target:',S.target)
    print(S.findByCommon())
    print(S.findByKMP())  
